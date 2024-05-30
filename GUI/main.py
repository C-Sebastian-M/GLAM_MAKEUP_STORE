import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ventanas.login import Ui_MainWindow
from ventanas.Caja import Ui_Caja
from ventanas.soporte_admin import AdminSoporteManager

class LoginWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_login.clicked.connect(self.checkFields)
        self.setMaximumSize(self.size())

    def checkFields(self):
        username = self.ui.lineEdit_user.text()
        password = self.ui.lineEdit_password.text()

        user_role = self.authenticate_user(username, password)

        if user_role == "admin" or user_role == "soporte":
            self.openAdminSupportWindow(user_role)
        elif user_role == "caja":
            self.openCajaWindow()
        else:
            self.showErrorMessage("Credenciales incorrectas")

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
        self.admin_soporte = AdminSoporteManager(user_role=user_role)
        self.admin_soporte.leer_estilos(self.app, [
            "GUI/sub_ventanas/css/admin.css",
        ])
        self.admin_soporte.run()
        self.close()

    def openCajaWindow(self):
        self.caja_window = QMainWindow()
        self.ui_caja = Ui_Caja()
        self.ui_caja.setupUi(self.caja_window)
        self.caja_window.show()
        self.close()

    def showErrorMessage(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText(message)
        msg_box.setWindowTitle("Error de autenticación")
        msg_box.exec_()


def main():
    app = QApplication(sys.argv)

    login_window = LoginWindow(app)
    login_window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
