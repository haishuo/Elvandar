"""
Render a high-resolution painted-style fantasy map of Elvandar.

Reads geometry hardcoded from the v6 working sketch (matches the SVGs in this
folder), then composites a raster image with:
  - procedural parchment background
  - heightmap-shaded mountains with directional lighting
  - coastal halo (gaussian-blurred coast in sea)
  - painterly forests (shaded blobs)
  - desert dune shading
  - frozen-north cold tint + frost
  - drawn city icons (walled-city silhouettes)
  - serif italic labels

Output: elvandar_map_painted.png in the same directory.
"""

from __future__ import annotations

import math
import os
import random
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops

# -------------------------------------------------------------
# Configuration
# -------------------------------------------------------------
HERE = Path(__file__).parent
OUT_PATH = HERE / "elvandar_map_painted.png"

# Source viewBox is 1200x900. Render at 3x for a crisp ~4MP image.
SCALE = 3
W, H = 1200 * SCALE, 900 * SCALE

random.seed(7)
np.random.seed(7)


def s(v):
    """Scale a single SVG coordinate to render space."""
    return v * SCALE


def sp(pts):
    """Scale a list of (x, y) points."""
    return [(s(x), s(y)) for x, y in pts]


# -------------------------------------------------------------
# Geometry (lifted from elvandar_map_v1.svg / v6)
# -------------------------------------------------------------

# Continent outline (line approximation of the SVG path)
CONTINENT = [
    (150, 220), (130, 200), (115, 165), (100, 130), (95, 95), (110, 75),
    (145, 65), (200, 60), (280, 55), (380, 52), (500, 50), (620, 52),
    (740, 55), (850, 60), (940, 70), (1010, 90), (1055, 120), (1075, 155),
    (1070, 195), (1050, 230), (1020, 270), (1000, 280),
    (1020, 360), (1010, 440), (990, 510),
    (970, 560), (940, 595), (900, 615),
    (870, 625), (840, 660), (825, 715), (850, 760), (870, 800),
    (855, 825), (815, 815), (780, 775), (755, 720), (740, 670),
    (710, 645), (670, 635), (630, 622), (590, 612), (545, 608), (500, 612),
    (460, 620), (420, 638), (380, 670), (340, 700), (305, 695), (280, 660),
    (240, 615), (195, 560), (165, 490), (145, 410), (140, 330), (150, 220),
]

# Balishan Desert outline
BALISHAN = [
    (455, 525), (435, 555), (430, 580), (445, 605), (460, 615),
    (500, 612), (545, 608), (590, 612), (635, 620),
    (655, 590), (660, 555), (645, 540),
    (620, 520), (580, 512), (540, 510), (495, 510), (470, 515), (455, 525),
]

# Mountain range definitions: list of (x, y) peak points
FROST_SPINE_PEAKS = [
    # west of central spine
    (180, 195), (215, 188), (252, 195), (292, 185), (332, 192),
    (372, 188), (412, 195), (452, 185), (492, 192),
    # east of central spine (gap at 515-565 for the Sentinels intersect)
    (588, 192), (628, 185), (668, 195), (708, 188), (748, 192),
    (788, 185), (828, 195), (868, 188), (908, 192), (948, 190),
]

SENTINEL_PEAKS = [
    (535, 195), (540, 300), (540, 335), (540, 370),
    (540, 405), (540, 440), (540, 475),
]

SMOKEPEAKS = [(735, 252), (760, 267), (785, 252), (810, 267)]
IRONWALL = [(733, 364), (755, 376), (778, 364)]
GEMSPIRE = [(862, 380), (882, 390), (907, 380)]
LYRIC = [(770, 647), (788, 659), (808, 647)]

# Mt. Karagh (the named volcano)
KARAGH = (540, 230)

# Rivers (control points; rendered as smooth polylines)
RIVERS = [
    # Blood
    [(380, 200), (370, 240), (360, 280), (365, 320), (375, 350), (410, 380)],
    # Imperial Vein
    [(215, 270), (205, 320), (200, 380), (215, 430), (235, 490), (255, 555)],
    # Scholar's
    [(700, 220), (695, 260), (690, 300), (695, 340), (710, 380), (720, 395)],
    # Cerulean
    [(850, 685), (855, 720), (860, 760)],
    # Frozen rivers in the north
    [(580, 60), (582, 90), (588, 120), (584, 145), (590, 165), (588, 190)],
    [(320, 55), (323, 90), (330, 120), (327, 140), (333, 155)],
]

