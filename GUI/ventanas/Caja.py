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
import random
#from login import Login

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
    def __init__(self, control_navegacion, ventana_login):
        super().__init__()
        loadUi(r"GUI\ui\PruebaMenu.ui", self)
        self.ventana_login  =ventana_login
        self.control_navegacion=control_navegacion
        self.MenuButton.clicked.connect(self.CajaWin)
        self.ReportButton.clicked.connect(self.repWin)
        self.LogOut.clicked.connect(self.volver_login)
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)

    def volver_login(self):
        self.ventana_login.show()
        self.close()

    def CajaWin(self):
        self.control_navegacion.mostrar_ventana("caja")

    def repWin(self):
        self.control_navegacion.mostrar_ventana("reporte")

class Caja(QMainWindow):
    def __init__(self, control_navegacion):
        super().__init__()
        loadUi(r"GUI\ui\Caja.ui", self)
        self.control_navegacion = control_navegacion
        self.Atras.clicked.connect(self.backMenu)
        self.cajero = Cajero()
        self.gestion_datos = GestionDatos()
        self.cedulaCliente = None
        self.posibleCedula = None
        self.posibleTelefono = None
        self.posibleNombre = None
        self.nombreCliente = None
        self.telefonoCliente = None
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
        self.BotonCliente.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.Clientes_2))
        self.BotonProductos.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.Productos_3))
        self.BotonServicios.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.Servicios_4))
        self.BotonPago.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.Pago_4))
        self.BotonCarrito.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.Carrito_4))

        #ancho de columnas tablas
        self.TablaCedulas.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.TablaProductos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.TablaTotalPro.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.TablaServicios.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.TablaTotalSer.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.TaCaro.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.TaSer.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

