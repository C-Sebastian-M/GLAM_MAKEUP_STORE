from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QMessageBox,QApplication
from PyQt5.QtCore import QPropertyAnimation, Qt
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPainter, QBrush, QColor

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
        
        self.menu_boton.clicked.connect(self.mover_menu)
        
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
        self.add_referencia_lineEdit.setValidator(validacion_referencia)
    
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
    
    # Método para definir base de datos ...
    #self.tabla_ver_productos.setRowCount(0)