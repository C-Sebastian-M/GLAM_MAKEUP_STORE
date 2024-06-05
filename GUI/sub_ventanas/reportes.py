import datetime
from PyQt5 import uic
from PyQt5.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy, QTableWidget,
    QHeaderView, QGraphicsDropShadowEffect, QTableWidgetItem, QLineEdit, QComboBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (
    QPainter, QBrush, QColor, QPixmap, QCursor, QIcon
)
from GUI.sub_ventanas.utils.css import CustomGroupBox, CBackground
import API.DATA as GD
from API.Validaciones import (
    validacion_Referencia, validacion_Codigo_Barras, validacion_Stock
)
from API.prueba import Reportes
from GUI.sub_ventanas.custom.validaciones import CustomValidaciones

# Tipado
from typing import List, Union, Dict

RP = Reportes()
GD = GD.GestionDatos()
vald = CustomValidaciones()

class ReportePorFecha(QWidget):
    def __init__(self, ref) -> None:
        super().__init__()
        uic.loadUi(r"GUI\sub_ventanas\ui\reportes\reportePorFecha.ui", self)
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
        uic.loadUi(r"GUI\sub_ventanas\ui\reportes\plantillaDesigner.ui", self)

        self.campos: List[Union[str, int, float]] = columns
        self.BD_DATA = {}

        self.titleLabel.setText(title)
        self.handle_table(data=self.BD_DATA)
        self.handle_labels()

        self.fechaBtn.clicked.connect(self.abrir_ventana_por_fecha)
        self.filtrarBtn.clicked.connect(self.filtrar)

        self.pintar()

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
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

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
<<<<<<< HEAD
        eleccion: str = self.consultandoPor.currentText().strip().lower()
        user_input: str = self.userInput.text()

        if eleccion == "productos":
            productos_filtrados = self.filtrar_productos(user_input)
            self.actualizar_tabla(productos_filtrados)
        elif eleccion == "servicios":
            servicios_filtrados = self.filtrar_servicios(user_input)
            self.actualizar_tabla(servicios_filtrados)
        elif eleccion == "ventas":
            ventas_filtradas = self.filtrar_ventas(user_input)
            self.actualizar_tabla(ventas_filtradas)
        else:
            print("Error: Opción de filtrado no válida.")
=======
        eleccion: str = self.normalizar(self.consultandoPor.text())
        campos = [campo.lower() for campo in self.campos]
        user_input: str = self.userInput.text()

        print(eleccion, user_input)

        def caja_input_no_valido():
            pass # mostrar caja
>>>>>>> f10651b2ad0734a1918bc2c1b88ec02be087dd71

    def filtrar_productos(self):
        referencia = self.filtroReferencia.text() if self.filtroReferencia.text() else None
        codigo_barras = self.filtroCodigoBarras.text() if self.filtroCodigoBarras.text() else None
        marca = self.filtroMarca.text() if self.filtroMarca.text() else None
        precio_adquisicion = float(self.filtroPrecioAdquisicion.text()) if self.filtroPrecioAdquisicion.text() else None
        stock = int(self.filtroStock.text()) if self.filtroStock.text() else None
        precio_venta = float(self.filtroPrecioVenta.text()) if self.filtroPrecioVenta.text() else None
        comparacion_precio_venta = self.filtroComparacionPrecioVenta.currentText() if self.filtroComparacionPrecioVenta.currentText() else None
        fecha_min = self.fechas_label.text().split(' - ')[0] if self.fechas_label else None
        fecha_max = self.fechas_label.text().split(' - ')[1] if self.fechas_label else None

        return RP.filtrar_productos(referencia, codigo_barras, marca, precio_adquisicion, stock, precio_venta, comparacion_precio_venta, fecha_min, fecha_max)
    def filtrar_servicios(self):
        nombre = self.filtroNombre.text() if self.filtroNombre.text() else None
        id_servicio = self.filtroIdServicio.text() if self.filtroIdServicio.text() else None
        precio = float(self.filtroPrecio.text()) if self.filtroPrecio.text() else None
        comparacion_precio = self.filtroComparacionPrecio.currentText() if self.filtroComparacionPrecio.currentText() else None
        fecha_min = self.fechas_label.text().split(' - ')[0] if self.fechas_label else None
        fecha_max = self.fechas_label.text().split(' - ')[1] if self.fechas_label else None

        return RP.filtrar_servicios(nombre, id_servicio, precio, comparacion_precio, fecha_min, fecha_max)

    def filtrar_ventas(self):
        id_venta = self.filtroIdVenta.text() if self.filtroIdVenta.text() else None
        cantidad = int(self.filtroCantidad.text()) if self.filtroCantidad.text() else None
        cliente = self.filtroCliente.text() if self.filtroCliente.text() else None
        subtotal = float(self.filtroSubtotal.text()) if self.filtroSubtotal.text() else None
        comparacion_subtotal = self.filtroComparacionSubtotal.currentText() if self.filtroComparacionSubtotal.currentText() else None
        producto_o_servicio = self.filtroProductoOServicio.currentText() if self.filtroProductoOServicio.currentText() else None
        fecha_min = self.fechas_label.text().split(' - ')[0] if self.fechas_label else None
        fecha_max = self.fechas_label.text().split(' - ')[1] if self.fechas_label else None
        id_caja = self.filtroIdCaja.text() if self.filtroIdCaja.text() else None

        return RP.filtrar_ventas(id_venta, cantidad, cliente, subtotal, comparacion_subtotal, producto_o_servicio, fecha_min, fecha_max, id_caja)
    def actualizar_tabla(self, data):
        table: QTableWidget = self.tablaReportes
        table.setRowCount(len(data))
        table.setColumnCount(len(self.campos))
        table.setHorizontalHeaderLabels(self.campos)

        for row_idx, row_data in enumerate(data.iterrows()):
            for col_idx, col in enumerate(self.campos):
                item = QTableWidgetItem(str(row_data[1][col]))
                table.setItem(row_idx, col_idx, item)

        table.resizeColumnsToContents()

<<<<<<< HEAD
=======
        # return CONRTOLADOR_DE_FILTRADO[eleccion] comentado para evitar error

    def normalizar(self, cadena: str):
        cadena = cadena.strip().lower().replace(" ", "_")
        return cadena
    
>>>>>>> f10651b2ad0734a1918bc2c1b88ec02be087dd71
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