from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import Qt
import sys


class Overlay(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )

        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

        self.setGeometry(
            0,
            0,
            1920,
            1080
        )

    def paintEvent(self, event):

        painter = QPainter(self)

        pen = QPen()

        pen.setWidth(4)

        painter.setPen(pen)

        painter.drawRect(
            21,
            281,
            349,
            45
        )


app = QApplication(sys.argv)

overlay = Overlay()

overlay.show()

sys.exit(app.exec())