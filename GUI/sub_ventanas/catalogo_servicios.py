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

from GUI.sub_ventanas.utils.css import CBackground

class GestionServicios(QMainWindow, CBackground):
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
        self.pushButton_mostrarModificar.clicked.connect(self.mostrar_servicioModificar)
        self.pushButton_mostrarEliminar.clicked.connect(self.mostrar_servicioEliminar)
        # self.pushButton_add.clicked.connect(self.registrar_servicio)
        self.pushButton_guardarInfo.clicked.connect(self.modificar_servicio)
        self.pushButton_eliminar.clicked.connect(self.eliminar_servicio)
        self.pushButton_modificar.clicked.connect(self.mostar_formulario)

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
        self.tableWidget_eliminarServicio.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.tableWidget_modificar.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.setupValidatorsId()
        self.setupValidatorsPrecio()
        self.frame_formulario.hide()
        df = pd.read_excel("registros.xlsx", sheet_name="Servicios")
        servicios = df["ID servicio"].astype(str).tolist()
        self.modelo_datos = QStringListModel(servicios)
        self.completer = QCompleter(self.modelo_datos, self)
        self.completer.setCaseSensitivity(False)  # Ignorar mayúsculas y minúsculas
        self.completer.setFilterMode(
            Qt.MatchContains
        )  # Coincidir con cualquier parte del texto
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.completer.setPopup(self.listView_buscar)
        self.completer.setPopup(self.listView_eliminar)
        self.lineEdit_modificar.setCompleter(self.completer)
        self.lineEdit_buscarEliminar.setCompleter(self.completer)

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    def setupValidatorsId(self):
        validacion_numero = QtGui.QRegularExpressionValidator(
            QtCore.QRegularExpression(r"\d{12}")
        )
        self.lineEdit_idServicio.setValidator(validacion_numero)
        self.lineEdit_nuevoId.setValidator(validacion_numero)
        self.lineEdit_modificar.setValidator(validacion_numero)
        self.lineEdit_buscarEliminar.setValidator(validacion_numero)

    def setupValidatorsPrecio(self):
        validacion_numero = QtGui.QRegularExpressionValidator(
            QtCore.QRegularExpression(r"\d{16}")
        )
        self.lineEdit_addPrecio.setValidator(validacion_numero)
        self.lineEdit_nuevoPrecio.setValidator(validacion_numero)
        self.lineEdit_modificar.setValidator(validacion_numero)
        self.lineEdit_buscarEliminar.setValidator(validacion_numero)

    def limpiar_campos(self):
        self.lineEdit_nuevoId.clear()
        self.lineEdit_idServicio.clear()
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

    # Acá se configura la base de datos
    def mostrar_servicios(self):
        self.tabla_verServicios.setRowCount(0)
        for i, row in self.gestion_datos.servicios.iterrows():
            self.tabla_verServicios.insertRow(i)
            for j, (colname, value) in enumerate(row.items()):
                self.tabla_verServicios.setItem(i, j, QTableWidgetItem(str(value)))

    def mostrar_servicioModificar(self):
        self.tableWidget_modificar.setRowCount(0)
        for i, row in self.gestion_datos.servicios.iterrows():
            self.tableWidget_modificar.insertRow(i)
            for j, (colname, value) in enumerate(row.items()):
                self.tableWidget_modificar.setItem(i, j, QTableWidgetItem(str(value)))

    def mostrar_servicioEliminar(self):
        self.tableWidget_eliminarServicio.setRowCount(0)
        for i, row in self.gestion_datos.servicios.iterrows():
            self.tableWidget_Eliminar.insertRow(i)
            for j, (colname, value) in enumerate(row.items()):
                self.tableWidget_Eliminar.setItem(i, j, QTableWidgetItem(str(value)))

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

    # def registrar_servicio(self):
    #  id_servicio = self.lineEdit_addId.text()
    #  nombre = self.lineEdit_addNombre.text()
    #   precio = self.lineEdit_addPrecio.text()
    #   if (
    #       validar_Id(id_servicio)
    #       and validar_Precio(precio)
    #       and validar_NombreCom(nombre)
    #   ):
    #       self.gestion_datos.agregar_servicio(id_servicio, nombre, precio)
    #       self.mostrar_servicios()
    #       self.label_aviso.setText("Servicio registrado con éxito")
    #       self.show_success_dialog("Servicio registrado con éxito.")
    #       self.limpiar_campos()
    #   else:
    #       self.showErrorMessage(
    #           "Error en los datos ingresados. Por favor, verifica la información."
    #       )

    def validar_existencia(self):
        # Los campos para validar son:
        if self.lineEdit_modificar.text():
            idBuscarServicio = self.lineEdit_modificar.text()
            if (
                idBuscarServicio in self.gestion_datos.servicios["ID servicio"].values
                or int(idBuscarServicio) in self.gestion_datos.servicios["ID servicio"]
            ):
                return True
            else:
                return False
        else:
            self.aviso_modificar.setText(
                "Campo Vacio. Por favor ingrese la información correspondiente."
            )

    def mostar_formulario(self, servicio):
        servicio = self.validar_existencia()
        if servicio:
            self.frame_formulario.show()
        else:
            self.showErrorMessage(
                "Error en los datos ingresados. Por favor, verifica la información."
            )
            self.aviso_modificar.setText(
                "Error en los datos ingresados. Por favor, verifica la información."
            )

    def modificar_servicio(self):
        id_servicio = int(self.lineEdit_.text())
        nuevos_datos = {
            "Nombre Servicio": self.lineEdit_nuevoServicio.text(),
            "Costo": self.lineEdit_nuevoPrecio.text(),
        }
        self.gestion_datos.agregar_servicio(id_servicio, nuevos_datos)
        self.mostrar_servicios()  # Actualizar la tabla de servicios

    def eliminar_servicio(self):
        id_servicio = self.lineEdit_buscarEliminar.text()
        self.gestion_datos.eliminar_servicio(id_servicio)
        self.mostrar_servicios()  # Actualizar la tabla de clientes
