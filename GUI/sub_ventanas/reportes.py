import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QLabel, QGroupBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor, QPixmap

# Tipado
from typing import List

class Plantilla(QWidget):
    def __init__(self, title: str, columns: List[str]) -> None:
        super().__init__()
        uic.loadUi(r"GUI\sub_ventanas\ui\reportes\plantillaDesigner.ui", self)

        self.title = title
        self.columns = columns

        self.inicializar()

    def inicializar(self):
        self.titleLabel.setText(self.title)
        for column in self.columns:
            contenedor = QGroupBox()
            decoracion = QLabel(contenedor)
            decoracion.pixmap(QPixmap(r"GUI\recursos\images\pink_circle.jpg"))
            label = QLabel(contenedor, column)

            self.labelsLayout.addWidget(contenedor)

class Ventas(Plantilla):
    def __init__(self, title: str, columns: List[str | int]) -> None:
        super().__init__(title, columns)
        self.plantilla = Plantilla(title, columns)

        self.inicializar()

    def inicializar(self):
        self.navbar.deleteLater()

class Inventario(Plantilla):
    def __init__(self, title: str, columns: List[str | int]) -> None:
        super().__init__(title, columns)

class CBackground:
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing)

        brocha1 = QBrush(QColor(212, 132, 180), Qt.SolidPattern)
        brocha2 = QBrush(QColor(228, 156, 198), Qt.SolidPattern)
        brocha3 = QBrush(QColor(235, 188, 220), Qt.SolidPattern)

        # Dibujando circulos abajo
        painter.setBrush(brocha3)
        painter.drawEllipse(140, 530, 200, 200)

        painter.setBrush(brocha2)
        painter.drawEllipse(40, 480, 200, 200)

        painter.setBrush(brocha1)
        painter.drawEllipse(-70, 440, 200, 200)

        # Dibujando circulos arriba
        painter.setBrush(brocha3)
        painter.drawEllipse(440, -140, 200, 200)

        painter.setBrush(brocha2)
        painter.drawEllipse(550, -100, 200, 200)

        painter.setBrush(brocha1)
        painter.drawEllipse(700, -70, 200, 200)

        painter.end()

class InventarioPanel(QWidget, CBackground):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(r"GUI\sub_ventanas\ui\reportes\inventarioPanelDesigner.ui", self)

class ReportePanel(QWidget, CBackground):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"GUI\sub_ventanas\ui\reportes\reportesDesigner.ui", self)