##////////FUNCIONES CLIENTES/////////##
        self.ChangeCli.clicked.connect(self.clickchange)
        self.ConfirmarNew.clicked.connect(self.posible_cliente)
        self.ConfirmarAnt.clicked.connect(self.creado)
        self.Seleccionar.clicked.connect(self.selCli)
        self.Nuevo_2.clicked.connect(self.New)
        self.AggProducto.clicked.connect(self.total_productos)
        self.AggServicios.clicked.connect(self.total_servicios)
        self.ConfirmarPago.clicked.connect(self.saber_pago)
        self.YES.clicked.connect(self.mostrar_carrito_yes)
        self.Factura.clicked.connect(self.crear_factura)
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
        self.Reserva.clicked.connect(self.date)
        self.Fast.clicked.connect(self.nodate)
        self.mostrar_servicios()
        self.mostrar_productos()

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
    
    #Metodo para ocultar los botones y crear el boton cambiar metodo de pago
    def confirmPay(self):
        #espacio para almacenar el dato
        self.MetodosPago.hide()
        self.ConfirmarPago.hide()
        self.CambiarPago.show()

    #Metodo para cambiar metodo de pago
    def changePay(self):
        #espacio para borrar el dato
        self.MetodosPago.show()
        self.ConfirmarPago.show()
        self.CambiarPago.hide()
    
    #metodo para ocutar la fecha
    def nodate(self):
        self.Fecha.hide()

    #metodo para mostra la fecha
    def date(self):
        self.Fecha.show()

    #metodo para ocultar los objetos de servicios y mostrar el boton de cambiar servicios
    def confirmServ(self):
        #espacio para almacenar los datos
        self.Servicios.hide()
        self.LabelStock.hide()
        self.EleServicios.hide()
        self.AggServicios.hide()
        self.TablaServicios.hide()
        self.LabelServ.hide()
        self.StockServicios.hide()
        self.TotalServicios.hide()
        self.TablaTotalSer.hide()
        self.Fast.hide()
        self.Reserva.hide()
        self.Fecha.hide()
        self.ConfirmarServicios.hide()
        self.EditarServ.show()

    #metodo para cambiar los servicios
    def changeServ(self):
        #espacio para borrar los datos
        self.Servicios.show()
        self.LabelStock.show()
        self.EleServicios.show()
        self.AggServicios.show()
        self.TablaServicios.show()
        self.LabelServ.show()
        self.StockServicios.show()
        self.TotalServicios.show()
        self.TablaTotalSer.show()
        self.Fast.show()
        self.Reserva.show()
        self.Fecha.hide()
        self.ConfirmarServicios.show()
        self.EditarServ.hide()

    #metodo para oculatr los objetos de productos y crear el boton cambiar productos
    def confirmPro(self):
        #espacio para añadir los productos
        self.TablaProductos.hide()
        self.LabelProductos.hide()
        self.StockProductos.hide()
        self.TotalPro.hide()
        self.TablaTotalPro.hide()
        self.ConfirmarPro.hide()
        self.EditarPro.show()
        self.LabelStockPro.hide()
        self.AggProducto.hide()
        self.EleProductos.hide()

    #metodo para cambiar los productos
    def changePro(self):
        #espacio para borarr los productos
        self.TablaProductos.show()
        self.LabelProductos.show()
        self.StockProductos.show()
        self.TotalPro.show()
        self.TablaTotalPro.show()
        self.ConfirmarPro.show()
        self.EditarPro.hide()
        self.LabelStockPro.show()
        self.AggProducto.show()
        self.EleProductos.show()

    #metodo para confirmar el seleccionar un cliente que ya esta dentro de la base de datos
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

    #metodo para confirmar un cliente nuevo ingresado por el usuario
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

    #metodo para cambiar el client y mostrar
    def clickchange(self):
        self.Seleccionar.show()
        self.Nuevo_2.show()
        self.ChangeCli.hide()

    #metodo para verificar si el cliente nuevo es correcto
    def posible_cliente(self):
        self.posibleCedula = self.Ced_2.text()
        self.posibleNombre = self.Nom_2.text()
        self.posibleTelefono = self.Tel_2.text()
        self.cedulaCliente = self.Ced_2.text()
        self.nombreCliente = self.Nom_2.text()
        self.telefonoCliente = self.Tel_2.text()
        
        
    def CheckNewClient(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Validación")
        msg_box.setStandardButtons(QMessageBox.Ok)
        if self.cajero.añadir_cliente(self.posibleCedula, self.posibleNombre, self.telefonoCliente):
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
            #self.cedulaCliente = cedula
        else:
            msg_box.setText("Cliente Incorrecto")
            msg_box.exec_()

    #metodo para volver al menu
    def backMenu(self):
        self.control_navegacion.mostrar_ventana("menu")

    def creado(self):
        cedula = self.IngCedula.text()
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Validación")
        msg_box.setStandardButtons(QMessageBox.Ok)
        if cedula == "":
            msg_box.setText("Cliente no encontrado")
        elif str(cedula) in str(self.gestion_datos.clientes["Cedula"].values): #Comprobar si dato ya existe
                self.cedulaCliente = cedula
                cliente = self.gestion_datos.clientes[self.gestion_datos.clientes["Cedula"] == int(cedula)]
                self.nombreCliente = cliente["Nombre"]
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
    
    def total_productos(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Validación")
        msg_box.setStandardButtons(QMessageBox.Ok)
        codigo_barras = self.EleProductos.text()
        cantidad = self.StockProductos.text()
        if codigo_barras != "" and cantidad != "": 
            if codigo_barras in self.gestion_datos.productos["Codigo de barras"].values or int(codigo_barras) in self.gestion_datos.productos["Codigo de barras"].values:
                codigo = 0
                datos_producto = self.gestion_datos.productos[self.gestion_datos.productos["Codigo de barras"] == int(codigo_barras)]
                while codigo in self.gestion_datos.venta_productos["ID venta"].values:
                    codigo = random.randint(1,1000)

                self.gestion_datos.agregar_venta_producto(codigo, self.cedulaCliente, self.nombreCliente,datos_producto.loc[:,"Referencia"], cantidad, self.cajero.mostra_total_productos(codigo_barras, int(cantidad)), 0)
                self.mostrar_total_productos()
            else:
                msg_box.setText("Codigo inexistente")
                msg_box.exec_()
        else:
            msg_box.setText("campos vacios")
            msg_box.exec_()
            
    def total_servicios(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Validación")
        msg_box.setStandardButtons(QMessageBox.Ok)
        id_servicio = self.EleServicios.text()
        cantidad = self.StockServicios.text()
        if cantidad != "" and id_servicio != "":
            codigo = 0
            datos_servicio = self.gestion_datos.servicios[self.gestion_datos.servicios["ID servicio"] == (id_servicio)]
            while codigo in self.gestion_datos.venta_servicios["ID venta"].values:
                codigo = random.randint(1,1000)
            self.gestion_datos.agregar_venta_producto(codigo, self.cedulaCliente, self.nombreCliente,datos_servicio.loc[:,"Nombre Servicio"], cantidad, self.cajero.mostra_total_servicios(id_servicio, int(cantidad)), 0)
            self.mostrar_total_servicios()
            msg_box.setText("Servicio añadido")
            msg_box.exec_()
        else:
            msg_box.setText("Servicios invalido")
            msg_box.exec_()
    
    def mostrar_productos(self):
        self.TablaProductos.setRowCount(0)
        for i, row in self.gestion_datos.productos.iterrows():
            self.TablaProductos.insertRow(i)
            for j, (colname, value) in enumerate(row.items()):
                self.TablaProductos.setItem(i, j, QTableWidgetItem(str(value)))
    
    def mostrar_servicios(self):
        self.TablaServicios.setRowCount(0)
        for i, row in self.gestion_datos.servicios.iterrows():
            self.TablaServicios.insertRow(i)
            for j, (colname, value) in enumerate(row.items()):
                self.TablaServicios.setItem(i, j, QTableWidgetItem(str(value)))
    
    def mostrar_total_productos(self):
        self.TablaTotalPro.setRowCount(0)
        for i, row in self.cajero.df.iterrows():
            self.TablaTotalPro.insertRow(i)
            for j, (colname, value) in enumerate(row.items()):
                self.TablaTotalPro.setItem(i, j, QTableWidgetItem(str(value)))
    
    def mostrar_total_servicios(self):
        self.TablaTotalSer.setRowCount(0)
        for i, row in self.cajero.serviciosC.iterrows():
            self.TablaTotalSer.insertRow(i)
            for j, (colname, value) in enumerate(row.items()):
                self.TablaTotalSer.setItem(i, j, QTableWidgetItem(str(value)))

    def saber_pago(self):
        metodo_pago = self.MetodosPago.currentText()
        print(metodo_pago)

    def mostrar_carrito_yes(self):
        self.TaCaro.setRowCount(0)
        precio = str(self.cajero.factura_con())
        self.TotalGeneral.setText(precio)
        for i, row in self.cajero.df.iterrows():
            self.TaCaro.insertRow(i)
            for j, (colname, value) in enumerate(row.items()):
                self.TaCaro.setItem(i, j, QTableWidgetItem(str(value)))
        
        self.TaSer.setRowCount(0)
        for i, row in self.cajero.serviciosC.iterrows():
            self.TaSer.insertRow(i)
            for j, (colname, value) in enumerate(row.items()):
                self.TaSer.setItem(i, j, QTableWidgetItem(str(value)))
        
        
    def vaciar_carrito(self):
        self.changePay()
        self.changePro()
        self.changeServ()
        self.clickchange()
        self.posibleCedula = None
        self.posibleNombre = None
        self.posibleTelefono = None
        self.cajero.vaciar_carrito()
        self.mostrar_carrito_yes()
    
    def crear_factura(self):
        precio = self.cajero.factura_con()
        archivo = open("mi_archivo.txt", "w")
        archivo.write("-----------Factura---------\n")
        archivo.write(f"Nombre Cliente = {self.nombreCliente}\n")
        archivo.write(f"Nombre Cedula cliente = {self.cedulaCliente}\n")
        self.cajero.serviciosC.to_excel("comprasde servicios.xlsx")
        self.cajero.df.to_excel("compras de productos..xlsx")
        archivo.write(f"Total {precio}")
        archivo.close()
        if validar_Cedula(self.posible_cliente) and validacion_Telefono(self.posibleTelefono) and validar_NombreCom(self.posibleNombre):
            self.gestion_datos.agregar_cliente(self.posibleCedula,self.posibleNombre, self.posibleTelefono)

        

class Reporte(QMainWindow, CBackground):
    def __init__(self, control_navegacion):
        super().__init__()
        loadUi(r"GUI\ui\ReporteDiario.ui", self)
        self.control_navegacion=control_navegacion
        self.Reporte_2.clicked.connect(self.Backmenu)
        self.Reporte.clicked.connect(self.VistaPre)

        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)

    def Backmenu(self):
        self.control_navegacion.mostrar_ventana("menu")

    def VistaPre(self):
        pass

    def envio(self):
        pass
    
    def showdate(self):
        pass
    

#/////CLASE CONEXIONES/////#
class Aplicacion(QMainWindow):
    def __init__(self, ventana_login):
        super().__init__()
        self.ventana_login = ventana_login
        self.control_navegacion = ControlNavegacion()

        self.ventana_principal = Menu(self.control_navegacion, self.ventana_login)
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