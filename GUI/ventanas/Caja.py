from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem, QWidget, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, Qt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import (
    QPainter, QBrush,
    QColor, QPixmap, 
    QCursor
)
from API.DATA import GestionDatos
from API.Validaciones import *
import sys
from API.prueba import Cajero
from API.Validaciones import *


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

class ControlNavegacion:
    def __init__(self):
        self.ventanas = {}
        
    def agregar_ventana(self, nombre, ventana):
        self.ventanas[nombre] = ventana

    def mostrar_ventana(self, nombre):
        for ventana in self.ventanas.values():
            ventana.hide()
        self.ventanas[nombre].show()

#/////CLASES VENTANAS/////#
class Menu(CBackground, QMainWindow):
    def __init__(self, control_navegacion):
        super().__init__()
        loadUi(r"GUI\ui\PruebaMenu.ui", self,)
        self.control_navegacion=control_navegacion
        self.MenuButton.clicked.connect(self.CajaWin)
        self.ReportButton.clicked.connect(self.repWin)
        
    def CajaWin(self):
        self.control_navegacion.mostrar_ventana("caja")

    def repWin(self):
        self.control_navegacion.mostrar_ventana("reporte")

class Caja(QMainWindow):
    def __init__(self, control_navegacion):
        super().__init__()
        loadUi(r"GUI\ui\Caja.ui", self,)
        self.control_navegacion = control_navegacion
        self.Atras.clicked.connect(self.backMenu)
<<<<<<< HEAD
        self.cajero = Cajero()

=======
        
        self.gestion_datos = GestionDatos() #<- se instaura un objeto tipo Gestion de datos
        
>>>>>>> main
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint) #borrar los botones externos de la pagina original
        self.BotonCliente.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.Clientes_2))
        self.BotonProductos.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.Productos_3))
        self.BotonServicios.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.Servicios_4))
        self.BotonPago.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.Pago_4))
        self.BotonCarrito.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.Carrito_4))
        self.TablaCedulas.setColumnCount(3)
        self.TablaCedulas.setHorizontalHeaderLabels(['Cedula', 'Nombre', 'Telefono'])
        self.mostrar_clientes()

        #definir funciones botones pagina Clientes
        self.ChangeCli.clicked.connect(self.clickchange)
        self.ConfirmarNew.clicked.connect(self.CheckNewClient)
        self.ConfirmarAnt.clicked.connect(self.creado)
        self.Seleccionar.clicked.connect(self.selCli)
        self.Nuevo_2.clicked.connect(self.New)
        self.TablaCedulas.hide()
        self.IngCedula.hide()
        self.Cedula_2.hide()
        self.Nombre_2.hide()
        self.Telefono_2.hide()
        self.Ced_2.hide()
        self.Tel_2.hide()
        self.Nom_2.hide()
<<<<<<< HEAD
        self.ConfirmarNew.hide()
        self.ConfirmarAnt.hide()
        self.ChangeCli.hide()
##////////FUNCIONES CLIENTES/////////##

    def clickchange(self):
        self.Seleccionar.show()
        self.Nuevo_2.show()
        self.ChangeCli.hide()

    def selCli(self):
        self.TablaCedulas.show()
        self.IngCedula.show()
        self.Cedula_2.hide()
        self.Nombre_2.hide()
        self.Telefono_2.hide()
        self.Ced_2.hide()
        self.Tel_2.hide()
        self.Nom_2.hide()
        self.ConfirmarNew.hide()
        self.ConfirmarAnt.show()

    def New(self):
        self.TablaCedulas.hide()
        self.IngCedula.hide()
        self.Cedula_2.show()
        self.Nombre_2.show()
        self.Telefono_2.show()
        self.Ced_2.show()
        self.Tel_2.show()
        self.Nom_2.show()
        self.ConfirmarNew.show()
        self.ConfirmarAnt.hide()

    def CheckNewClient(self):
        cedula = self.Ced_2.text()
        nombre = self.Nom_2.text()
        telefono = self.Tel_2.text()
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Validación")
        msg_box.setStandardButtons(QMessageBox.Ok)
        if self.cajero.agregar_cliente(cedula, nombre, telefono):
            msg_box.setText("Cliente ingresado con éxito")
            msg_box.exec_()
            self.LabelCedula.hide()
            self.Seleccionar.hide()
            self.Nuevo_2.hide()
            self.ConfirmarNew.hide()
            self.ConfirmarAnt.hide()
            self.TablaCedulas.hide()
            self.IngCedula.hide()
            self.Cedula_2.hide()
            self.Nombre_2.hide()
            self.Telefono_2.hide()
            self.Ced_2.hide()
            self.Tel_2.hide()
            self.Nom_2.hide()
            self.ConfirmarNew.hide()
            self.ConfirmarAnt.hide()
            self.ChangeCli.show()
        else:
            msg_box.setText("Cliente Incorrecto")
            msg_box.exec_()
