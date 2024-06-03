from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QMessageBox,QApplication
from PyQt5.QtCore import QPropertyAnimation, Qt
from PyQt5 import QtCore, QtWidgets, QtGui
from API.DATA import GestionDatos
from PyQt5.QtGui import QPainter, QBrush, QColor
from API.DATA import GestionDatos
<<<<<<< HEAD
=======
from API.prueba import Inventario
>>>>>>> 5d03a52ea2ceeb48405790eb660237d1e6d9b975

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

class InventarioProductos(QMainWindow, CBackground):
    def __init__(self):
        super(InventarioProductos, self).__init__()
        loadUi(
            r"GUI\sub_ventanas\ui\inventario_productos\inventario_productos.ui",
            self,
        )
<<<<<<< HEAD
<<<<<<< HEAD
        self.gestion_datos=GestionDatos()
=======
        self.gestion_datos = GestionDatos()
        
>>>>>>> main
        self.menu_boton.clicked.connect(self.mover_menu)

        self.add_boton.clicked.connect(self.add_productos)
        self.ver_actualizar_boton.clicked.connect(self.ver_productos)
=======
        self.inventario = Inventario()
        self.gestion_datos = GestionDatos()
        self.menu_boton.clicked.connect(self.mover_menu)
        self.add_boton.clicked.connect(self.add_productos)
        self.ver_actualizar_boton.clicked.connect(self.ver_productos)
        
>>>>>>> 5d03a52ea2ceeb48405790eb660237d1e6d9b975
        # Conexión botones barra lateral con páginas
        self.ver_productos_boton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.ver_productos_pagina)
        )
        self.ver_productos_boton.clicked.connect(self.limpiar_campos)
        self.nuevo_producto_boton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.nuevo_producto_pagina)
        )
        self.nuevo_producto_boton.clicked.connect(self.limpiar_campos)
        self.modificar_producto_boton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.modificar_producto_pagina)
        )
        self.modificar_producto_boton.clicked.connect(self.limpiar_campos)
        self.descontinuar_producto_boton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.descontinuar_producto_pagina)
        )
        self.descontinuar_producto_boton.clicked.connect(self.limpiar_campos)
        self.comprar_stock_boton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.comprar_stock_pagina)
        )
        self.comprar_stock_boton.clicked.connect(self.limpiar_campos)

        # Llamado métodos de validación en constructor
        self.setupValidatorsCodigoBarras()
        self.setupValidatorsPrecios()
        self.setupValidatorsUnidades()
        
    # Método para limpiar los campos cada que se cambiar de página
    def limpiar_campos(self):
        #Labels añadir_producto
        self.add_referencia_lineEdit.clear()
        self.add_marca_lineEdit.clear()
        self.add_precio_adquisicion_lineEdit.clear()
        self.add_precio_ventas_lineEdit.clear()
        self.add_unidades_actuales_lineEdit.clear()
    
    # Método para validar la longitud del código de barras
    def setupValidatorsCodigoBarras(self):
        validacion_referencia = QtGui.QRegularExpressionValidator(
            QtCore.QRegularExpression(r"\d{0,13}")
        )
        self.add_codigoBarras_lineEdit.setValidator(validacion_referencia)
    
    # Método para definir los precios
    def setupValidatorsPrecios(self):
        validacion_precios = QtGui.QRegularExpressionValidator(
            QtCore.QRegularExpression(r"\d{0,12}")
        )
        self.add_precio_adquisicion_lineEdit.setValidator(validacion_precios)
        self.add_precio_ventas_lineEdit.setValidator(validacion_precios)
    
    # Método para definir la cantidad de unidades (máximo 99.999)
    def setupValidatorsUnidades(self):
        validacion_unidades = QtGui.QRegularExpressionValidator(
            QtCore.QRegularExpression(r"\d{0,5}")
        )
        self.add_unidades_actuales_lineEdit.setValidator(validacion_unidades)
    
    # Método que permite mover la barra de menú
    def mover_menu(self):
        if True:
            width = self.frame_control.width()
            normal = 0
            if width == 0:
                extender = 270
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.frame_control, b"minimumWidth")
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(
                QtCore.QEasingCurve.InOutQuart
            )  # InQuad, InOutQuad, InCubic, InOutExpo
            self.animacion.start()