# Region borders (curves rendered as polylines)
REGION_BORDERS = [
    [(175, 330), (250, 340), (320, 345), (400, 338), (470, 330)],
    [(590, 320), (680, 330), (760, 335), (860, 328), (950, 320)],
    [(620, 440), (700, 450), (780, 455), (880, 452), (970, 450)],
    [(750, 685), (790, 715), (825, 745)],
]

# Cities: (x, y, name, kind)  kind in {'capital','major'}
CITIES = [
    (545, 600, "Kaha'an", "capital_major"),
    (350, 295, "Takama", "capital"),
    (760, 305, "Mechanus", "capital"),
    (820, 410, "The Ivory Tower", "capital"),
    (900, 540, "Eruliath", "capital"),
    (240, 465, "Vartonne", "capital"),
    (830, 780, "Silaris", "capital"),
    (965, 525, "Port Valen", "major"),
    (880, 475, "Northcrest", "major"),
    (430, 345, "Shizan", "major"),
    (900, 390, "Lumina Vale", "major"),
    (975, 355, "Empirica", "major"),
]

# Region labels: (x, y, text, size, color)
REGION_LABELS = [
    (540, 120, "THE FROZEN NORTH", 56, (40, 60, 80)),
    (320, 268, "Terinok", 48, (110, 50, 30)),
    (780, 268, "Gunastran", 48, (60, 55, 50)),
    (200, 395, "Vartonne", 40, (110, 90, 40)),
    (870, 365, "Uratha", 40, (70, 55, 130)),
    (870, 495, "Erulius", 40, (40, 90, 40)),
    (830, 826, "Silaris", 28, (110, 50, 70)),
]

FEATURE_LABELS = [
    (540, 305, "Mt. Karagh", 18, (130, 30, 30), True),
    (540, 320, "the Red Mountain", 14, (120, 30, 30), True),
    (700, 600, "Balishan Desert", 22, (90, 60, 10), True),
    (430, 613, "The Golden Path", 18, (160, 110, 20), True),
    (775, 685, "Cerulean R.", 14, (60, 100, 130), True),
    (358, 350, "Blood R.", 14, (110, 30, 30), True),
    (200, 430, "Imperial Vein", 14, (60, 100, 130), True),
    (685, 280, "Scholar's R.", 14, (60, 100, 130), True),
    (770, 248, "Smokepeaks", 16, (60, 50, 40), True),
    (755, 358, "Ironwall Mts.", 14, (60, 50, 40), True),
    (882, 375, "Gemspire Peaks", 14, (60, 50, 40), True),
    (790, 640, "Lyric Mts.", 14, (60, 50, 40), True),
    (780, 785, "Whispering Forest", 14, (50, 80, 50), True),
    (518, 535, "Gray Wastes", 14, (60, 50, 50), True),
    (1080, 460, "Azure Sea", 32, (50, 90, 120), True),
    (600, 870, "Azure Sea", 28, (50, 90, 120), True),
    (120, 510, "Western Sea", 26, (50, 90, 120), True),
    (320, 42, "Northern Ice Sea", 22, (60, 95, 130), True),
]


# -------------------------------------------------------------
# Procedural noise helpers
# -------------------------------------------------------------

def value_noise(width: int, height: int, scale: float, octaves: int = 4,
                seed: int = 0) -> np.ndarray:
    """Simple multi-octave value noise. Returns float array in [0, 1]."""
    rng = np.random.default_rng(seed)
    result = np.zeros((height, width), dtype=np.float32)
    amp = 1.0
    norm = 0.0
    for o in range(octaves):
        s_ = scale * (2 ** o)
        gw = max(2, int(width / s_) + 2)
        gh = max(2, int(height / s_) + 2)
        grid = rng.random((gh, gw)).astype(np.float32)
        layer = np.array(Image.fromarray((grid * 255).astype(np.uint8))
                         .resize((width, height), Image.BICUBIC),
                         dtype=np.float32) / 255.0
        result += layer * amp
        norm += amp
        amp *= 0.5
    return result / norm


def gradient_radial(width: int, height: int, cx: float, cy: float,
                    inner: float, outer: float) -> np.ndarray:
    """Return an array in [0,1] that goes from 1 at center to 0 at outer."""
    yy, xx = np.indices((height, width), dtype=np.float32)
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
    g = (outer - d) / (outer - inner)
    return np.clip(g, 0.0, 1.0)


# -------------------------------------------------------------
# Compositing helpers
# -------------------------------------------------------------

def array_to_image(arr: np.ndarray) -> Image.Image:
    """Convert a float [0,1] array (HxWx3 or HxW) to an RGB PIL image."""
    if arr.ndim == 2:
        a = (np.clip(arr, 0, 1) * 255).astype(np.uint8)
        return Image.fromarray(a, mode="L").convert("RGB")
    a = (np.clip(arr, 0, 1) * 255).astype(np.uint8)
    return Image.fromarray(a, mode="RGB")


