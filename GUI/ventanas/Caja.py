from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem, QWidget
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, Qt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import (
    QPainter, QBrush,
    QColor, QPixmap, 
    QCursor
)
#from DATA import GestionDatos
import sys
#from DATA import GestionDatos
#from API.Validaciones import *

class Caja(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(r"GUI\ui\Caja.ui", self,)

        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint) #borrar los botones externos de la pagina original
        self.BotonCliente.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.Clientes_2))
        self.BotonProductos.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.Productos_3))
        self.BotonServicios.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.Servicios_4))
        self.BotonPago.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.Pago_4))
        self.BotonCarrito.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.Carrito_4))

        #definir funciones botones pagina Clientes
        self.Seleccionar.clicked.connect(self.selCli)
        self.Nuevo_2.clicked.connect(self.New)
        self.Clientes.hide()
        self.Cedula_2.hide()
        self.Nombre_2.hide()
        self.Telefono_2.hide()
        self.Ced_2.hide()
        self.Tel_2.hide()
        self.Nom_2.hide()

        #definir funciones para validar la informacion
    def ingresar_lista_cedulas(self):
        for cedula, nombre in self.lista:
            self.Clientes.addItem(cedula, nombre)

        #definir funciones layout pagina sevicios
        self.dateEdit.hide()
        self.Reserva.clicked.connect(self.showdate)
        self.Fast.clicked.connect(self.hidedate)
    
    def showdate(self):
        self.dateEdit.show()
    
    def hidedate(self):
        self.dateEdit.hide()

    def selCli(self):
        self.Clientes.show()
        self.Cedula_2.hide()
        self.Nombre_2.hide()
        self.Telefono_2.hide()
        self.Ced_2.hide()
        self.Tel_2.hide()
        self.Nom_2.hide()

    def New(self):
        self.Clientes.hide()
        self.Cedula_2.show()
        self.Nombre_2.show()
        self.Telefono_2.show()
        self.Ced_2.show()
        self.Tel_2.show()
        self.Nom_2.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    caja = Caja()
    caja.show()  # Asegúrate de mostrar la ventana
    sys.exit(app.exec_())