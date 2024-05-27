import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ventanas.login import Ui_MainWindow

# Importa tu ventana de administrador aquí
# from windows.admin_window import AdminWindow

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def main():
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