def overlay_blend(base: np.ndarray, top: np.ndarray, alpha: float = 1.0) -> np.ndarray:
    """Overlay-style blend with alpha."""
    b = base
    t = top
    low = 2 * b * t
    high = 1 - 2 * (1 - b) * (1 - t)
    out = np.where(b < 0.5, low, high)
    return b * (1 - alpha) + out * alpha


def multiply(base: np.ndarray, top: np.ndarray, alpha: float = 1.0) -> np.ndarray:
    return base * (1 - alpha) + (base * top) * alpha


# -------------------------------------------------------------
# Background: parchment paper
# -------------------------------------------------------------

def make_parchment() -> Image.Image:
    """Generate a procedural parchment paper background."""
    print("  parchment...")
    # base sepia color
    base = np.full((H, W, 3), [0.94, 0.86, 0.68], dtype=np.float32)

    # noise layer for paper grain
    grain_fine = value_noise(W, H, scale=4, octaves=4, seed=1)
    grain_coarse = value_noise(W, H, scale=80, octaves=3, seed=2)

    # blend darker fibers
    for c in range(3):
        base[..., c] *= (0.85 + 0.30 * grain_coarse)
        base[..., c] *= (0.92 + 0.16 * grain_fine)

    # warm radial vignette toward edges
    vignette = 1 - 0.45 * (1 - gradient_radial(W, H, W * 0.5, H * 0.5,
                                               0, max(W, H) * 0.65))
    for c in range(3):
        base[..., c] *= vignette

    # corner stains
    for cx, cy, r in [(80, 80, 600), (W - 80, 80, 480), (80, H - 80, 720),
                       (W - 80, H - 80, 600)]:
        stain = 1 - 0.15 * gradient_radial(W, H, cx, cy, 0, r)
        for c in range(3):
            base[..., c] *= stain

    # tint: pull toward warm sepia
    base = base * np.array([1.02, 0.98, 0.84])

    # random ink specks
    rng = np.random.default_rng(3)
    speck_count = 700
    for _ in range(speck_count):
        x = rng.integers(0, W)
        y = rng.integers(0, H)
        r = rng.integers(1, 4)
        intensity = rng.uniform(0.6, 0.9)
        ys, xs = np.ogrid[max(0, y - r):min(H, y + r + 1),
                           max(0, x - r):min(W, x + r + 1)]
        mask = ((ys - y) ** 2 + (xs - x) ** 2) <= r * r
        sub = base[max(0, y - r):min(H, y + r + 1),
                   max(0, x - r):min(W, x + r + 1)]
        sub[mask] *= intensity

    return array_to_image(base)


# -------------------------------------------------------------
# Land mask + heightmap
# -------------------------------------------------------------

def build_land_mask() -> Image.Image:
    """Render the continent outline as a binary mask."""
    mask = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(mask)
    d.polygon(sp(CONTINENT), fill=255)
    return mask


def build_heightmap(land_mask: Image.Image) -> np.ndarray:
    """Build a soft heightmap: 0 at sea, rising into land, with mountain peaks."""
    print("  heightmap...")
    base = np.array(land_mask, dtype=np.float32) / 255.0  # 1 inside land

    # blur to give smooth coastal rise
    soft = np.array(land_mask.filter(ImageFilter.GaussianBlur(radius=10 * SCALE)),
                    dtype=np.float32) / 255.0
    inland = soft * 0.25

    # add mountain bumps
    yy, xx = np.indices((H, W), dtype=np.float32)
    height = inland.copy()

    def add_peak(x, y, peak=1.0, radius=20):
        cx, cy = s(x), s(y)
        r = radius * SCALE
        d2 = (xx - cx) ** 2 + (yy - cy) ** 2
        bump = peak * np.exp(-d2 / (2 * r * r))
        return bump

    # broad ridge under each range
    for px, py in FROST_SPINE_PEAKS:
        height += add_peak(px, py, peak=0.8, radius=22)
    for px, py in SENTINEL_PEAKS:
        height += add_peak(px, py, peak=0.85, radius=24)
    for px, py in SMOKEPEAKS:
        height += add_peak(px, py, peak=0.6, radius=15)
    for px, py in IRONWALL + GEMSPIRE:
        height += add_peak(px, py, peak=0.55, radius=14)
    for px, py in LYRIC:
        height += add_peak(px, py, peak=0.4, radius=10)
    # Karagh — taller
    height += add_peak(*KARAGH, peak=1.4, radius=22)

    # add subtle noise to terrain
    h_noise = value_noise(W, H, scale=20, octaves=4, seed=5)
    height += (h_noise - 0.5) * 0.08

    # mask back to land only
    height *= base
    return height