<<<<<<< HEAD

    def nuevo_producto_pagina(self):
        referencia = self.add_referencia_lineEdit.text()
        marca = self.add_marca_lineEdit.text()
        precio_a = self.add_precio_adquisicion_lineEdit.text()
        precio_v = self.add_precio_ventas_lineEdit.text()
        stock = self.add_unidades_actuales_lineEdit.text()
=======
    
    # Método para definir base de datos ...
    #self.tabla_ver_productos.setRowCount(0)

    def add_productos(self):
        referencia = self.add_referencia_lineEdit.text()
        marca =  self.add_marca_lineEdit.text()
        precio_adquisicion = self.add_precio_adquisicion_lineEdit.text()
        precio_venta =  self.add_precio_ventas_lineEdit.text()
        unidades_actuales = self.add_unidades_actuales_lineEdit.text()
<<<<<<< HEAD
        self.gestion_datos.agregar_producto(1,2,3,4,5,6)

    def ver_productos(self):
        self.tabla_ver_productos.setRowCount(0)
        for i, row in self.gestion_datos.clientes.iterrows():
            self.tabla_ver_productos.insertRow(i)
            for j, (colname, value) in enumerate(row.items()):
                self.tabla_ver_productos.setItem(i, j, QTableWidgetItem(str(value)))
=======
        codigo_barras = self.add_codigoBarras_lineEdit.text()
        self.inventario.crear_productos(referencia,codigo_barras, marca, precio_adquisicion, precio_venta, unidades_actuales)
    
<<<<<<< HEAD
    def ver_productos(self):
        self.tabla_ver_productos.setRowCount(0)
        for i, row in self.gestion_datos.productos.iterrows():
            self.tabla_ver_productos.insertRow(i)
            for j, (colname, value) in enumerate(row.items()):
                self.tabla_ver_productos.setItem(i, j, QTableWidgetItem(str(value)))
        
>>>>>>> 5d03a52ea2ceeb48405790eb660237d1e6d9b975
=======
    # VER PRODUCTOS PÁGINA
    # tabla_ver_productos (DATAFRAME)
    # ver_actualizar_boton
    
    # AÑADIR NUEVO PRODUCTO
    # add_referencia_lineEdit
    # add_codigo_barras_lineEdit
    # add_marca_lineEdit
    # add_precio_adquisicion_lineEdit
    # add_precio_venta_lineEdit
    # add_unidades_actuales_lineEdit
    
    # MODIFICAR PRODUCTO
    # modify_tabla_productos (DATAFRAME)
    # modify_buscar_producto_lineEdit (BARRA DE BUSQUEDA DEL DATAFRAME)
    # modify_buscar_boton (SELECCIONAR BOTÓN)
    # modify_marca_lineEdit
    # modify_precio_adquisicion_lineEdit
    # modify_precio_venta_lineEdit
    # modify_guardar_boton (BOTON PARA GUARDAR)
    
    # DESCONTINUAR PRODUCTO
    # del_tabla_productos (DATAFRAME)
    # del_buscar_producto_lineEdit (BARRA DE BUSQUEDA DEL DATAFRAME)
    # del_guardar_boton (BOTON PARA GUARDAR)
    
    # COMPRAR STOCK
    # buy_tabla_productos (DATAFRAME)
    # buy_buscar_producto_lineEdit (BARRA DE BUSQUEDA DEL DATAFRAME)
    # buy_buscar_boton (BOTON SELECCIONAR)
    # buy_cantidad_ingresar_lineEdit (BOTON PARA INGRESAR UNIDADES)
    # buy_add_boton (BOTON PARA AÑADIR)
>>>>>>> 5b993dea764534de7c7f9bb78fa73890379c23b7
>>>>>>> main
