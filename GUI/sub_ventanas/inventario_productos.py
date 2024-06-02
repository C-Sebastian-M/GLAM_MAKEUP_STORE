from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets, QtGui
from API.DATA import GestionDatos

class InventarioProductos(QMainWindow):
    def __init__(self):
        super(InventarioProductos, self).__init__()
        loadUi(
            r"GUI\sub_ventanas\ui\inventario_productos\inventario_productos.ui",
            self,
        )
        self.gestion_datos = GestionDatos()
        
        self.menu_boton.clicked.connect(self.mover_menu)
        
        # Conexión botones barra lateral con páginas
        self.ver_productos_boton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.ver_productos_pagina)
        )
        self.nuevo_producto_boton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.nuevo_producto_pagina)
        )
        self.modificar_producto_boton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.modificar_producto_pagina)
        )
        self.descontinuar_producto_boton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.descontinuar_producto_pagina)
        )
        self.comprar_stock_boton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.comprar_stock_pagina)
        )
        
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
            
    def ver_productos_pagina(self):
        self.tabla_verProductos.setRowCount(0)
        for i, row in self.gestion_datos.productos.iterrows():
            self.tabla_verProductos.insertRow(i)
            for j, (colname, value) in enumerate(row.items()):
                self.tabla_verProductos.setItem(i, j, QTableWidgetItem(str(value)))
                