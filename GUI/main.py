import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ventanas.login import Ui_MainWindow  # Asegúrate de que esta importación es correcta
from ventanas.Caja import Ui_Caja, Sele_Compra, Sele_Cliente # Importa tu ventana de caja

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
        if username == "admin" and password == "admin_password":
            return "admin"
        elif username == "caja" and password == "caja":
            return "caja"
        elif username == "soporte" and password == "soporte_password":
            return "soporte"
        else:
            return None

    def openAdminWindow(self):
        # Abre la ventana de administrador
        pass  # Implementa esto según tu ventana de administrador

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

class Caja(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cajaC = Ui_Caja()
        self.cajaC.setupUi(self)
        self.cajaC.PushButton.clicked.connect(self.report) #metodo para añadir reporte, por ahora vacio
        self.cajaC.pushButton_2.clicked.connect(self.exit) #metodo para salir del programa
        self.cajaC.PushButton_3.clicked.connect(self.OpenWindowSele) #metodo par avanzar a la siguient pagina

    def report(self):
        pass

    def exit(self):
        self.close()

    def OpenWindowSele(self):
        self.SeleW = QMainWindow()
        self.ui_sele = Sele_Compra()
        self.ui_sele.setupUi(self.SeleW)
        self.seleW.show()
        self.close()

class SeleCompra(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Sele=Sele_Compra()
        self.Sele.setupUi(self)
        self.Sele.pushButtonC.clicked.connect(self.Buy)
        self.Sele.pushButtonC_2.clicked.connect(self.cancel)
    def Buy(self):
        pass

    def cancel(self):
        self.backC = QMainWindow()
        self.ui_backC = Ui_Caja()
        self.ui_backC.setupUi(self.backC)
        self.backC.show()
        
class SeleCliente(QMainWindow):
    def __init__(self):
        pass
    
def main():
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
