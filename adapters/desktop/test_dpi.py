from PyQt6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)

screen = app.primaryScreen()

print("DPI:", screen.logicalDotsPerInch())
print("Scale:", screen.devicePixelRatio())

sys.exit()