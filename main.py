"""Точка входа: python main.py"""
import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

from reader.app import MainWindow
from reader.config import APP_NAME


def main() -> int:
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    window = MainWindow(Path(__file__).parent / "content")
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
