import sys
from PyQt5.QtWidgets import QApplication
from GUI.ventanas.login import Login

class Main:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.login_window = Login(self.app)

    def run(self):
        self.login_window.show()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    app = Main()
    app.run()
