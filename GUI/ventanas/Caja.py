from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem, QWidget, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, Qt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import (
    QPainter, QBrush,
    QColor, QPixmap, 
    QCursor
)
import sys
from API.prueba import Cajero
from API.Validaciones import *
from API.DATA import GestionDatos


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
        self.cajero = Cajero()
        self.gestion_datos = GestionDatos()
        self.cedulaCliente = None
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint) #borrar los botones externos de la pagina original
        self.BotonCliente.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.Clientes_2))
        self.BotonProductos.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.Productos_3))
        self.BotonServicios.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.Servicios_4))
        self.BotonPago.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.Pago_4))
        self.BotonCarrito.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.Carrito_4))

##////////FUNCIONES CLIENTES/////////##
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
        self.ConfirmarNew.hide()
        self.ConfirmarAnt.hide()
        self.ChangeCli.hide()
        self.Fecha.hide()
        self.Reserva.clicked.connect(self.showdate)
        self.Fast.clicked.connect(self.hidedate)

####//////////////////FUNCION BOTONES PRODUCTOS/////////////###
        self.ConfirmarPro.clicked.connect(self.confirmPro)
        self.EditarPro.clicked.connect(self.changePro)
        self.EditarPro.hide()
###///////////////FUNCION BOTONES SERVICIOS/////////////////###
        self.ConfirmarServicios.clicked.connect(self.confirmServ)
        self.EditarServ.clicked.connect(self.changeServ)
        self.Reserva.clicked.connect(self.date)
        self.Fast.clicked.connect(self.nodate)
        self.Fecha.hide()
        self.EditarServ.hide()
###////////////////////FUNCION METODO DE PAGO//////////////###
        self.ConfirmarPago.clicked.connect(self.confirmPay)
        self.CambiarPago.clicked.connect(self.changePay)
        self.CambiarPago.hide()
    
    def confirmPay(self):
        #espacio para almacenar el dato
        self.MetodosPago.hide()
        self.ConfirmarPago.hide()
        self.CambiarPago.show()

    def changePay(self):
        #espacio para borrar el dato
        self.MetodosPago.show()
        self.ConfirmarPago.show()
        self.CambiarPago.hide()
    
    def nodate(self):
        self.Fecha.hide()

    def date(self):
        self.Fecha.show()

    def confirmServ(self):
        #espacio para almacenar los datos
        self.TablaServicios.hide()
        self.LabelServ.hide()
        self.StockServicios.hide()
        self.TotalServicios.hide()
        self.viewtotal.hide()
        self.Fast.hide()
        self.Reserva.hide()
        self.Fecha.hide()
        self.ConfirmarServicios.hide()
        self.EditarServ.show()

    def changeServ(self):
        #espacio para borrar los datos
        self.TablaServicios.show()
        self.LabelServ.show()
        self.StockServicios.show()
        self.TotalServicios.show()
        self.viewtotal.show()
        self.Fast.show()
        self.Reserva.show()
        self.Fecha.hide()
        self.ConfirmarServicios.show()
        self.EditarServ.hide()
        
    def confirmPro(self):
        #espacio para añadir los productos
        self.TablaProductos.hide()
        self.LabelProductos.hide()
        self.StockProductos.hide()
        self.TotalPro.hide()
        self.ListaTotal.hide()
        self.ConfirmarPro.hide()
        self.EditarPro.show()
    
    def changePro(self):
        #espacio para borarr los productos
        self.TablaProductos.show()
        self.LabelProductos.show()
        self.StockProductos.show()
        self.TotalPro.show()
        self.ListaTotal.show()
        self.ConfirmarPro.show()
        self.EditarPro.hide()

    def clickchange(self):
        self.Seleccionar.show()
        self.Nuevo_2.show()
        self.ChangeCli.hide()

    def selCli(self):
        self.mostrar_clientes()
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
        if self.cajero.añadir_cliente(cedula, nombre, telefono):
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
            self.cedulaCliente = cedula
        else:
            msg_box.setText("Cliente Incorrecto")
            msg_box.exec_()

    def backMenu(self):
        self.control_navegacion.mostrar_ventana("menu")

    
    def showdate(self):
        self.dateEdit.show()
    
    def hidedate(self):
        self.dateEdit.hide()

    def creado(self):
        cedula = self.IngCedula.text()
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Validación")
        msg_box.setStandardButtons(QMessageBox.Ok)
        if str(cedula) in str(self.gestion_datos.clientes["Cedula"].values): #Comprobar si dato ya existe
                self.cedulaCliente = cedula
                msg_box.setText("Cliente encontrado en la lista")
        else:
            msg_box.setText("Cliente no encontrado")
        msg_box.exec_()
            
    def mostrar_clientes(self):
        self.TablaCedulas.setRowCount(0)
        for i, row in self.gestion_datos.clientes.iterrows():
            self.TablaCedulas.insertRow(i)
            for j, (colname, value) in enumerate(row.items()):
                self.TablaCedulas.setItem(i, j, QTableWidgetItem(str(value)))


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