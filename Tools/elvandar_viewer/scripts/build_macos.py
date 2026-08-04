from __future__ import annotations

import os
import plistlib
import subprocess
import sys
import tomllib
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ICON = PROJECT_ROOT / "assets" / "ElvandarViewer-transparent.png"
BUILD_ROOT = PROJECT_ROOT / "build"
DIST_ROOT = PROJECT_ROOT / "dist"
APP_BUNDLE = DIST_ROOT / "Elvandar Viewer.app"


def project_version() -> str:
    with (PROJECT_ROOT / "pyproject.toml").open("rb") as handle:
        return str(tomllib.load(handle)["project"]["version"])


def run(*arguments: str) -> None:
    environment = os.environ.copy()
    environment.setdefault(
        "PYINSTALLER_CONFIG_DIR",
        str(BUILD_ROOT / "pyinstaller-config"),
    )
    subprocess.run(arguments, check=True, env=environment)


def build_application() -> None:
    run(
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconfirm",
        "--clean",
        "--windowed",
        "--name",
        "Elvandar Viewer",
        "--icon",
        str(SOURCE_ICON),
        "--osx-bundle-identifier",
        "com.elvandar.viewer",
        "--paths",
        str(PROJECT_ROOT / "src"),
        "--add-data",
        f"{SOURCE_ICON}:assets",
        "--distpath",
        str(DIST_ROOT),
        "--workpath",
        str(BUILD_ROOT / "pyinstaller"),
        "--specpath",
        str(BUILD_ROOT),
        str(PROJECT_ROOT / "scripts" / "entrypoint.py"),
    )

    info_path = APP_BUNDLE / "Contents" / "Info.plist"
    with info_path.open("rb") as handle:
        info = plistlib.load(handle)
    info.update(
        {
            "CFBundleDisplayName": "Elvandar Viewer",
            "CFBundleShortVersionString": project_version(),
            "CFBundleVersion": "1",
            "LSApplicationCategoryType": "public.app-category.productivity",
            "NSHighResolutionCapable": True,
            "NSHumanReadableCopyright": "Private Elvandar reading application",
        }
    )
    with info_path.open("wb") as handle:
        plistlib.dump(info, handle)

    run("codesign", "--force", "--deep", "--sign", "-", str(APP_BUNDLE))
    run("codesign", "--verify", "--deep", "--strict", str(APP_BUNDLE))


def main() -> int:
    if sys.platform != "darwin":
        raise SystemExit("The macOS application bundle can only be built on macOS")
    if not SOURCE_ICON.is_file():
        raise SystemExit(f"Missing icon source: {SOURCE_ICON}")
    BUILD_ROOT.mkdir(exist_ok=True)
    DIST_ROOT.mkdir(exist_ok=True)
    build_application()
    print(APP_BUNDLE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
