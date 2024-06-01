from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from GUI.ventanas.Caja_X import Ui_Caja
from GUI.ventanas.soporte_admin import AdminSoporteManager

class Login(QMainWindow):
    def __init__(self, app):
        super().__init__()
        uic.loadUi(
            r"GUI\ui\Login.ui",
            self,
        )
        self.app = app
        # BT CLOSE POPUP
        self.pushButton_close_pupup.clicked.connect(lambda: self.frame_error.hide())

        # HIDE ERROR
        self.frame_error.hide()

        # BT LOGIN
        self.pushButton_login.clicked.connect(self.checkFields)
        self.pushButton_login.clicked.connect(self.limpiarCampo)
        self.stylePopupError = "background-color: rgb(255, 85, 127); border-radius: 5px;"
        self.stylePopupOk = "background-color: rgb(255, 0, 0); border-radius: 5px;"

    def limpiarCampo(self):
        self.lineEdit_user.clear()
        self.lineEdit_password.clear()

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
        else:
            textUser = ""

        # CHECK PASSWORD
        if not password:
            textPassword = " Contraseña Vacia. "
        else:
            textPassword = ""

        # CHECK FIELDS
        if textUser + textPassword != "":
            text = textUser + textPassword
            showMessage(text)
        else:
            user_role = self.authenticate_user(username, password)
            if user_role:
                if user_role == "admin" or user_role == "soporte":
                    self.openAdminSupportWindow(user_role)
                elif user_role == "caja":
                    self.openCajaWindow()
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
        # Aquí deberías tener la lógica de autenticación, por ejemplo, verificar las credenciales en una base de datos
        if username == "admin" and password == "admin":
            return "admin"
        elif username == "caja" and password == "caja":
            return "caja"
        elif username == "soporte" and password == "soporte":
            return "soporte"
        else:
            return None

    def openAdminSupportWindow(self, user_role: str):
        self.admin_soporte = AdminSoporteManager(self,user_role=user_role)
        self.admin_soporte.leer_estilos(self.app, [
            "GUI\sub_ventanas\css\\admin.css",
        ])
        self.admin_soporte.run()
        self.close()

    def openCajaWindow(self):
        self.caja_window = QMainWindow()
        self.ui_caja = Ui_Caja()
        self.ui_caja.setupUi(self.caja_window)
        self.caja_window.show()
        self.close()