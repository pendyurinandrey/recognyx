"""Запуск графического интерфейса: команда `recognyx` или `python -m recognyx`
(из активированного .venv или через `uv run`)."""

import sys

from PySide6.QtWidgets import QApplication

from recognyx.ui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
