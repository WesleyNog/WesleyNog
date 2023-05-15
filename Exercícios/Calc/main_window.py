import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QApplication

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        self.setWindowTitle('Calculadora de WeS')

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
