import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt

from soporteDesigner import Ui_SuppWindow

# main page
class Soporte(QMainWindow):
    def __init__(self) -> None:
        super(QMainWindow, self).__init__()

        self.ui = Ui_SuppWindow()
        self.ui.setupUi(self)

        is_admin = False
        if is_admin:
            pass # add btn for admins
        else:
            pass # add btn for no admins

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing)

        brocha1 = QBrush(QColor(212, 132, 180), Qt.SolidPattern)
        brocha2 = QBrush(QColor(228, 156, 198), Qt.SolidPattern)
        brocha3 = QBrush(QColor(235, 188, 220), Qt.SolidPattern)

        # Dibujando circulos abajo
        painter.setBrush(brocha3)
        painter.drawEllipse(140, 530, 200, 200)

        painter.setBrush(brocha2)
        painter.drawEllipse(40, 480, 200, 200)

        painter.setBrush(brocha1)
        painter.drawEllipse(-70, 440, 200, 200)

        # Dibujando circulos arriba
        painter.setBrush(brocha3)
        painter.drawEllipse(440, -140, 200, 200)

        painter.setBrush(brocha2)
        painter.drawEllipse(550, -100, 200, 200)

        painter.setBrush(brocha1)
        painter.drawEllipse(700, -70, 200, 200)

        painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # styles
    with open('C:\GLAM_MAKEUP_STORE\GUI\Soporte\stylesheet.qss', 'r') as style_file:
        style_line = style_file.read()

    app.setStyleSheet(style_line)

    soporte = Soporte()
    soporte.show()

    sys.exit(app.exec_())
