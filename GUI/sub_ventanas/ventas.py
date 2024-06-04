#from PyQt5.uic import loadUi
#import pandas as pd
#from PyQt5.QtWidgets import (
#    QMainWindow,
#    QHeaderView,
#    QTableWidgetItem,
#    QMessageBox,
#    QCompleter,
#)
#from PyQt5.QtCore import QPropertyAnimation, Qt, QStringListModel
#from PyQt5 import QtCore, QtWidgets, QtGui
#from API.DATA import GestionDatos
#from API.Validaciones import *
#from API.prueba import Cajero
#from GUI.sub_ventanas.custom.utils.css import CBackground


<<<<<<< HEAD
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
        #self.pushButton_actualizarPagos.clicked.connect(self.mostrar_pagos)
        # #self.pushButton_mostrarModificar.clicked.connect(self.mostrar_ventas)
        # self.pushButton_addPago.clicked.connect(self.mostrar_formulario_addPago)
        # self.pushButton_eliminarPago.clicked.connect(self.mostrar_formulario_delPago)
        # self.pushButton_confirmarPago.clicked.connect(self.add_metodoPago)
        # self.pushButton_delPago.clicked.connect(self.del_metodoPago)
        # self.pushButton_modificarBuscar.clicked.connect(self.mostrar_formulario)
        # self.pushButton_eliminarVenta.clicked.connect(self.mostrar_formularioEliminar)
        # self.pushButton_ConfirmarEliminado.clicked.connect(self.ConfirmarEliminado)
        # self.pushButton_CancelarEliminado.clicked.connect(self.CancelarEliminado)
        # self.pushButton_guardarInfo.clicked.connect(self.pushButton_guardarInfo)
        # self.pushButton_fecha.clicked.connect(self.mostrar_calendario)

        # Mas botones
        # self.pushButton_pagos.clicked.connect(
        #     lambda: self.stackedWidget.setCurrentWidget(self.pagina_pagos)
        # )
        # self.pushButton_pagos.clicked.connect(self.limpiar_campos)
        # self.pushButton_ventas.clicked.connect(
        #     lambda: self.stackedWidget.setCurrentWidget(self.pagina_ventas)
        # )
        # self.pushButton_ventas.clicked.connect(self.limpiar_campos)

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
=======
#class VentasAdmin(QMainWindow, CBackground):
#    def __init__(self):
#        super(VentasAdmin, self).__init__()
#        loadUi(
#            r"GUI\sub_ventanas\ui\Ventas.ui",
#            self,
#        )
#        self.gestion_datos = GestionDatos()
#        self.cajero = Cajero()
#        self.pushButton_menu.clicked.connect(self.mover_menu)
#        # Botones
#        self.pushButton_actualizarPagos.clicked.connect(self.mostrar_pagos)
#        self.pushButton_mostrarModificar.clicked.connect(self.mostrar_ventas)
#        self.pushButton_addPago.clicked.connect(self.mostrar_formulario_addPago)
#        self.pushButton_eliminarPago.clicked.connect(self.mostrar_formulario_delPago)
#        self.pushButton_confirmarPago.clicked.connect(self.add_metodoPago)
#        self.pushButton_delPago.clicked.connect(self.del_metodoPago)
#        self.pushButton_modificarBuscar.clicked.connect(self.mostrar_formulario)
#        self.pushButton_eliminarVenta.clicked.connect(self.mostrar_formularioEliminar)
#        self.pushButton_ConfirmarEliminado.clicked.connect(self.ConfirmarEliminado)
#        self.pushButton_CancelarEliminado.clicked.connect(self.CancelarEliminado)
#        self.pushButton_guardarInfo.clicked.connect(self.pushButton_guardarInfo)
#        self.pushButton_fecha.clicked.connect(self.mostrar_calendario)
#
#        # Mas botones
#        self.pushButton_pagos.clicked.connect(
#            lambda: self.stackedWidget.setCurrentWidget(self.pagina_pagos)
#        )
#        self.pushButton_pagos.clicked.connect(self.limpiar_campos)
#        self.pushButton_ventas.clicked.connect(
#            lambda: self.stackedWidget.setCurrentWidget(self.pagina_ventas)
#        )
#        self.pushButton_ventas.clicked.connect(self.limpiar_campos)
#
#    def mover_menu(self):
#        if True:
#            width = self.frame_control.width()
#            normal = 0
#            if width == 0:
#                extender = 270
#            else:
#                extender = normal
#            self.animacion = QPropertyAnimation(self.frame_control, b"minimumWidth")
#            self.animacion.setDuration(300)
#            self.animacion.setStartValue(width)
#            self.animacion.setEndValue(extender)
#            self.animacion.setEasingCurve(
#                QtCore.QEasingCurve.InOutQuart
#            )  # InQuad, InOutQuad, InCubic, InOutExpo
#            self.animacion.start()
#
>>>>>>> 9ab90341a1217c6cc1156587a71d313c6603d132
