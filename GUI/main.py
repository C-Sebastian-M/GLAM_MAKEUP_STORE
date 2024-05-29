import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ventanas.login import Ui_MainWindow # Asegúrate de que esta importación es correcta
from ventanas.Caja import Ui_Caja, Sele_Compra, Sele_Cliente, Cli_Curr # Importa tu ventana de caja
# Importa tu ventana de caja
from ventanas.soporte_admin import Ui_soporte_admin

# Importa otras ventanas según sea necesario
# from ventanas.admin_window import Ui_Admin
# from ventanas.soporte_window import Ui_Soporte

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_login.clicked.connect(self.checkFields)
        self.setMaximumSize(self.size())

    def checkFields(self):
        username = self.ui.lineEdit_user.text()
        password = self.ui.lineEdit_password.text()

        user_role = self.authenticate_user(username, password)

        if user_role == "admin":
            self.openAdminWindow()
        elif user_role == "caja":
            self.openCajaWindow()
        elif user_role == "soporte":
            self.openSoporteWindow()
        else:
            self.showErrorMessage("Credenciales incorrectas")

    def authenticate_user(self, username, password):
        # Aquí deberías tener la lógica de autenticación, por ejemplo, verificar las credenciales en una base de datos
        if username == "admin" and password == "admin":
            return "admin"
        elif username == "caja" and password == "caja":
            return "caja"
        elif username == "soporte" and password == "soporte_password":
            return "soporte"
        else:
            return None

    def openAdminWindow(self):
        self.soporte_admin_window = QMainWindow()
        self.ui_soporte_admin = Ui_soporte_admin()
        self.ui_soporte_admin.setupUi(self.soporte_admin_window)
        self.soporte_admin_window.show()
        self.close()

    def openCajaWindow(self):
        self.caja_window = QMainWindow()
        self.ui_caja = Ui_Caja()
        self.ui_caja.setupUi(self.caja_window)
        self.caja_window.show()
        self.close()

    def openSoporteWindow(self):
        # Abre la ventana de soporte
        pass  # Implementa esto según tu ventana de soporte

    def showErrorMessage(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText(message)
        msg_box.setWindowTitle("Error de autenticación")
        msg_box.exec_()


    
def main():
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
