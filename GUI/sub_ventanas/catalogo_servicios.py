from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets, QtGui
from DATA import GestionDatos
import sys
from DATA import GestionDatos
from API.Validaciones import *


class GestionServicios(QMainWindow):
    def __init__(self):
        super(GestionServicios, self).__init__()
        loadUi(
            r"GUI\sub_ventanas\ui\GestionServicios.ui",
            self,
        )
        self.gestion_datos = GestionDatos()

        self.pushButton_menu.clicked.connect(self.mover_menu)
        # Botones
        self.pushButton_actualizar.clicked.connect(self.mostrar_servicios)
        # self.pushButton_add.clicked.connect(self.registrar_servicio)
        # self.pushButton_guardarInfo.clicked.connect(self.modificar_servicio)
        # self.pushButton_eliminar.clicked.connect(self.eliminar_servicio)

        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # Mas botones
        self.pushButton_verServicios.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pagina_consulta)
        )
        self.pushButton_verServicios.clicked.connect(self.limpiar_campos)
        self.pushButton_addServicio.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pagina_add)
        )
        self.pushButton_addServicio.clicked.connect(self.limpiar_campos)
        self.pushButton_modificarServicio.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pagina_modificar)
        )
        self.pushButton_modificarServicio.clicked.connect(self.limpiar_campos)
        self.pushButton_eliminarServicio.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pagina_eliminar)
        )
        self.pushButton_eliminarServicio.clicked.connect(self.limpiar_campos)

        # Ancho columna adaptable
        self.tabla_verServicios.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        # self.setupValidatorsId()
        # self.setupValidatorsPrecio()

        # Ancho columna adaptable
        self.tabla_verServicios.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    # Permite ingrear solo numeros a los campos y el paraletro del metodo es la cantidad de caracteres
    """def setupValidatorsId(self):
        validacion_numero = QtGui.QRegularExpressionValidator(
            QtCore.QRegularExpression(r"\d{12}")
        )
        self.lineEdit_addId.setValidator(validacion_numero)
        self.lineEdit_nuevoId.setValidator(validacion_numero)
        self.lineEdit_buscarModificar.setValidator(validacion_numero)
        self.lineEdit_buscarEliminar.setValidator(validacion_numero)
    
    def setupValidatorsPrecio(self):
        validacion_numero = QtGui.QRegularExpressionValidator(
            QtCore.QRegularExpression(r"\d{16}")
        )
        self.lineEdit_addPrecio.setValidator(validacion_numero)
        self.lineEdit_nuevoPrecio.setValidator(validacion_numero)
        self.lineEdit_buscarModificar.setValidator(validacion_numero)
        self.lineEdit_buscarEliminar.setValidator(validacion_numero)"""

    def limpiar_campos(self):
        self.lineEdit_addPrecio.clear()
        self.lineEdit_addServicio.clear()
        self.lineEdit_buscarModificar.clear()
        self.lineEdit_buscarEliminar.clear()
        self.lineEdit_nuevoServicio.clear()
        self.lineEdit_nuevoPrecio.clear()

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
    def mostrar_servicios(self):
        self.tabla_verServicios.setRowCount(0)
        for i, row in self.gestion_datos.servicios.iterrows():
            self.tabla_verServicios.insertRow(i)
            for j, (colname, value) in enumerate(row.items()):
                self.tabla_verServicios.setItem(i, j, QTableWidgetItem(str(value)))

    """def registrar_servicio(self):
        id_servicio = self.lineEdit_addId.text()
        nombre = self.lineEdit_addNombre.text()
        precio = self.lineEdit_addPrecio.text()
        if (
            validar_Id(id_servicio)
            and validar_Precio(precio)
            and validar_NombreCom(nombre)
        ):
            self.gestion_datos.agregar_servicio(id_servicio, nombre, precio)
            self.mostrar_servicios()
            self.show_success_dialog("Servicio registrado con éxito.")
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

    def modificar_servicio(self):
        id_servicio = self.lineEdit_.text()
        nuevos_datos = {
            "Nombre Servicio": self.lineEdit_nuevoServicio.text(),
            "Costo": self.lineEdit_nuevoPrecio.text(),
        }
        self.gestion_datos.agregar_servicio(id_servicio, nuevos_datos)
        self.mostrar_servicios()  # Actualizar la tabla de servicios

    def eliminar_servicio(self):
        id_servicio = self.lineEdit_buscarEliminar.text()
        self.gestion_datos.eliminar_servicio(id_servicio)
        self.mostrar_servicios()  # Actualizar la tabla de clientes"""


"""if __name__ == "__main__":
    app = QApplication(sys.argv)
    add = GestionClientes()
    add.show()  # Asegúrate de mostrar la ventana
    sys.exit(app.exec_())"""
