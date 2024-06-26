import time

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QPushButton
from GUI.ventanas.Caja import ControlNavegacion, Aplicacion
from GUI.ventanas.soporte_admin import AdminSoporteManager
from API.prueba import Cajero
from API.DATA import GestionDatos
from API.Validaciones import *
import subprocess


class Login(QMainWindow):
    def __init__(self, app):
        super().__init__()
        uic.loadUi(
            r"GUI\ui\Login.ui",
            self,
        )
        self.gestion_datos = GestionDatos()
        self.app = app
        # BT CLOSE POPUP
        self.pushButton_close_pupup.clicked.connect(lambda: self.frame_error.hide())
        self.cajero = Cajero()
        self.manual = (
            r"DESIGN\Manual_de_Uso_del_Sistema_de_Gestión_de_Glam_Makeup_Store.pdf"
        )
        self.pushBoton_manual.clicked.connect(self.abrir_manual)
        # HIDE ERROR
        self.frame_error.hide()

        # BT LOGIN
        self.pushButton_login.clicked.connect(self.checkFields)
        self.pushButton_login.clicked.connect(self.limpiarCampo)

        self.stylePopupError = (
            "background-color: rgb(255, 85, 127); border-radius: 5px;"
        )
        self.stylePopupOk = "background-color: rgb(255, 0, 0); border-radius: 5px;"

        buttons = self.findChildren(QPushButton)
        for button in buttons:
            button.setCursor(QCursor(Qt.PointingHandCursor))

    def limpiarCampo(self):
        self.lineEdit_user.setText("")
        self.lineEdit_password.setText("")

    def checkFields(self):
        username = self.lineEdit_user.text()
        password = self.lineEdit_password.text()

        def showMessage(message, is_error=True):
            self.frame_error.show()
            self.label_error.setText(message)
            if is_error:
                self.frame_error.setStyleSheet(self.stylePopupError)
            else:
                self.frame_error.setStyleSheet(self.stylePopupOk)

        # CHECK USER
        if not username:
            textUser = " Usuario Vacio. "
            showMessage(textUser)
        else:
            textUser = ""

        # CHECK PASSWORD
        if not password:
            textPassword = " Contraseña Vacia. "
            showMessage(textPassword)
        else:
            textPassword = ""

        # CHECK FIELDS
        if textUser + textPassword != "":
            text = textUser + textPassword
            showMessage(text)
        else:
            user_role = self.authenticate_user(username, password)
            if user_role:
                if user_role == 1:
                    self.openAdminSupportWindow("soporte")
                    self.frame_error.hide()
                elif user_role == 2:
                    self.openAdminSupportWindow("admin")
                    self.frame_error.hide()
                elif user_role == 3:
                    self.openCajaWindow()
                    self.frame_error.hide()
                else:
                    showMessage("Credenciales incorrectas")
            else:
                showMessage("Usuario o contraseña incorrecta. ")
                self.showErrorMessage("Credenciales Incorrectas")

    def showErrorMessage(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText(message)
        msg_box.setWindowTitle("Error de autenticación")
        msg_box.exec_()

    def authenticate_user(self, username, password):
        usuario_datos = self.gestion_datos.usuarios[
            self.gestion_datos.usuarios["usuario"] == username
        ]
        if not usuario_datos.empty:
            if password in usuario_datos["contraseña"].values:
                rol = usuario_datos["Rol ID"].values
                return int(rol)
            return False
        return False

    def openAdminSupportWindow(self, user_role: str):
        self.admin_soporte = AdminSoporteManager(self, user_role=user_role)
        self.admin_soporte.leer_estilos(
            self.app,
            [
                "GUI/sub_ventanas/css/admin.css",
            ],
        )
        self.admin_soporte.run()
        self.close()

    def openCajaWindow(self):
        caja = Aplicacion(self)
        caja.show()
        self.close()

    def abrir_manual(self):
        file = self.manual
        subprocess.call(["start", file], shell=True)
