import pandas as pd
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import (
    QMainWindow,
    QHeaderView,
    QTableWidgetItem,
    QCompleter,
    QMessageBox,
    QTableWidget
)
from PyQt5.QtCore import QPropertyAnimation, Qt, QStringListModel
from PyQt5 import QtCore, QtGui
from API.DATA import GestionDatos
from API.prueba import Inventario
from API.Validaciones import *
from GUI.sub_ventanas.custom.utils.css import CBackground


class InventarioProductos(QMainWindow, CBackground):
    def __init__(self):
        super(InventarioProductos, self).__init__()
        loadUi(
            r"GUI\sub_ventanas\ui\inventario_productos\inventario_productos.ui",
            self,
        )
        self.menu_boton.clicked.connect(self.mover_menu)
        self.add_boton.clicked.connect(self.add_productos)
        self.ver_actualizar_boton.clicked.connect(self.ver_productos)
        self.pushButton_verStock.clicked.connect(self.ver_productosComprar)
        self.pushButton_verModificar.clicked.connect(self.ver_productosModificar)
        self.pushButton_verEliminar.clicked.connect(self.ver_productosEliminar)
        self.modify_buscar_boton.clicked.connect(self.mostrar_formulario)
        self.modify_guardar_boton.clicked.connect(self.modificar_productos)
        self.buy_buscar_boton.clicked.connect(self.mostrar_formulario2)
        self.buy_add_boton.clicked.connect(self.comprar_stock)
        self.del_guardar_boton.clicked.connect(self.descontinuar_producto)
        self.inventario = Inventario()
        self.gestion_datos = GestionDatos()
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
            lambda: self.stackedWidget.setCurrentWidget(
                self.descontinuar_producto_pagina
            )
        )
        self.descontinuar_producto_boton.clicked.connect(self.limpiar_campos)
        self.comprar_stock_boton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.comprar_stock_pagina)
        )
        self.comprar_stock_boton.clicked.connect(self.limpiar_campos)

        # Ancho columna adaptable
        self.tabla_ver_productos.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.tableWidget_modificar.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.del_tabla_productos.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.tableWidget_comprarStock.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        # Llamado métodos de validación en constructor
        self.setupValidatorsCodigoBarras()
        self.setupValidatorsPrecios()
        self.setupValidatorsUnidades()
        self.frame_formularioModificar.hide()
        self.frame_formulario_comprar_stock.hide()
        self.df = pd.read_excel("registros.xlsx", sheet_name="Productos")
        self.productos = self.df["Codigo de barras"].astype(str).tolist()
        self.modelo_datos = QStringListModel(self.productos)
        self.completer = QCompleter(self.modelo_datos, self)
        self.completer.setCaseSensitivity(False)  # Ignorar mayúsculas y minúsculas
        self.completer.setFilterMode(
            Qt.MatchContains
        )  # Coincidir con cualquier parte del texto
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.completer.setPopup(self.listView_comprarStock)
        self.completer.setPopup(self.listView_modificar)
        self.completer.setPopup(self.listView_eliminar)
        self.modify_buscar_producto_lineEdit.setCompleter(self.completer)
        self.del_buscar_producto_lineEdit.setCompleter(self.completer)
        self.buy_buscar_producto_lineEdit.setCompleter(self.completer)

    # Método para limpiar los campos cada que se cambiar de página
    def limpiar_campos(self):
        # Labels añadir_producto
        self.add_referencia_lineEdit.clear()
        self.add_marca_lineEdit.clear()
        self.add_precio_adquisicion_lineEdit.clear()
        self.add_precio_ventas_lineEdit.clear()
        self.add_unidades_actuales_lineEdit.clear()
        self.add_codigoBarras_lineEdit.clear()
        self.modify_buscar_producto_lineEdit.clear()
        self.modify_marca_lineEdit.clear()
        self.modify_precio_adquisicion_lineEdit.clear()
        self.modify_precio_venta_lineEdit.clear()
        self.del_buscar_producto_lineEdit.clear()
        self.buy_buscar_producto_lineEdit.clear()
        self.buy_cantidad_ingresar_lineEdit.clear()
        self.aviso_add_label.setText("")
        self.aviso_modify_label.setText("")
        self.del_aviso_label.setText("")
        self.buy_aviso_label.setText("")

    # Método para validar la longitud del código de barras
    def setupValidatorsCodigoBarras(self):
        cbarras = QtGui.QRegularExpressionValidator(
            QtCore.QRegularExpression(r"\d{0,13}")
        )
        self.add_codigoBarras_lineEdit.setValidator(cbarras)
        self.modify_buscar_producto_lineEdit.setValidator(cbarras)
        self.del_buscar_producto_lineEdit.setValidator(cbarras)
        self.buy_buscar_producto_lineEdit.setValidator(cbarras)

    # Método para definir los precios
    def setupValidatorsPrecios(self):
        # Límite recomendado para precios (hasta 99999999.99)
        validacion_precios = QtGui.QRegularExpressionValidator(
            QtCore.QRegularExpression(r"\d{1,12}(\.\d{1,2})?")
        )
        self.add_precio_adquisicion_lineEdit.setValidator(validacion_precios)
        self.add_precio_ventas_lineEdit.setValidator(validacion_precios)
        self.modify_precio_adquisicion_lineEdit.setValidator(validacion_precios)
        self.modify_precio_venta_lineEdit.setValidator(validacion_precios)

    # Método para definir la cantidad de unidades (máximo 99.999)
    def setupValidatorsUnidades(self):
        validacion_unidades = QtGui.QRegularExpressionValidator(
            QtCore.QRegularExpression(r"\d{0,7}")
        )
        self.add_unidades_actuales_lineEdit.setValidator(validacion_unidades)
        self.buy_cantidad_ingresar_lineEdit.setValidator(validacion_unidades)

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

    def showErrorMessage(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText(message)
        msg_box.setWindowTitle("Error de autenticación")
        msg_box.exec_()

    def show_success_dialog(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(message)
        msg_box.setWindowTitle("Éxito")
        msg_box.exec_()


    def add_productos(self):
        referencia = self.add_referencia_lineEdit.text()
        marca = self.add_marca_lineEdit.text()
        precio_adquisicion = self.add_precio_adquisicion_lineEdit.text()
        precio_venta = self.add_precio_ventas_lineEdit.text()
        unidades_actuales = self.add_unidades_actuales_lineEdit.text()
        codigo_barras = self.add_codigoBarras_lineEdit.text()
        if precio_venta and precio_adquisicion and unidades_actuales and codigo_barras != "":
            if self.inventario.crear_productos(
                referencia,
                precio_adquisicion,
                precio_venta,
                codigo_barras,
                marca,
                unidades_actuales,
            ):
                self.show_success_dialog("Producto agregado correctamente")
                self.aviso_add_label.setText("Producto agregado correctamente")
                self.limpiar_campos()
            else:
                self.showErrorMessage(
                    "Producto no agregado. Por favor, verifica la información."
                )
                self.aviso_add_label.setText(
                    "Producto no agregado. Por favor, verifica la información."
                )
        else:
            self.showErrorMessage(
                    "Algun campo esta vacío. Por favor, verifica la información."
                )
            self.aviso_add_label.setText(
                "Algun campo esta vacío. Por favor, verifica la información."
            )
        self.ver_productos()
        self.ver_productosComprar()
        self.ver_productosEliminar()
        self.ver_productosModificar()
        
    def ver_productos(self):
        table: QTableWidget = self.tabla_ver_productos
        table.setRowCount(0)
        for i, row in self.gestion_datos.productos.iterrows():
            table.insertRow(i)
            for j, (_, value) in enumerate(row.items()):
                table.setItem(i, j, QTableWidgetItem(str(value)))
                
    def ver_productosModificar(self):
        table: QTableWidget = self.tableWidget_modificar
        table.setRowCount(0)
        for i, row in self.gestion_datos.productos.iterrows():
            table.insertRow(i)
            for j, (_, value) in enumerate(row.items()):
                table.setItem(i, j, QTableWidgetItem(str(value)))
                     
    def ver_productosEliminar(self):
        table: QTableWidget = self.del_tabla_productos
        table.setRowCount(0)
        for i, row in self.gestion_datos.productos.iterrows():
            table.insertRow(i)
            for j, (_, value) in enumerate(row.items()):
                table.setItem(i, j, QTableWidgetItem(str(value)))

    def ver_productosComprar(self):
        self.tableWidget_comprarStock.setRowCount(0)
        for i, row in self.gestion_datos.productos.iterrows():
            self.tableWidget_comprarStock.insertRow(i)
            for j, (colname, value) in enumerate(row.items()):
                self.tableWidget_comprarStock.setItem(
                    i, j, QTableWidgetItem(str(value))
                )

    def mostrar_formulario(self):
        if self.modify_buscar_producto_lineEdit.text() != "":
            # print(self.productos)
            codigo_barras = self.gestion_datos.buscar_producto(
                self.modify_buscar_producto_lineEdit.text()
            )
            # print(codigo_barras)
            if codigo_barras:
                self.frame_formularioModificar.show()
            else:
                # print(codigo_barras)
                self.showErrorMessage(
                    "Producto Inexistente. Por favor, verifica la información."
                )
                self.aviso_modify_label.setText(
                    "Producto Inexistente. Por favor, verifica la información."
                )
        else:
            self.showErrorMessage("Campo vacío. Por favor, verifica la información.")
            self.aviso_modify_label.setText(
                "Campo vacío. Por favor, verifica la información."
            )

    def modificar_productos(self):
        codigo = self.modify_buscar_producto_lineEdit.text()
        marca = self.modify_marca_lineEdit.text()
        precio_a = self.modify_precio_adquisicion_lineEdit.text()
        precio_v = self.modify_precio_venta_lineEdit.text()
        if self.inventario.modificar_producto(marca, precio_a, precio_v, codigo):
            self.ver_productos()  # Actualizar la tabla de productos
            self.show_success_dialog("Producto modificado correctamente")
            self.aviso_modify_label.setText("Produdcto modificado correctamente")
            self.limpiar_campos()
            self.frame_formularioModificar.hide()
            # print(datos_producto)
        else:
            self.showErrorMessage("Error en los campos, verifique la información")
            self.aviso_modify_label.setText(
                "Error en los campos. Porfavor, verifique la información"
            )
        self.ver_productosComprar()
        self.ver_productosEliminar()
        self.ver_productosModificar()
        self.ver_productos()
    
    def descontinuar_producto(self): 
        codigo = self.del_buscar_producto_lineEdit.text()
        if codigo == "":
            self.showErrorMessage(
                    "Campo Vacio."
                )
            self.aviso_modify_label.setText(
                    "Campo Vacio."
                )
        elif codigo in self.gestion_datos.productos["Codigo de barras"].values:
            self.gestion_datos.descontinuar_producto(codigo)
        elif int(codigo) in self.gestion_datos.productos["Codigo de barras"].values:
            codigo = int(codigo)
            self.gestion_datos.descontinuar_producto(codigo)
        self.ver_productosComprar()
        self.ver_productosEliminar()
        self.ver_productosModificar()
        self.ver_productos()
         
    def verificar_existencia_stock(self):
        if self.buy_buscar_producto_lineEdit.text() != "":
            codigo = self.buy_buscar_producto_lineEdit.text()
            if (
                codigo in self.gestion_datos.productos["Codigo de barras"].values
                or int(codigo) in self.gestion_datos.productos["Codigo de barras"].values
            ):
                return True
            else:
                return False
        else:
            self.showErrorMessage("Campo vacío, por favor ingrese la información.")

    def mostrar_formulario2(self):
            codigo_barras = self.verificar_existencia_stock()
            if codigo_barras == True:
                self.frame_formulario_comprar_stock.show()
            else:
                self.showErrorMessage(
                    "Producto Inexistente. Por favor, verifica la información."
                )
                self.aviso_modify_label.setText(
                    "Producto Inexistente. Por favor, verifica la información."
                )

    def comprar_stock(self):
        codigo = self.buy_buscar_producto_lineEdit.text()
        stock = self.buy_cantidad_ingresar_lineEdit.text()
        if int(codigo) in self.gestion_datos.productos["Codigo de barras"].values:
            codigo = int(codigo)
        if stock != "" and validacion_Stock(int(stock)):
            self.inventario.comprar_stock(codigo, int(stock))
            self.ver_productosComprar()
            self.ver_productosEliminar()
            self.ver_productosModificar()
            self.ver_productos()
