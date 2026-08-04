from __future__ import annotations

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QKeySequence, QMouseEvent, QPainter, QPixmap, QShortcut, QWheelEvent
from PySide6.QtWidgets import (
    QDialog,
    QFrame,
    QGraphicsPixmapItem,
    QGraphicsScene,
    QGraphicsView,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class ImageCanvas(QGraphicsView):
    def __init__(self, image: QImage) -> None:
        super().__init__()
        self._scene = QGraphicsScene(self)
        self._pixmap_item = QGraphicsPixmapItem(QPixmap.fromImage(image))
        self._scene.addItem(self._pixmap_item)
        self.setScene(self._scene)
        self.setSceneRect(self._pixmap_item.boundingRect())
        self.setRenderHints(QPainter.RenderHint.Antialiasing | QPainter.RenderHint.SmoothPixmapTransform)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorViewCenter)
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setBackgroundBrush(Qt.GlobalColor.transparent)
        self._scale = 1.0

    def fit_image(self) -> None:
        self.resetTransform()
        self.fitInView(self._pixmap_item, Qt.AspectRatioMode.KeepAspectRatio)
        self._scale = self.transform().m11()

    def actual_size(self) -> None:
        self.resetTransform()
        self._scale = 1.0
        self.centerOn(self._pixmap_item)

    def zoom_in(self) -> None:
        self._zoom(1.2)

    def zoom_out(self) -> None:
        self._zoom(1 / 1.2)

    def wheelEvent(self, event: QWheelEvent) -> None:  # noqa: N802 - Qt API
        self._zoom(1.18 if event.angleDelta().y() > 0 else 1 / 1.18)
        event.accept()

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:  # noqa: N802 - Qt API
        if abs(self._scale - 1.0) < 0.05:
            self.fit_image()
        else:
            self.actual_size()
        event.accept()

    def _zoom(self, factor: float) -> None:
        target = self._scale * factor
        if not 0.04 <= target <= 24:
            return
        self.scale(factor, factor)
        self._scale = target


class ImageViewerDialog(QDialog):
    def __init__(self, data: bytes, name: str, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        image = QImage.fromData(data)
        if image.isNull():
            raise ValueError(f"Could not decode image: {name}")

        self.setWindowTitle(f"{name} — Elvandar Viewer")
        self.resize(1100, 780)
        self.setMinimumSize(620, 440)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        toolbar = QFrame(objectName="imageToolbar")
        tools = QHBoxLayout(toolbar)
        tools.setContentsMargins(16, 10, 14, 10)
        tools.setSpacing(7)
        title = QLabel(name, objectName="imageTitle")
        title.setToolTip(name)
        tools.addWidget(title, 1)
        tools.addWidget(QLabel(f"{image.width():,} × {image.height():,} px", objectName="imageInfo"))

        self.canvas = ImageCanvas(image)
        for label, callback in (
            ("−", self.canvas.zoom_out),
            ("Fit", self.canvas.fit_image),
            ("100%", self.canvas.actual_size),
            ("+", self.canvas.zoom_in),
        ):
            button = QPushButton(label, objectName="imageToolButton")
            button.clicked.connect(callback)
            tools.addWidget(button)

        layout.addWidget(toolbar)
        layout.addWidget(self.canvas, 1)
        self.setStyleSheet(
            """
            QDialog { background: #181A1F; }
            QFrame#imageToolbar { background: #23262D; border-bottom: 1px solid #363A43; }
            QLabel#imageTitle { color: #E8EAF0; font-size: 13px; font-weight: 600; }
            QLabel#imageInfo { color: #9299A6; font-size: 11px; padding-right: 8px; }
            QPushButton#imageToolButton { color: #D9DCE3; background: #30343C; border: 1px solid #414651;
                border-radius: 5px; padding: 5px 10px; min-width: 28px; }
            QPushButton#imageToolButton:hover { background: #3A3F49; }
            QGraphicsView { background: #181A1F; }
            """
        )

        self._shortcuts: list[QShortcut] = []
        for sequence, callback in (
            ("+", self.canvas.zoom_in),
            ("-", self.canvas.zoom_out),
            ("0", self.canvas.actual_size),
            ("F", self.canvas.fit_image),
        ):
            shortcut = QShortcut(QKeySequence(sequence), self)
            shortcut.activated.connect(callback)
            self._shortcuts.append(shortcut)
        QTimer.singleShot(0, self.canvas.fit_image)
