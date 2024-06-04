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
