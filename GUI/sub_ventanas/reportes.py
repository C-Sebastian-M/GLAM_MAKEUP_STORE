import datetime

from PyQt5 import uic

from PyQt5.QtWidgets import ( 
    QWidget, QLabel, 
    QHBoxLayout, QSpacerItem, 
    QSizePolicy, QMainWindow
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (
    QPainter, QBrush,
    QColor, QPixmap, 
    QCursor, QIcon, 
    QPainterPath, QRegion
)
from GUI.sub_ventanas.utils.css import CustomGroupBox

# Tipado
from typing import List, Union, Dict

class ReportePorFecha(QWidget):
    def __init__(self, ref) -> None:
        super().__init__()
        uic.loadUi(
            r"GUI\sub_ventanas\ui\reportes\reportePorFecha.ui", 
            self
        )
        self.ref = ref
        self.fecha = {}

        self.setFixedSize(400, 335)
        self.setWindowIcon(QIcon(r"GUI\recursos\images\icono.ico"))

        self.setBtn.clicked.connect(self.combo_event)
        self.cancelarBtn.clicked.connect(self.close)
        self.confirmarBtn.clicked.connect(self.confirmar)

        self.pintar()

    def combo_event(self) -> None:
        comboFocus: str = self.des_hasComboBox.currentText()
        fecha_seleccionada: str = self.calendarPorFecha.selectedDate().toPyDate()
        if comboFocus.strip().lower() == "desde":
            self.fecha["desde"] = fecha_seleccionada
            self.desdeLabel.setText(f'Desde\n{fecha_seleccionada}')
            return None

        self.fecha["hasta"] = fecha_seleccionada
        self.hastaLabel.setText(f'Hasta\n{fecha_seleccionada}')

    def confirmar(self) -> None:
        if not self.fecha:
            return

        if self.fecha['hasta'] < self.fecha['desde']:
            # Fecha no valida.
            return

        self.ref.setText(f"{self.fecha['desde']} - {self.fecha['hasta']}")
        self.close()

    def pintar(self) -> None:
        with open(r"GUI\sub_ventanas\css\byDate.css", "r") as style_file:
            style_line = style_file.read()

        self.setStyleSheet(style_line)
        style_file.close()

        # path = QPainterPath()
        # path.moveTo(0, 0)
        # path.lineTo(self.width(), 0)
        # path.lineTo(self.width(), self.height() - 20)
        # path.quadTo(self.width(), self.height(), self.width() - 20, self.height())
        # path.lineTo(20, self.height())
        # path.quadTo(0, self.height(), 0, self.height() - 20)
        # path.lineTo(0, 0) 

        # region = QRegion(path.toFillPolygon().toPolygon())
        # self.setMask(region)

class Plantilla(QWidget):
    def __init__(self, title: str, columns: List[str]) -> None:
        super().__init__()
        uic.loadUi(
            r"GUI\sub_ventanas\ui\reportes\plantillaDesigner.ui", 
            self
        )

        self.titleLabel.setText(title)
        self.handle_labels(columns)

        self.fechaBtn.clicked.connect(self.abrir_ventana_por_fecha)

    def handle_labels(self, columns: List[Union[str, int]]) -> None:
        for nombre in columns:
            contenedor = CustomGroupBox(self)
            contenedor.setObjectName("contenedorColumnas")
            contenedor.setCursor(QCursor(Qt.PointingHandCursor))
            contenedor.setContentsMargins(10, 0, 10, 0)

            decoracion = QLabel(contenedor)
            decoracion.setPixmap(QPixmap(r"GUI\recursos\images\pink_circle.png"))
            decoracion.setMaximumSize(15, 13)
            decoracion.setScaledContents(True)

            label = QLabel(contenedor)
            label.setObjectName("campo")
            label.setText(nombre)
            contenedor.label = label

            vbox_layout = QHBoxLayout(contenedor)
            vbox_layout.addWidget(decoracion)
            vbox_layout.addWidget(label)

            contenedor.setLayout(vbox_layout)

            self.labelsLayout.addWidget(contenedor)

        self.labelsLayout.addItem(QSpacerItem(2, 70, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def handle_table(self, fields: List[str], data: Dict[str, Union[int, str]]) -> None:
        pass

    def abrir_ventana_por_fecha(self) -> None:
        self.consultandoPor.setText("fecha")
        fecha_actual = datetime.date.today()

        self.fechas_label = self.findChild(QLabel, "rangoDeFechasLabel")
        if not self.fechas_label:
            self.fechas_label = QLabel()
            self.fechas_label.setObjectName("rangoDeFechasLabel")
            self.fechas_label.setText(f"{fecha_actual} - {fecha_actual}")
            self.cajaFiltroVerticalLayout.insertWidget(5, self.fechas_label)

        self.consulta_por_fecha = ReportePorFecha(ref=self.fechas_label)
        self.consulta_por_fecha.show()

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

class CBackground:
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing)

        brocha1 = QBrush(QColor(212, 132, 180), Qt.SolidPattern)
        brocha2 = QBrush(QColor(228, 156, 198), Qt.SolidPattern)
        brocha3 = QBrush(QColor(235, 188, 220), Qt.SolidPattern)

        # Obtén el tamaño actual de la ventana
        width = self.width()
        height = self.height()

        # Calcula las posiciones y tamaños en función del tamaño de la ventana
        diameter = width // 4
        offset_x = width // 8
        offset_y = height // 5

        # Dibujando círculos abajo
        painter.setBrush(brocha3)
        painter.drawEllipse(int(width // 2 - diameter // 2), int(height - offset_y), int(diameter), int(diameter))

        painter.setBrush(brocha2)
        painter.drawEllipse(int(width // 4 - diameter // 2), int(height - offset_y * 1.5), int(diameter), int(diameter))

        painter.setBrush(brocha1)
        painter.drawEllipse(int(width // 8 - diameter // 2), int(height - offset_y * 2), int(diameter), int(diameter))

        # Dibujando círculos arriba
        painter.setBrush(brocha3)
        painter.drawEllipse(int(width // 2 - diameter // 2), int(-offset_y), int(diameter), int(diameter))

        painter.setBrush(brocha2)
        painter.drawEllipse(int(width // 2 + offset_x), int(-offset_y // 2), int(diameter), int(diameter))

        painter.setBrush(brocha1)
        painter.drawEllipse(int(width // 2 + offset_x * 2), int(0), int(diameter), int(diameter))

        painter.end()

class ReportePanel(QWidget, CBackground):
    def __init__(self):
        super().__init__()
        uic.loadUi(
            r"GUI\sub_ventanas\ui\reportes\reportesDesigner.ui",
            self,
        )
