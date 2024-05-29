import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream

from reportesDesigner import Ui_reportes

class Ventas(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = None # plantilla de consultas de servicio y productos

class Reportes(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_reportes()
        self.ui.setupUi(self)

    def painterEvent(self, event):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # styles
    with open('C:\GLAM_MAKEUP_STORE\GUI\\forms\Soporte\components\\reportes\general.qss', 'r') as style_file:
        style_line = style_file.read()

    app.setStyleSheet(style_line)

    soporte = Reportes()
    soporte.show()

    sys.exit(app.exec_())

