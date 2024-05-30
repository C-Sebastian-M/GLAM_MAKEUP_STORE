from PyQt5 import uic

from PyQt5.QtWidgets import ( 
    QWidget, QGroupBox, 
    QLabel, QHBoxLayout,
    QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor, QPixmap

# Tipado
from typing import List, Union

class Plantilla(QWidget):
    def __init__(self, title: str, columns: List[str]) -> None:
        super().__init__()
        uic.loadUi(r"GUI\sub_ventanas\ui\reportes\plantillaDesigner.ui", self)

        self.titleLabel.setText(title)
        self.handle_labels(columns)
    
    def handle_labels(self, columns: List[Union[str, int]]) -> None:
        for nombre in columns:
            contenedor = QGroupBox()
            contenedor.setObjectName("filtroLabelContenedor")

            decoracion = QLabel(contenedor)
            decoracion.setPixmap(QPixmap(r"GUI\recursos\images\pink_circle.png"))
            decoracion.setMaximumSize(15, 15)
            decoracion.setScaledContents(True)

            label = QLabel(contenedor)
            label.setText(nombre)

            vbox_layout = QHBoxLayout(contenedor)
            vbox_layout.addWidget(decoracion)
            vbox_layout.addWidget(label)
            vbox_layout.addItem(QSpacerItem(5, 2, QSizePolicy.Minimum, QSizePolicy.Expanding))

            contenedor.setLayout(vbox_layout)

            self.labelsLayout.addWidget(contenedor)

        self.labelsLayout.addItem(QSpacerItem(2, 70, QSizePolicy.Minimum, QSizePolicy.Expanding))

class Ventas(Plantilla):
    def __init__(self, title: str, columns: List[str | int]) -> None:
        super().__init__(title, columns)

        self.inicializar()

    def inicializar(self):
        if hasattr(self, 'navbar'):
            self.navbar.deleteLater()

class Inventario(Plantilla):
    def __init__(self, title: str, columns: List[str | int]) -> None:
        super().__init__(title, columns)
        uic.loadUi(r"GUI\sub_ventanas\ui\reportes\inventarioPanelDesigner.ui", self)

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
