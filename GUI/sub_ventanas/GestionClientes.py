from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets
import sys


class GestionClientes(QMainWindow):
    def __init__(self):
        super(GestionClientes, self).__init__()
        loadUi(
            r"GUI\sub_ventanas\ui\gestion_clientes\GestionClientes.ui",
            self,
        )

        self.pushButton_menu.clicked.connect(self.mover_menu)

        # Botones
        self.pushButton_actualizar.clicked.connect(self.mostrar_clientes)
        self.pushButton_add.clicked.connect(self.registrar_cliente)
        self.pushButton_guardarInfo.clicked.connect(self.modificar_cliente)
        self.pushButton_eliminar.clicked.connect(self.eliminar_cliente)

        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # Mas botones
        self.pushButton_verClientes.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pagina_consulta)
        )
        self.pushButton_addCliente.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pagina_add)
        )
        self.pushButton_modificarCliente.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pagina_modificar)
        )
        self.pushButton_eliminarCliente.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pagina_eliminar)
        )

        # Ancho columna adaptable
        self.tabla_verClientes.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.tabla_eliminarClientes.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    def mousePressEvent(self, event):
        self.click_position = event.globalPos()

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

    # Acá se configura la base de datos
    def mostrar_clientes(self):
        None

    def registrar_cliente(self):
        None

    def modificar_cliente(self):
        None

    def eliminar_cliente(self):
        None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    add = GestionClientes()
    add.show()  # Asegúrate de mostrar la ventana
    sys.exit(app.exec_())
