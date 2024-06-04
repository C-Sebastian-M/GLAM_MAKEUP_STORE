from PyQt5.uic import loadUi
import pandas as pd
from PyQt5.QtWidgets import (
    QMainWindow,
    QHeaderView,
    QTableWidgetItem,
    QMessageBox,
    QCompleter,
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
        self.completer.setPopup(self.listView_buscar)
        #self.lineEdit_idVenta.setCompleter(self.completer)

        # Mas botones
        self.pushButton_pagos.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pagina_pagos)
        )
        self.pushButton_pagos.clicked.connect(self.limpiar_campos)
        self.pushButton_ventas.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pagina_ventas)
        )
        self.pushButton_ventas.clicked.connect(self.limpiar_campos)
    
    def limpiar_campos(self):
        None

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



    def mostrar_pagos(self):
        None

    def mostrar_ventas(self):
        # Implement your logic to display the ventas page here
        # Similar to mostrar_pagos, it likely returns None
        return None

    def mostrar_formulario_addPago(self):
        # Implement your logic to display the add payment form here
        # Similar to mostrar_pagos, it likely returns None
        return None

    def mostrar_formulario_delPago(self):
        None

    def add_metodoPago(self):
        None

    def del_metodoPago(self):
        None

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
