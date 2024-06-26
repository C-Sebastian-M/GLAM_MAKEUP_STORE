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
validacion = CustomValidaciones()

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
        if not self.fecha or len(self.fecha) == 1:
            validacion.caja_input_no_valido("Asegurese de poner ambas fechas.")
            return None
        
        fechas_compuesta = f"{self.fecha['desde']} - {self.fecha['hasta']}"
        fechas_validas = validacion.validar_fechas(fechas_compuesta)

        if not fechas_validas:
            validacion.caja_input_no_valido("Fechas ingresadas no validas, recuerde que la primera fecha (desde)\ndebe ser menor que la segunda(hasta).")
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

        table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        table.setHorizontalScrollMode(QTableWidget.ScrollPerPixel)
        # logica para implementar los registros de la tabla

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
        user_input: str = self.userInput.text().strip()
        if not user_input:
            validacion.caja_input_no_valido("Ingresastes una consulta vacia")
            return None

        if eleccion == "referencia":
            if user_input in self.gestion_datos.productos["Referencia"].values:
                self.reportes.filtrar_referencia(user_input)
                self.mostrar_referencia()
            else:
                validacion.caja_input_no_valido("Referencia ingresada no valida")
        elif eleccion == "codigo_de_barras":
            if user_input in self.gestion_datos.productos["Codigo de barras"].values:
                self.reportes.filtrar_codigo_de_barras(user_input)
                self.mostrar_referencia()
            elif int(user_input) in self.gestion_datos.productos["Codigo de barras"].values:
                user_input = int(user_input)
                self.reportes.filtrar_codigo_de_barras(user_input)
                self.mostrar_referencia()
            else:
                validacion.caja_input_no_valido("El codigo de barras ingresado no es valido")
        elif eleccion == "marca":
            if user_input in self.gestion_datos.productos["Marca"].values:
                self.reportes.filtrar_marca(user_input)
                self.mostrar_referencia()    
            else:
                validacion.caja_input_no_valido("La marca ingresada no es valida")
        elif eleccion == "precio_de_adquisicion":
            if user_input in self.gestion_datos.productos["Precio de adquisicion"].values:
                self.reportes.filtrar_precioA(user_input)
                self.mostrar_referencia()
            elif int(user_input) in self.gestion_datos.productos["Precio de adquisicion"].values:
                user_input = int(user_input)
                self.reportes.filtrar_precioA(user_input)
                self.mostrar_referencia()
            else:
                validacion.caja_input_no_valido("El precio de adquisicion no es valido")
        elif eleccion == "precio_venta":
            if user_input in self.gestion_datos.productos["Precio venta"].values:
                self.reportes.filtrar_precioV(user_input)
                self.mostrar_referencia()
            elif int(user_input) in self.gestion_datos.productos["Precio venta"].values:
                user_input = int(user_input)
                self.reportes.filtrar_precioV(user_input)
                self.mostrar_referencia()
            else:
                validacion.caja_input_no_valido("El precio de venta ingresado no es valido")
        elif eleccion == "unidades_actuales":
            if user_input in self.gestion_datos.productos["Unidades actuales"].values:
                self.reportes.filtrar_stock(user_input)
                self.mostrar_referencia()
            elif int(user_input) in self.gestion_datos.productos["Unidades actuales"].values:
                user_input = int(user_input)
                self.reportes.filtrar_stock(user_input)
                self.mostrar_referencia()
            else:
                validacion.caja_input_no_valido("Las unidades que ingresastes no son validas")
        elif eleccion == "producto_disponible":
            if user_input in self.gestion_datos.productos["Producto disponible"].values:
                self.reportes.filtrar_disponibilidad(user_input)
                self.mostrar_referencia()
            elif int(user_input) in self.gestion_datos.productos["Producto disponible"].values:
                user_input = int(user_input)
                self.reportes.filtrar_disponibilidad(user_input)
                self.mostrar_referencia()
            else:
                validacion.caja_input_no_valido("Input no valido")
        elif eleccion ==  "id_servicio":
            if user_input in self.gestion_datos.servicios["ID servicio"].values:
                self.reportes.filtrar_ID_Servicio(user_input)
                self.mostrar_servicios()
            elif int(user_input) in self.gestion_datos.servicios["ID servicio"].values:
                user_input = int(user_input)
                self.reportes.filtrar_ID_Servicio(user_input)
                self.mostrar_servicios()
            else:
                validacion.caja_input_no_valido("referencia de servicio no valida")
        elif eleccion == "nombre_servicio":
            if user_input in self.gestion_datos.servicios["Nombre Servicio"].values:
                self.reportes.filtrar_servicio(user_input)
                self.mostrar_servicios()
            else:
                validacion.caja_input_no_valido("Nombre de servicio no valido")
        elif eleccion == "costo":
            if user_input in self.gestion_datos.servicios["Costo"].values:
                self.reportes.filtrar_costo(user_input)
                self.mostrar_servicios()
            elif int(user_input) in self.gestion_datos.servicios["Costo"].values:
                user_input = int(user_input)
                self.reportes.filtrar_costo(user_input)
                self.mostrar_servicios()
        elif eleccion == "fecha":
            fechas = self.findChild(QLabel, "rangoDeFechasLabel").text()
            self.reportes.filtrar_fecha(fechas)
            self.mostrar_servicios()
        else:
            validacion.caja_input_no_valido("Input no valido")

    def mostrar_referencia(self):
        table: QTableWidget = self.tablaReportes
        table.setRowCount(0)
        for i, row in self.reportes.filtrado_productos.iterrows():
            table.insertRow(i)
            for j, (_, value) in enumerate(row.items()):
                table.setItem(i, j, QTableWidgetItem(str(value)))
    
    def mostrar_servicios(self):
        table: QTableWidget = self.tablaReportes
        table.setRowCount(0)
        for i, row in self.reportes.filtrado_servicios.iterrows():
            table.insertRow(i)
            for j, (_, value) in enumerate(row.items()):
                table.setItem(i, j, QTableWidgetItem(str(value)))

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
    def __init__(self, title: str, columns: List[str | int], ref: int) -> None:
        super().__init__(title, columns)
        if ref == 1:
            self.fechaBtn.hide()
        
class ReportePanel(QWidget, CBackground):
    def __init__(self):
        super().__init__()
        uic.loadUi(
            r"GUI\sub_ventanas\ui\reportes\reportesDesigner.ui",
            self,
        )
