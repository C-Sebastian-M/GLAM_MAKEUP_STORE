from PyQt5.uic import loadUi
import pandas as pd
from PyQt5.QtWidgets import (
    QMainWindow,
    QHeaderView,
    QTableWidgetItem,
    QMessageBox,
    QCompleter,
    QTableWidget
)
from PyQt5.QtCore import QPropertyAnimation, Qt, QStringListModel
from PyQt5 import QtCore, QtWidgets, QtGui
from API.DATA import GestionDatos
from API.Validaciones import *
from API.prueba import Cajero
from GUI.sub_ventanas.custom.utils.css import CBackground

class VentasAdmin(QMainWindow, CBackground):
    def __init__(self):
        super(VentasAdmin, self).__init__()
        loadUi(
            r"GUI\sub_ventanas\ui\Ventas.ui",
            self,
        )
        self.gestion_datos = GestionDatos()
        self.cajero = Cajero()
        self.pushButton_menu.clicked.connect(self.mover_menu)
        # Botones
        self.pushButton_actualizarPagos.clicked.connect(self.mostrar_pagos)
        self.pushButton_mostrarModificar.clicked.connect(self.mostrar_ventas)
        self.pushButton_addPago.clicked.connect(self.mostrar_formulario_addPago)
        self.pushButton_eliminarPago.clicked.connect(self.mostrar_formulario_delPago)
        self.pushButton_confirmarPago.clicked.connect(self.add_metodoPago)
        self.pushButton_delPago.clicked.connect(self.del_metodoPago)
        self.pushButton_modificarBuscar.clicked.connect(self.mostrar_formulario)
        self.pushButton_eliminarVenta.clicked.connect(self.mostrar_formularioEliminar)
        self.pushButton_ConfirmarEliminado.clicked.connect(self.ConfirmarEliminado)
        self.pushButton_CancelarEliminado.clicked.connect(self.CancelarEliminado)
        self.pushButton_guardarInfo.clicked.connect(self.guardarInfo)
        self.pushButton_fecha.clicked.connect(self.mostrar_calendario)
        self.frame_formulario.hide()
        self.frame_calendario.hide()
        self.frame_formularioEliminar.hide()
        self.frame_addPago.hide()
        self.frame_delPago.hide()
        #self.df = pd.read_excel("registros.xlsx", sheet_name="productosServicios")
        #id_ventas = self.df["ID venta"].astype(str).tolist()
        #self.modelo_datos = QStringListModel(id_ventas)
        #self.completer = QCompleter(self.modelo_datos, self)
        #self.completer.setCaseSensitivity(False)  # Ignorar mayúsculas y minúsculas
        #self.completer.setFilterMode(
        #    Qt.MatchContains
        #)  # Coincidir con cualquier parte del texto
        #self.completer.setCompletionMode(QCompleter.PopupCompletion)
        #self.completer.setPopup(self.listView_buscar)
        #self.lineEdit_idVenta.setCompleter(self.completer)

        # Mas botones
        self.pushButton_pagos.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pagina_pagos)
        )
        self.pushButton_pagos.clicked.connect(self.limpiar_campos)
        self.pushButton_ventas.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pagina_ventas)
        )
        self.tableWidget_pagos.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.pagos = self.gestion_datos.metodo_pago["Metodo de pago"].tolist()
        self.comboBox_pago.addItems(self.pagos)
        self.pushButton_ventas.clicked.connect(self.limpiar_campos)
       
    def limpiar_campos(self):
        self.lineEdit_addPago.clear()
        self.lineEdit.clear()
        self.lineEdit_addPrecio.clear()
        self.lineEdit_addServicio.clear()
        self.lineEdit_buscarEliminar.clear()
        self.lineEdit_nuevoServicio.clear()
        self.lineEdit_nuevoPrecio.clear()
        self.lineEdit_modificar.clear()

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


    def mostrar_pagos(self):
        table: QTableWidget = self.tableWidget_pagos
        table.setRowCount(0)
        for i, row in self.gestion_datos.metodo_pago.iterrows():
            table.insertRow(i)
            for j, (_, value) in enumerate(row.items()):
                table.setItem(i, j, QTableWidgetItem(str(value)))

    def mostrar_ventas(self):
        # Implement your logic to display the ventas page here
        # Similar to mostrar_pagos, it likely returns None
        return None

    def mostrar_formulario_addPago(self, servicio):
        self.frame_addPago.show()
    
    def mostrar_formulario_delPago(self):
        self.frame_delPago.show()
    
    def del_metodoPago(self):
        if self.comboBox_pago.currentIndex() != -1:
            pago = self.comboBox_pago.currenText()
            if pago in self.gestion_datos.metodo_pago["Metodos de pago"].values:
                self.gestion_datos.metodo_pago = self.gestion_datos.metodo_pago[self.gestion_datos.metodo_pago['ID'] != pago]
                self.gestion_datos.guardar_dataframes()
            self.show_success_dialog("Metodo de pago eliminado correctamente")
            self.aviso_pago.show("Metodo de pago eliminado correctamente")
            self.frame_delPago.hide()
        elif int(pago) in self.gestion_datos.metodo_pago['ID'].values:
            pago = int(usuario)
            self.gestion_datos.metodo_pago = self.gestion_datos.metodo_pago[self.gestion_datos.metodo_pago['ID'] != pago]
            self.gestion_datos.guardar_dataframes()
            self.show_success_dialog("Metodo de pago eliminado correctamente")
            self.aviso_pago.show("Metodo de pago eliminado correctamente")
            self.frame_delPago.hide()
        else:
            return False  
                

    def mostrar_formulario(self):
        None

    def mostrar_formularioEliminar(self):
        None

    def ConfirmarEliminado(self):
        None
    
    def CancelarEliminado(self):
        None
    
    def guardarInfo(self):  
        None
    def mostrar_calendario(self):
        # Implement your logic to display the calendar here
        # Similar to mostrar_pagos, it likely returns None
        return None
    

    def add_metodoPago(self):
        id_metodo = self.lineEdit_addPago.text()
        metodo = self.lineEdit.text()
        if id_metodo not in self.gestion_datos.metodo_pago["ID"].values and int(id_metodo) not in self.gestion_datos.metodo_pago["ID"].values:
            nueva_fila = pd.DataFrame([[id_metodo, metodo]], columns=['ID', 'Metodo de pago'])
            self.gestion_datos.metodo_pago = pd.concat([self.gestion_datos.metodo_pago, nueva_fila], ignore_index=True)
            self.frame_addPago.hide()
            
            self.pagos = self.gestion_datos.metodo_pago["Metodo de pago"].tolist()
            self.comboBox_pago.addItems(self.pagos)