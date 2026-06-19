from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import Qt
import uiautomation as auto
import sys


class Overlay(QWidget):

    def __init__(self):

        super().__init__()

        self.rect_data = self.find_bluetooth()

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )

        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

        screen = QApplication.primaryScreen()

        geometry = screen.geometry()

        self.setGeometry(
            geometry.x(),
            geometry.y(),
            geometry.width(),
            geometry.height()
        )

    def find_bluetooth(self):

        settings = auto.WindowControl(
            searchDepth=1,
            Name="Settings"
        )

        if not settings.Exists(3):
            return None

        for control, depth in auto.WalkControl(
            settings,
            maxDepth=20
        ):

            try:

                if (
                    control.Name ==
                    "Bluetooth & devices"
                    and
                    control.ControlTypeName ==
                    "ListItemControl"
                ):

                    rect = control.BoundingRectangle

                    return (
                        rect.left,
                        rect.top,
                        rect.right - rect.left,
                        rect.bottom - rect.top
                    )

            except:
                pass

        return None

    def paintEvent(self, event):

        if not self.rect_data:
            return

        painter = QPainter(self)

        pen = QPen()

        pen.setWidth(4)

        painter.setPen(pen)

        x, y, w, h = self.rect_data

        y = int(y * 0.75)
        painter.drawRect(
            x,
            y,
            w,
            h
        )


app = QApplication(sys.argv)

overlay = Overlay()

overlay.show()

sys.exit(app.exec())