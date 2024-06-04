import datetime

from PyQt5 import uic

from PyQt5.QtWidgets import ( 
    QWidget, QLabel, 
    QHBoxLayout, QSpacerItem, 
    QSizePolicy, QTableWidget,
    QHeaderView, QGraphicsDropShadowEffect, 
    QTableWidgetItem
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (
    QColor, QPixmap, 
    QCursor, QIcon
)
from GUI.sub_ventanas.custom.utils.css import CustomGroupBox, CBackground
import API.DATA as GD
from GUI.sub_ventanas.custom.validaciones import CustomValidaciones
# Tipado
from typing import List, Union, Dict
from API.prueba import Reportes

GD = GD.GestionDatos()
vald = CustomValidaciones()

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
        fecha_seleccionada: str = self.calendarioPorFecha.selectedDate().toPyDate()
        if comboFocus.strip().lower() == "desde":
            self.fecha["desde"] = fecha_seleccionada
            self.desdeLabel.setText(f'Desde\n{fecha_seleccionada}')
            return None

        self.fecha["hasta"] = fecha_seleccionada
        self.hastaLabel.setText(f'Hasta\n{fecha_seleccionada}')

    def confirmar(self) -> None:
        if not self.fecha:
            return
        
        fechas_compuesta = f"{self.fecha['desde']} - {self.fecha['hasta']}"
        fechas_validas = vald.validar_fechas(fechas_compuesta)

        if not fechas_validas:
            vald.caja_input_no_valido("""
                Fechas ingresadas no validas,\n 
                recuerde que la primera fecha (desde)\n
                debe ser menor que la segunda(hasta).
            """)
            return None

        self.ref.setText(fechas_compuesta)
        self.close()

    def pintar(self) -> None:
        with open(r"GUI\sub_ventanas\css\byDate.css", "r") as style_file:
            style_line = style_file.read()

        self.setStyleSheet(style_line)
        style_file.close()

class Plantilla(QWidget):
    def __init__(self, title: str, columns: List[str]) -> None:
        super().__init__()
        uic.loadUi(
            r"GUI\sub_ventanas\ui\reportes\plantillaDesigner.ui", 
            self
        )

        self.campos: List[Union[str, int, float]] = columns
        self.BD_DATA = {}

        self.titleLabel.setText(title)
        self.handle_table(data=self.BD_DATA)
        self.handle_labels()

        self.fechaBtn.clicked.connect(self.abrir_ventana_por_fecha)
        self.filtrarBtn.clicked.connect(self.filtrar)
        self.filtrarBtn.clicked.connect(self.mostrar_referencia)

        self.pintar()
        self.reportes = Reportes()
        self.gestion_datos = GD
    def handle_labels(self) -> None:
        for campo in self.campos:
            if campo.strip().lower() == 'fecha':
                continue

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
            label.setText(campo)
            contenedor.label = label

            vbox_layout = QHBoxLayout(contenedor)
            vbox_layout.addWidget(decoracion)
            vbox_layout.addWidget(label)

            contenedor.setLayout(vbox_layout)

            self.labelsLayout.addWidget(contenedor)

        self.labelsLayout.addItem(QSpacerItem(2, 70, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def handle_table(self, data: Dict[str, Union[int, str]]) -> None:
        table: QTableWidget = self.tablaReportes
        table.setColumnCount(len(self.campos))
        table.setHorizontalHeaderLabels(self.campos)
        table.resizeColumnsToContents()
        table.verticalHeader().setDefaultSectionSize(20)

        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(8)
        shadow_effect.setColor(QColor(0, 0, 0, 70))
        shadow_effect.setOffset(0, 0)
        header.setGraphicsEffect(shadow_effect)

        table.setHorizontalScrollMode(QTableWidget.ScrollPerPixel)
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

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

    def filtrar(self):
        eleccion: str = self.normalizar(self.consultandoPor.text())
        user_input: str = self.userInput.text()
        if eleccion == "referencia":
            if user_input in self.gestion_datos.productos["Referencia"].values:
                self.reportes.filtrar_referencia(user_input)
                self.mostrar_referencia()
        print(eleccion,user_input)
                    
        campos = [campo.lower() for campo in self.campos]
    
    def mostrar_referencia(self):
        self.tablaReportes.setRowCount(0)
        for i, row in self.reportes.filtrado_productos.iterrows():
            self.tablaReportes.insertRow(i)
            for j, (colname, value) in enumerate(row.items()):
                self.tablaReportes.setItem(i, j, QTableWidgetItem(str(value)))

        

        def caja_input_no_valido():
            pass # mostrar caja

        CONRTOLADOR_DE_FILTRADO = {} # funciones para hacer query

        # return CONRTOLADOR_DE_FILTRADO[eleccion] comentado para evitar error

    def normalizar(self, cadena: str):
        cadena = cadena.strip().lower().replace(" ", "_")
        return cadena
    
    def pintar(self) -> None:
        with open(r"GUI\sub_ventanas\css\reportes_plantilla.css", "r") as style_file:
            style_line = style_file.read()

        self.setStyleSheet(style_line)
        style_file.close()



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

class ReportePanel(QWidget, CBackground):
    def __init__(self):
        super().__init__()
        uic.loadUi(
            r"GUI\sub_ventanas\ui\reportes\reportesDesigner.ui",
            self,
        )
