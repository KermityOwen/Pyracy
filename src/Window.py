from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys


def create_window(window_name: str):
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setGeometry(200, 200, 300, 300)
    window.setWindowTitle(window_name)

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    create_window("test")