=======
        
>>>>>>> main

    def backMenu(self):
        self.control_navegacion.mostrar_ventana("menu")

        #definir funciones para validar la informacion
    def ingresar_lista_cedulas(self):
        self.lista =[(123, "hola"), (456, "adios")]
        for cedula, nombre in self.lista:
            self.Clientes.setItem(cedula, nombre)

        #definir funciones layout pagina sevicios
        self.dateEdit.hide()
        self.Reserva.clicked.connect(self.showdate)
        self.Fast.clicked.connect(self.hidedate)
    
    def showdate(self):
        self.dateEdit.show()
    
    def hidedate(self):
        self.dateEdit.hide()

<<<<<<< HEAD
    
    
    def creado(self):
        pass

=======
    def  selCli(self):
        self.TablaCedulas.show()
        self.IngCedula.show()
        self.Cedula_2.hide()
        self.Nombre_2.hide()
        self.Telefono_2.hide()
        self.Ced_2.hide()
        self.Tel_2.hide()
        self.Nom_2.hide()

    def New(self):
        self.TablaCedulas.hide()
        self.IngCedula.hide()
        self.Cedula_2.show()
        self.Nombre_2.show()
        self.Telefono_2.show()
        self.Ced_2.show()
        self.Tel_2.show()
        self.Nom_2.show()

    def CheckNewClient(self):
        cedula = self.Ced_2.text()
        telefono = self.Tel_2.text()
        nombre = self.Nom_2.text()
        if (
            validar_Cedula(cedula) #Se aplican las validaciones respectivas sobre la cedula, telefono y nombre
            and validacion_Telefono(telefono)
            and validar_NombreCom(nombre)
            and cedula not in self.gestion_datos.clientes["Cedula"].values #Se comprueba que la cedula no este en la BD
        ):
            self.gestion_datos.agregar_cliente(cedula, nombre, telefono)
            return True
        else:
            return False
    
    def mostrar_clientes(self):
        self.TablaCedulas.setRowCount(0)
        for i, row in self.gestion_datos.clientes.iterrows():
            self.TablaCedulas.insertRow(i)
            for j, (colname, value) in enumerate(row.items()):
                self.TablaCedulas.setItem(i, j, QTableWidgetItem(str(value)))
    
    def seleccionar(self):
        cedula = self.IngCedula.text()
        if validar_Cedula(cedula):
            datos_cliente = self.gestion_datos.clientes[self.gestion_datos.clientes["Cedula"]==cedula]
            if not datos_cliente.empty:
                return datos_cliente
>>>>>>> main

class Reporte(QMainWindow, CBackground):
    def __init__(self, control_navegacion):
        super().__init__()
        loadUi(r"GUI\ui\ReporteDiario.ui", self,)
        self.control_navegacion=control_navegacion
        self.Reporte_2.clicked.connect(self.Backmenu)
        self.Reporte.clicked.connect(self.VistaPre)
        self.VistaPrevia.clicked.connect(self.envio)

    def Backmenu(self):
        self.control_navegacion.mostrar_ventana("menu")

    def VistaPre(self):
        pass

    def envio(self):
        pass
    

#/////CLASE CONEXIONES/////#
class Aplicacion(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.control_navegacion = ControlNavegacion()

        self.ventana_principal = Menu(self.control_navegacion)
        self.ventana1 = Caja(self.control_navegacion)
        self.ventana2 = Reporte(self.control_navegacion)

        self.control_navegacion.agregar_ventana("menu", self.ventana_principal)
        self.control_navegacion.agregar_ventana("caja", self.ventana1)
        self.control_navegacion.agregar_ventana("reporte", self.ventana2)

        self.control_navegacion.mostrar_ventana("menu")

#/////MAIN////#
#if __name__ == "__main__":
#    app = Aplicacion(sys.argv)
#    sys.exit(app.exec_())