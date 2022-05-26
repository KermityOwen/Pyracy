import os
import sys

from PySide6.QtWidgets import *

APP = QApplication(sys.argv)
WINDOW_NAME = "Pyracy GUI Application"
SCREEN_RESOLUTION = {
    "x": APP.primaryScreen().size().width(),
    "y": APP.primaryScreen().size().height()
}
STYLES_PATH = os.path.abspath("gui/styles.css")
UI_PATH = os.path.abspath("gui/pyracy-main.ui")
STYLES = open(STYLES_PATH, "r").read()


class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI("PYRACY GUI")

    def initUI(self, window_name):
        self.setGeometry(0, 0, int(SCREEN_RESOLUTION["x"] / 2), int(SCREEN_RESOLUTION["y"] / 2))
        self.setWindowTitle(window_name)


win = Window()
win.show()
sys.exit(APP.exec())
