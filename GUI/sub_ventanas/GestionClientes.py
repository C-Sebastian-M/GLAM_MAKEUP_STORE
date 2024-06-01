from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets, QtGui
from DATA import GestionDatos
import sys
from DATA import GestionDatos
from API.Validaciones import *


class GestionClientes(QMainWindow):
    def __init__(self):
        super(GestionClientes, self).__init__()
        loadUi(
            r"GUI\sub_ventanas\ui\gestion_clientes\GestionClientes.ui",
            self,
        )
        self.gestion_datos = GestionDatos()

        self.pushButton_menu.clicked.connect(self.mover_menu)
        # Botones
        self.pushButton_actualizar.clicked.connect(self.mostrar_clientes)
        self.pushButton_add.clicked.connect(self.registrar_cliente)
        self.pushButton_guardarInfo.clicked.connect(self.modificar_cliente)
        self.pushButton_eliminar.clicked.connect(self.eliminar_cliente)

        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # Mas botones
        self.pushButton_verClientes.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pagina_consulta)
        )
        self.pushButton_verClientes.clicked.connect(self.limpiar_campos)
        self.pushButton_addCliente.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pagina_add)
        )
        self.pushButton_addCliente.clicked.connect(self.limpiar_campos)
        self.pushButton_modificarCliente.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pagina_modificar)
        )
        self.pushButton_modificarCliente.clicked.connect(self.limpiar_campos)
        self.pushButton_eliminarCliente.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pagina_eliminar)
        )
        self.pushButton_eliminarCliente.clicked.connect(self.limpiar_campos)

        # Ancho columna adaptable
        self.tabla_verClientes.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.setupValidatorsCedula()
        self.setupValidatorsTelefono()

        # Ancho columna adaptable
        self.tabla_verClientes.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    def setupValidatorsCedula(self):
        validacion_numero = QtGui.QRegularExpressionValidator(
            QtCore.QRegularExpression(r"\d{9,12}")
        )
        self.lineEdit_addCedula.setValidator(validacion_numero)
        self.lineEdit_nuevaCedula.setValidator(validacion_numero)
        self.lineEdit_buscarModificar.setValidator(validacion_numero)
        self.lineEdit_buscarEliminar.setValidator(validacion_numero)
    
    def setupValidatorsTelefono(self):
        validacion_numero = QtGui.QRegularExpressionValidator(
            QtCore.QRegularExpression(r"\d{0,16}")
        )
        self.lineEdit_addCedula.setValidator(validacion_numero)
        self.lineEdit_nuevaCedula.setValidator(validacion_numero)
        self.lineEdit_buscarModificar.setValidator(validacion_numero)
        self.lineEdit_buscarEliminar.setValidator(validacion_numero)

    def limpiar_campos(self):
        self.lineEdit_addTelefono.clear()
        self.lineEdit_addCedula.clear()
        self.lineEdit_addNombre.clear()
        self.lineEdit_buscarModificar.clear()
        self.lineEdit_buscarEliminar.clear()
        self.lineEdit_nuevaCedula.clear()
        self.lineEdit_nuevoNombre.clear()
        self.lineEdit_nuevoTelefono.clear()

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

    # Acá se configura la base de datos
    def mostrar_clientes(self):
        self.tabla_verClientes.setRowCount(0)
        for i, row in self.gestion_datos.clientes.iterrows():
            self.tabla_verClientes.insertRow(i)
            for j, (colname, value) in enumerate(row.items()):
                self.tabla_verClientes.setItem(i, j, QTableWidgetItem(str(value)))

    def registrar_cliente(self):
        cedula = self.lineEdit_addCedula.text()
        nombre = self.lineEdit_addNombre.text()
        telefono = self.lineEdit_addTelefono.text()
        if (
            validar_Cedula(cedula)
            and validacion_Telefono(telefono)
            and validar_NombreCom(nombre)
        ):
            self.gestion_datos.agregar_cliente(cedula, nombre, telefono)
            self.mostrar_clientes()
            self.show_success_dialog("Cliente registrado con éxito.")
            self.limpiar_campos()
        else:
            self.showErrorMessage(
                "Error en los datos ingresados. Por favor, verifica la información."
            )

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

    def modificar_cliente(self):
        cedula = self.lineEdit_nuevaCedula.text()
        nuevos_datos = {
            "Nombre": self.lineEdit_nuevoNombre.text(),
            "Telefono": self.lineEdit_nuevoTelefono.text(),
        }
        self.gestion_datos.actualizar_cliente(cedula, nuevos_datos)
        self.mostrar_clientes()  # Actualizar la tabla de clientes

    def eliminar_cliente(self):
        cedula = self.lineEdit_buscarEliminar.text()
        self.gestion_datos.eliminar_clientes(cedula)
        self.mostrar_clientes()  # Actualizar la tabla de clientes


"""if __name__ == "__main__":
    app = QApplication(sys.argv)
    add = GestionClientes()
    add.show()  # Asegúrate de mostrar la ventana
    sys.exit(app.exec_())"""