# -------------------------------------------------------------
# Hill-shading (relief lighting)
# -------------------------------------------------------------

def hillshade(height: np.ndarray, azimuth_deg: float = 315.0,
              altitude_deg: float = 35.0, z_factor: float = 25.0) -> np.ndarray:
    """Standard hill-shading. Returns array in [0, 1]."""
    print("  hillshading...")
    az = math.radians(360.0 - azimuth_deg + 90.0)
    al = math.radians(altitude_deg)

    # gradient
    dy, dx = np.gradient(height * z_factor)
    slope = np.arctan(np.sqrt(dx * dx + dy * dy))
    aspect = np.arctan2(-dx, dy)

    shaded = (np.sin(al) * np.cos(slope) +
              np.cos(al) * np.sin(slope) * np.cos(az - aspect))
    return np.clip(shaded, 0, 1)


# -------------------------------------------------------------
# Apply all the layered look
# -------------------------------------------------------------

def composite_map() -> Image.Image:
    """Build the full painted map."""
    print("Building parchment...")
    img = make_parchment().convert("RGB")

    print("Building land mask...")
    land_mask = build_land_mask()

    print("Building heightmap...")
    height = build_heightmap(land_mask)

    print("Computing hillshade...")
    shade = hillshade(height)

    base = np.array(img, dtype=np.float32) / 255.0

    # ---- SEA: tint everything outside land toward blue-gray, with wave noise
    print("Painting sea...")
    sea_mask = 1.0 - (np.array(land_mask, dtype=np.float32) / 255.0)
    sea_color = np.array([0.72, 0.78, 0.82], dtype=np.float32)
    wave = value_noise(W, H, scale=12, octaves=3, seed=11)
    sea_layer = base.copy()
    sea_tint = sea_color * (0.92 + 0.18 * wave[..., None])
    # blend sea over base where sea_mask
    blend = 0.78
    for c in range(3):
        base[..., c] = base[..., c] * (1 - sea_mask * blend) + sea_tint[..., c] * (sea_mask * blend)

    # add horizontal "engraved" wave hatching in sea
    rng = np.random.default_rng(13)
    for _ in range(W // 6):
        y = rng.integers(0, H)
        x0 = rng.integers(-50, W)
        ln = rng.integers(50, 220)
        x1 = min(W, x0 + ln)
        x0 = max(0, x0)
        if sea_mask[y, x0:x1].mean() > 0.7:
            # darken a row slightly
            t = rng.uniform(0.92, 0.97)
            base[y, x0:x1, :] *= t

    # ---- COASTAL HALO: glow inside the sea around the coast
    print("Coastal halo...")
    coast = land_mask.filter(ImageFilter.GaussianBlur(radius=6 * SCALE))
    coast_arr = np.array(coast, dtype=np.float32) / 255.0
    halo = np.clip(coast_arr - (np.array(land_mask, dtype=np.float32) / 255.0),
                   0, 1)
    halo *= 0.45
    halo_color = np.array([0.55, 0.50, 0.30])
    for c in range(3):
        base[..., c] = base[..., c] * (1 - halo) + halo_color[c] * halo

    # ---- LAND BASE: tint the parchment slightly warmer where land is
    land = np.array(land_mask, dtype=np.float32) / 255.0
    land_tint = np.array([1.02, 0.97, 0.84])
    for c in range(3):
        base[..., c] = np.where(land > 0.5,
                                base[..., c] * land_tint[c], base[..., c])

    # ---- HILLSHADE: multiply onto land only
    print("Applying hillshade...")
    shade_strength = 0.55
    sm = (shade ** 1.2) * land
    for c in range(3):
        base[..., c] = base[..., c] * (1 - sm * shade_strength) + \
                       base[..., c] * sm * (1 + 0.05 * shade_strength)

    # ---- REGION TINTS (very subtle)
    print("Region tints...")
    base = apply_region_tints(base, land_mask)

    # ---- BALISHAN sandstone tint
    print("Desert tint...")
    desert_mask = polygon_mask(BALISHAN)
    desert_arr = np.array(desert_mask, dtype=np.float32) / 255.0
    sand_color = np.array([0.92, 0.78, 0.46])
    for c in range(3):
        base[..., c] = base[..., c] * (1 - desert_arr * 0.55) + \
                       sand_color[c] * (desert_arr * 0.55)
    # add dune ripples
    dune_noise = value_noise(W, H, scale=6, octaves=2, seed=21)
    ripple = (dune_noise - 0.5) * 0.18
    for c in range(3):
        base[..., c] = base[..., c] + ripple * desert_arr

    # ---- FROZEN NORTH: cold blue tint above ~y=215
    print("Frozen north...")
    freeze_mask = make_north_mask(land_mask)
    fa = np.array(freeze_mask, dtype=np.float32) / 255.0
    cold = np.array([0.82, 0.88, 0.92])
    for c in range(3):
        base[..., c] = base[..., c] * (1 - fa * 0.45) + cold[c] * (fa * 0.45)
    # frost stipple
    rng = np.random.default_rng(31)
    for _ in range(2500):
        x = rng.integers(0, W)
        y = rng.integers(0, H)
        if fa[y, x] > 0.5:
            base[y:y + 2, x:x + 2] = np.minimum(base[y:y + 2, x:x + 2] +
                                                 0.10, 1.0)

    # ---- MT KARAGH: hot red overlay on the volcano
    print("Karagh...")
    kx, ky = s(KARAGH[0]), s(KARAGH[1])
    yy, xx = np.indices((H, W), dtype=np.float32)
    karagh_d = np.sqrt((xx - kx) ** 2 + (yy - ky) ** 2)
    karagh_glow = np.clip(1 - karagh_d / (45 * SCALE), 0, 1) ** 1.5
    red = np.array([0.85, 0.20, 0.15])
    for c in range(3):
        base[..., c] = base[..., c] * (1 - karagh_glow * 0.35) + \
                       red[c] * (karagh_glow * 0.35)
    # smoke plume rising
    smoke = np.zeros((H, W), dtype=np.float32)
    for dy in range(0, 90 * SCALE):
        x_off = int(SCALE * 5 * math.sin(dy / (15 * SCALE)))
        for dx in range(-int(15 * SCALE), int(15 * SCALE) + 1):
            xx_ = kx + dx + x_off
            yy_ = ky - dy - int(20 * SCALE)
            if 0 <= xx_ < W and 0 <= yy_ < H:
                rad = abs(dx) / (15 * SCALE)
                smoke[yy_, xx_] += 0.7 * (1 - rad) * \
                                   max(0, 1 - dy / (90 * SCALE))
    smoke = np.clip(smoke, 0, 1) * 0.6
    smoke_blur = np.array(Image.fromarray((smoke * 255).astype(np.uint8))
                          .filter(ImageFilter.GaussianBlur(radius=8 * SCALE)),
                          dtype=np.float32) / 255.0
    smoke_col = np.array([0.30, 0.30, 0.30])
    for c in range(3):
        base[..., c] = base[..., c] * (1 - smoke_blur * 0.6) + \
                       smoke_col[c] * smoke_blur * 0.6

    # ---- FORESTS (Whispering Forest + scattered)
    print("Forests...")
    base = paint_forests(base, land_mask)

    # ---- GRAY WASTES patch
    print("Gray Wastes...")
    base = paint_gray_wastes(base)

    # ---- FINAL: mild grain overlay & contrast
    print("Final grain...")
    fine = value_noise(W, H, scale=2, octaves=2, seed=41)
    for c in range(3):
        base[..., c] = base[..., c] * (0.94 + 0.12 * fine)

    # gentle gamma
    base = np.clip(base, 0, 1) ** 0.96

    img = array_to_image(base)

    # ---- VECTOR-LIKE OVERLAYS (drawn in PIL on top of the painted layers)
    print("Drawing overlays (rivers, borders, mountains, cities, labels)...")
    draw_overlays(img)

    return img


# -------------------------------------------------------------
# Helpers used above
# -------------------------------------------------------------

def polygon_mask(poly_pts) -> Image.Image:
    m = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(m)
    d.polygon(sp(poly_pts), fill=255)
    return m


def make_north_mask(land_mask: Image.Image) -> Image.Image:
    """Return the part of land north of the Frost Spine."""
    rect = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(rect)
    d.rectangle([0, 0, W, s(215)], fill=255)
    return ImageChops.multiply(land_mask, rect)


def apply_region_tints(base: np.ndarray, land_mask: Image.Image) -> np.ndarray:
    """Subtle color cast per nation. Approximate polygons."""
    tints = [
        # (rough polygon, color)
        ([(140, 220), (510, 220), (510, 335), (175, 335), (140, 330)],
         [1.00, 0.92, 0.86]),  # Terinok (rusty)
        ([(565, 220), (1075, 220), (1000, 290), (950, 320), (760, 335),
          (590, 320), (565, 240)],
         [0.96, 0.94, 0.90]),  # Gunastran (smoke)
        ([(140, 335), (320, 345), (470, 330), (510, 335), (510, 510),
          (460, 525), (430, 580), (460, 615), (420, 638), (380, 670),
          (340, 700), (305, 695), (280, 660), (240, 615), (195, 560),
          (165, 490), (145, 410), (140, 330)],
         [1.00, 0.96, 0.82]),  # Vartonne (faded gold)
        ([(565, 320), (590, 325), (760, 335), (950, 320), (1010, 380),
          (1010, 460), (780, 462), (620, 450), (565, 430)],
         [0.94, 0.92, 1.00]),  # Uratha (lavender)
        ([(565, 460), (620, 450), (780, 462), (1010, 460), (1020, 510),
          (990, 555), (940, 595), (900, 615), (870, 625), (840, 660),
          (750, 685), (720, 670), (660, 660), (640, 620), (635, 540),
          (565, 540)],
         [0.93, 0.98, 0.90]),  # Erulius (green)
        ([(750, 685), (790, 715), (825, 745), (850, 760), (870, 800),
          (855, 825), (815, 815), (780, 775), (755, 720), (740, 670)],
         [1.00, 0.92, 0.93]),  # Silaris (rose)
    ]
    land = np.array(land_mask, dtype=np.float32) / 255.0
    for poly, color in tints:
        m = polygon_mask(poly)
        ma = (np.array(m, dtype=np.float32) / 255.0) * land
        col = np.array(color)
        for c in range(3):
            base[..., c] = base[..., c] * (1 - ma * 0.18) + \
                           base[..., c] * col[c] * (ma * 0.18) * 1.4
    return base


def paint_forests(base: np.ndarray, land_mask: Image.Image) -> np.ndarray:
    """Paint the Whispering Forest and a few decorative woodland patches."""
    forests = [
        # Whispering Forest (Silaris)
        [(795, 745), (812, 755), (803, 765), (822, 770), (800, 780),
         (818, 788), (800, 798), (815, 800)],
        # decorative forests
        [(170, 450), (195, 490), (280, 500), (320, 540)],
        [(830, 555), (860, 585), (800, 600)],
        [(765, 420), (850, 440)],
        [(280, 280), (400, 300), (450, 290)],
        [(650, 285), (900, 295)],
    ]
    forest_color = np.array([0.30, 0.45, 0.30])
    for cluster in forests:
        # rasterize a cluster of soft circles
        m = Image.new("L", (W, H), 0)
        d = ImageDraw.Draw(m)
        for (x, y) in cluster:
            r = int(s(8))
            d.ellipse([s(x) - r, s(y) - r, s(x) + r, s(y) + r], fill=140)
            d.ellipse([s(x) - r // 2, s(y) - r // 2,
                       s(x) + r // 2, s(y) + r // 2], fill=200)
        m = m.filter(ImageFilter.GaussianBlur(radius=2 * SCALE))
        ma = np.array(m, dtype=np.float32) / 255.0
        for c in range(3):
            base[..., c] = base[..., c] * (1 - ma * 0.55) + \
                           forest_color[c] * (ma * 0.55)
    return base


def paint_gray_wastes(base: np.ndarray) -> np.ndarray:
    cx, cy = s(518), s(548)
    rx, ry = int(s(28)), int(s(14))
    yy, xx = np.indices((H, W), dtype=np.float32)
    d = ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2
    mask = np.clip(1 - d, 0, 1)
    gray = np.array([0.40, 0.40, 0.42])
    for c in range(3):
        base[..., c] = base[..., c] * (1 - mask * 0.55) + \
                       gray[c] * (mask * 0.55)
    return base


# -------------------------------------------------------------
# Vector-style overlays (rivers, borders, mountain icons, cities, labels)
# -------------------------------------------------------------

def draw_overlays(img: Image.Image):
    d = ImageDraw.Draw(img, "RGBA")

    # rivers
    for r in RIVERS[:4]:  # only main rivers, not frozen-north
        pts = sp(r)
        d.line(pts, fill=(50, 100, 130, 220), width=int(2.5 * SCALE),
               joint="curve")
    for r in RIVERS[4:]:  # frozen rivers
        pts = sp(r)
        d.line(pts, fill=(120, 160, 180, 200), width=int(1.6 * SCALE),
               joint="curve")

    # region borders (dashed feel: short segments)
    for border in REGION_BORDERS:
        pts = sp(border)
        for i in range(len(pts) - 1):
            x0, y0 = pts[i]
            x1, y1 = pts[i + 1]
            steps = 16
            for j in range(steps):
                if j % 2 == 0:
                    continue
                t0 = j / steps
                t1 = (j + 1) / steps
                xa = x0 + (x1 - x0) * t0
                ya = y0 + (y1 - y0) * t0
                xb = x0 + (x1 - x0) * t1
                yb = y0 + (y1 - y0) * t1
                d.line([(xa, ya), (xb, yb)], fill=(100, 70, 30, 180),
                       width=int(1.3 * SCALE))

    # Balishan dashed historical border
    bal = sp(BALISHAN)
    for i in range(len(bal) - 1):
        x0, y0 = bal[i]
        x1, y1 = bal[i + 1]
        steps = 8
        for j in range(steps):
            if j % 2 == 0:
                continue
            t0 = j / steps
            t1 = (j + 1) / steps
            xa = x0 + (x1 - x0) * t0
            ya = y0 + (y1 - y0) * t0
            xb = x0 + (x1 - x0) * t1
            yb = y0 + (y1 - y0) * t1
            d.line([(xa, ya), (xb, yb)], fill=(120, 80, 30, 220),
                   width=int(1.4 * SCALE))

    # Golden Path (dashed)
    path_pts = sp([(200, 615), (260, 632), (320, 648), (380, 633),
                    (440, 622), (500, 605), (545, 600), (600, 600),
                    (660, 605), (740, 615), (820, 628), (900, 615),
                    (950, 600)])
    for i in range(len(path_pts) - 1):
        x0, y0 = path_pts[i]
        x1, y1 = path_pts[i + 1]
        steps = 14
        for j in range(steps):
            if j % 2 == 0:
                continue
            t0 = j / steps
            t1 = (j + 1) / steps
            xa = x0 + (x1 - x0) * t0
            ya = y0 + (y1 - y0) * t0
            xb = x0 + (x1 - x0) * t1
            yb = y0 + (y1 - y0) * t1
            d.line([(xa, ya), (xb, yb)], fill=(190, 140, 30, 240),
                   width=int(2.6 * SCALE))

    # mountain icons (small painted triangles with shading) — drawn on top
    def mountain(cx, cy, w=24, h=16, col=(140, 110, 80, 255)):
        cx, cy = s(cx), s(cy)
        w, h = w * SCALE, h * SCALE
        # base triangle
        d.polygon([(cx - w / 2, cy + h / 2), (cx, cy - h / 2),
                    (cx + w / 2, cy + h / 2)],
                   fill=col, outline=(60, 40, 20, 255))
        # snow cap
        d.polygon([(cx - w * 0.15, cy - h * 0.2), (cx, cy - h / 2),
                    (cx + w * 0.15, cy - h * 0.2)],
                   fill=(245, 245, 240, 230))
        # shadow side
        d.polygon([(cx, cy - h / 2), (cx + w / 2, cy + h / 2),
                    (cx + w * 0.05, cy + h / 2)],
                   fill=(80, 60, 35, 140))

    for x, y in FROST_SPINE_PEAKS:
        mountain(x, y, w=28, h=20)
    # Sentinel range as bigger triangles
    for x, y in SENTINEL_PEAKS:
        mountain(x, y, w=30, h=22, col=(125, 95, 65, 255))
    for x, y in SMOKEPEAKS:
        mountain(x, y, w=22, h=15, col=(110, 100, 95, 255))
    for x, y in IRONWALL:
        mountain(x, y, w=20, h=14, col=(120, 100, 80, 255))
    for x, y in GEMSPIRE:
        mountain(x, y, w=20, h=14, col=(150, 130, 110, 255))
    for x, y in LYRIC:
        mountain(x, y, w=16, h=12, col=(140, 115, 95, 255))

    # Mt Karagh on top
    mountain(KARAGH[0], KARAGH[1], w=42, h=32, col=(165, 50, 40, 255))
    # crater dot
    cx, cy = s(KARAGH[0]), s(KARAGH[1] - 6)
    r = int(2 * SCALE)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(40, 20, 15, 255))

    # cities
    for cx, cy, name, kind in CITIES:
        x, y = s(cx), s(cy)
        if kind.startswith("capital"):
            # walled city: small castle-like silhouette
            big = "major" in kind
            sz = (10 if big else 8) * SCALE
            d.rectangle([x - sz, y - sz * 0.55, x + sz, y + sz * 0.55],
                        fill=(245, 230, 195, 255), outline=(50, 35, 20, 255),
                        width=max(1, SCALE))
            # castellations
            for ox in (-sz, -sz * 0.4, sz * 0.4 - sz * 0.4 + sz * 0.4 - sz):
                pass
            for offset, w in [(-sz, sz * 0.4), (-sz * 0.2, sz * 0.4),
                              (sz * 0.6, sz * 0.4)]:
                d.rectangle([x + offset, y - sz * 0.95,
                             x + offset + w, y - sz * 0.55],
                            fill=(245, 230, 195, 255),
                            outline=(50, 35, 20, 255), width=max(1, SCALE))
            # door
            d.rectangle([x - sz * 0.15, y - sz * 0.05,
                         x + sz * 0.15, y + sz * 0.55],
                        fill=(40, 25, 15, 255))
        else:
            r = 3 * SCALE
            d.ellipse([x - r, y - r, x + r, y + r],
                      fill=(50, 30, 18, 255), outline=(20, 10, 5, 255))
            # tower triangle
            d.polygon([(x, y - r * 1.8), (x - r * 0.9, y - r * 0.4),
                        (x + r * 0.9, y - r * 0.4)],
                       fill=(50, 30, 18, 255))

    # labels
    draw_labels(d)


def draw_labels(d: ImageDraw.ImageDraw):
    """Draw labels with appropriate fonts."""
    font_path = find_font_italic()
    font_path_bold = find_font_bold()

    # cities
    for cx, cy, name, kind in CITIES:
        x, y = s(cx), s(cy)
        size = int((20 if kind.startswith("capital") else 14) * SCALE * 0.7)
        try:
            font = ImageFont.truetype(font_path_bold if kind.startswith("capital")
                                       else font_path, size)
        except Exception:
            font = ImageFont.load_default()
        if kind.startswith("capital"):
            ox = 14 * SCALE
            oy = -2 * SCALE
        else:
            ox = 10 * SCALE
            oy = -10 * SCALE
        # halo
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                d.text((x + ox + dx, y + oy + dy), name,
                       fill=(245, 230, 200, 220), font=font)
        d.text((x + ox, y + oy), name, fill=(40, 25, 15, 255), font=font)

    # region labels
    for cx, cy, text, size, color in REGION_LABELS:
        x, y = s(cx), s(cy)
        try:
            font = ImageFont.truetype(font_path, int(size * SCALE * 0.6))
        except Exception:
            font = ImageFont.load_default()
        bbox = d.textbbox((0, 0), text, font=font)
        w = bbox[2] - bbox[0]
        # halo for readability
        for dx in (-2, 0, 2):
            for dy in (-2, 0, 2):
                d.text((x - w / 2 + dx, y + dy), text,
                       fill=(245, 230, 200, 200), font=font)
        d.text((x - w / 2, y), text, fill=color + (255,), font=font)

    # feature labels
    for entry in FEATURE_LABELS:
        cx, cy, text, size, color, italic = entry
        x, y = s(cx), s(cy)
        try:
            font = ImageFont.truetype(font_path, int(size * SCALE * 0.6))
        except Exception:
            font = ImageFont.load_default()
        bbox = d.textbbox((0, 0), text, font=font)
        w = bbox[2] - bbox[0]
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                d.text((x - w / 2 + dx, y + dy), text,
                       fill=(245, 230, 200, 220), font=font)
        d.text((x - w / 2, y), text, fill=color + (255,), font=font)

    # title cartouche
    title_font_size = int(64 * SCALE * 0.5)
    try:
        title_font = ImageFont.truetype(font_path_bold, title_font_size)
    except Exception:
        title_font = ImageFont.load_default()
    title = "ELVANDAR"
    bbox = d.textbbox((0, 0), title, font=title_font)
    tw = bbox[2] - bbox[0]
    cx_t = W / 2
    cy_t = s(70)
    # banner
    bw = tw + 80 * SCALE
    bh = 60 * SCALE
    d.rounded_rectangle([cx_t - bw / 2, cy_t - bh / 2,
                          cx_t + bw / 2, cy_t + bh / 2],
                         radius=int(15 * SCALE),
                         fill=(238, 218, 175, 235),
                         outline=(60, 40, 20, 255),
                         width=int(1.6 * SCALE))
    d.text((cx_t - tw / 2, cy_t - bbox[3] / 2 - 4 * SCALE), title,
           fill=(60, 25, 18, 255), font=title_font)


def find_font_italic() -> str:
    candidates = [
        "/System/Library/Fonts/Supplemental/Georgia Italic.ttf",
        "/Library/Fonts/Georgia Italic.ttf",
        "/System/Library/Fonts/Supplemental/Georgia.ttf",
        "/Library/Fonts/Palatino.ttc",
        "/System/Library/Fonts/Supplemental/Times New Roman Italic.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf",
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return ""


def find_font_bold() -> str:
    candidates = [
        "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
        "/Library/Fonts/Georgia Bold.ttf",
        "/System/Library/Fonts/Supplemental/Georgia.ttf",
        "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return ""


# -------------------------------------------------------------
# Main
# -------------------------------------------------------------

if __name__ == "__main__":
    img = composite_map()
    img.save(OUT_PATH, optimize=True)
    print(f"Saved {OUT_PATH}  ({W}x{H})")
