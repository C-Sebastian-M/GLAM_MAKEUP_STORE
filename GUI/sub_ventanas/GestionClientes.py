from PyQt5.uic import loadUi
import pandas as pd
from PyQt5.QtWidgets import (
    QMainWindow,
    QHeaderView,
    QTableWidgetItem,
    QMessageBox,
    QCompleter,
    QTableWidget,
)
from PyQt5.QtCore import QPropertyAnimation, Qt, QStringListModel
from PyQt5 import QtCore, QtWidgets, QtGui
from API.DATA import GestionDatos
from API.Validaciones import *
from API.prueba import Cajero
from DATA.database import DatabaseManager
from GUI.sub_ventanas.custom.utils.css import CBackground


class GestionClientes(QMainWindow, CBackground):
    def __init__(self):
        super(GestionClientes, self).__init__()
        loadUi(
            r"GUI\sub_ventanas\ui\gestion_clientes\GestionClientes.ui",
            self,
        )
        self.gestion_datos = GestionDatos()
        self.db_manager = DatabaseManager(
            host="localhost",
            user="root",
            password="3245619850",
            database="glam_makeup_store",
        )
        self.db_manager.connect()
        self.cajero = Cajero()
        self.mostrar_clientes()
        self.mostrar_clientesModificar()
        self.mostrar_clientesEliminar()
        self.pushButton_menu.clicked.connect(self.mover_menu)
        # Botones
        self.pushButton_actualizar.clicked.connect(self.mostrar_clientes)
        self.pushButton_mostrarModificar.clicked.connect(self.mostrar_clientesModificar)
        self.pushButton_mostrarEliminar.clicked.connect(self.mostrar_clientesEliminar)
        self.pushButton_add.clicked.connect(self.registrar_cliente)
        self.pushButton_guardarInfo.clicked.connect(self.modificar_cliente)
        self.pushButton_eliminar.clicked.connect(self.eliminar_cliente)
        self.pushButton_modificar.clicked.connect(self.mostrar_formulario)

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

        self.tableWidget_Eliminar.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.tableWidget_modificar.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.setupValidators()
        self.frame_formulario.hide()
        df = pd.read_excel("registros.xlsx", sheet_name="Clientes")
        cedulas = df["Cedula"].astype(str).tolist()
        self.modelo_datos = QStringListModel(cedulas)
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

    def setupValidators(self):
        self.setValidator(self.lineEdit_addCedula, r"\d{9,10}")
        self.setValidator(self.lineEdit_nuevaCedula, r"\d{9,10}")
        self.setValidator(self.lineEdit_buscarEliminar, r"\d{9,10}")
        self.setValidator(self.lineEdit_modificar, r"\d{9,10}")
        self.setValidator(self.lineEdit_addTelefono, r"\d{0,16}")

    def setValidator(self, lineEdit, pattern):
        validator = QtGui.QRegularExpressionValidator(
            QtCore.QRegularExpression(pattern)
        )
        lineEdit.setValidator(validator)

    def limpiar_campos(self):
        self.lineEdit_addTelefono.clear()
        self.lineEdit_addCedula.clear()
        self.lineEdit_addNombre.clear()
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

    def showErrorMessage(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText(message)
        msg_box.setWindowTitle("Error")
        msg_box.exec_()

    def show_success_dialog(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(message)
        msg_box.setWindowTitle("Éxito")
        msg_box.exec_()

    # Acá se configura la base de datos
    def mostrar_clientes(self):
        tableR: QTableWidget = self.tabla_verClientes
        tableM: QTableWidget = self.tableWidget_modificar
        registros, columnas = self.db_manager.obtener_tablaCliente("cliente")
        if registros:
            tableR,tableM.setRowCount(len(registros))
            tableR,tableM.setColumnCount(len(registros[0]))
            tableR,tableM.setHorizontalHeaderLabels(columnas)
            for i, row in enumerate(registros):
                for j, datos in enumerate(row):
                    tableR,tableM.setItem(i, j, QTableWidgetItem(str(datos)))
        else:
            tableR,tableM.clear()

    def registrar_cliente(self):
        cedula = self.lineEdit_addCedula.text()
        nombre = self.lineEdit_addNombre.text()
        telefono = self.lineEdit_addTelefono.text()
        if (
            validar_Cedula(cedula)
            and validacion_Telefono(telefono)
            and validar_NombreCom(nombre)
        ):

            self.mostrar_clientes()
            self.show_success_dialog("Cliente registrado con éxito.")
            self.aviso_add.setText("Cliente registrado con éxito.")
            self.limpiar_campos()
            self.frame_formulario.hide()
        else:
            self.showErrorMessage(
                "Error en los datos ingresados. Por favor, verifica la información."
            )
            self.aviso_add.setText(
                "Error en los datos ingresados. Por favor, verifica la información."
            )

    def validar_existencia(self):
        # Los campos para validar son:
        if self.lineEdit_modificar.text():
            cedulaBuscarCliente = int(self.lineEdit_modificar.text())
            if (
                str(cedulaBuscarCliente)
                in str(self.gestion_datos.clientes["Cedula"].values)
                or cedulaBuscarCliente in self.gestion_datos.clientes["Cedula"].values
            ):
                return True
            else:
                return False
        else:
            self.aviso_modificar.setText(
                "Campo Vacio. Por favor ingrese la información correspondiente."
            )

    def mostrar_formulario(self):
        cedula = self.validar_existencia()
        if cedula:
            self.frame_formulario.show()
            self.aviso_modificar.setText("")
        else:
            self.showErrorMessage(
                "Cédula Inexistente. Por favor, verifica la información."
            )
            self.aviso_modificar.setText(
                "Cédula Inexistente. Por favor, verifica la información."
            )

    def modificar_cliente(self):
        cedulaBuscarCliente = int(self.lineEdit_modificar.text())
        if str(cedulaBuscarCliente) in self.gestion_datos.clientes["Cedula"].values:
            datos_cliente = self.gestion_datos.clientes[
                self.gestion_datos.clientes["Cedula"] == str(cedulaBuscarCliente)
            ]
        elif cedulaBuscarCliente in self.gestion_datos.clientes["Cedula"].values:
            datos_cliente = self.gestion_datos.clientes[
                self.gestion_datos.clientes["Cedula"] == cedulaBuscarCliente
            ]
        # print(datos_cliente)
        nuevaCedula = self.lineEdit_nuevaCedula.text()
        nuevoNombre = self.lineEdit_nuevoNombre.text()
        nuevoTelefono = self.lineEdit_nuevoTelefono.text()
        if not datos_cliente.empty:
            if self.cajero.modificar_cliente(
                nuevaCedula,
                nuevoNombre,
                nuevoTelefono,
                cedulaBuscarCliente,
            ):
                self.mostrar_clientes()  # Actualizar la tabla de clientes
                self.show_success_dialog("Cliente modificado correctamente")
                self.aviso_modificar.setText("Cliente modificado correctamente")
                self.limpiar_campos()
                self.frame_formulario.hide()
            else:
                self.showErrorMessage(
                    "Error en los datos ingresados. Por favor, verifica la información."
                )
                self.aviso_add.setText(
                    "Error en los datos ingresados. Por favor, verifica la información."
                )
        else:
            self.showErrorMessage(
                "Error en los datos ingresados. Por favor, verifica la información."
            )
            self.aviso_eliminar.setText(
                "Error en los datos ingresados. Por favor, verifica la información."
            )

    def eliminar_cliente(self):
        if not self.lineEdit_buscarEliminar.text():
            self.aviso_eliminar.setText(
                "Cédula Inexistente. Por favor, verifica la información."
            )
            return self.showErrorMessage(
                "Cédula Inexistente. Por favor, verifica la información."
            )
        cedula = int(self.lineEdit_buscarEliminar.text())
        eliminado = self.gestion_datos.eliminar_clientes(cedula)
        if cedula:
            if (
                eliminado
            ):  # No elimina nada, solo añadí el if para usar los valores de retorno del metodo y mostrar las ventanas emergentes
                self.mostrar_clientes()
                self.show_success_dialog("Cliente eliminado correctamente")
                self.aviso_eliminar.setText("Cliente eliminado correctamente")
                self.limpiar_campos()
            else:
                self.showErrorMessage(
                    "Error en los datos ingresados. Por favor, verifica la información."
                )
                self.aviso_eliminar.setText(
                    "Error en los datos ingresados. Por favor, verifica la información."
                )
