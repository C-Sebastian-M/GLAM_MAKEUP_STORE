from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor
import sys


class CBackground:
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


class GestionClientes(QMainWindow, CBackground):
    def __init__(self):
        super().__init__()
        uic.loadUi(
            r"GUI\sub_ventanas\ui\gestion_clientes\GestionClientes.ui",
            self,
        )


class CrearCliente(QMainWindow, CBackground):
    def __init__(self):
        super().__init__()
        uic.loadUi(
            r"GUI\sub_ventanas\ui\gestion_clientes\CrearCliente.ui",
            self,
        )
        self.BotonGuardar.clicked.connect(self.guardar_cliente)
        
    def guardar_cliente(self):
        # Obtener los datos de los campos de entrada
        cedula = self.IngresoCedula.text()
        nombre = self.IngresoNombre.text()
        telefono = self.IngresoTelefono.text()
        print(f"Nombre: {nombre}, Cédula: {cedula}, Teléfono: {telefono}")

    def inicializar(self):
        pass



class AdminSoporte(QMainWindow, CBackground):
    def __init__(self, role: str) -> None:
        super(QMainWindow, self).__init__()
        self.role = role

        uic.loadUi(
            r"GUI\sub_ventanas\ui\reportes\adminDesigner.ui",
            self,
        )

        self.cerrarBtn.clicked.connect(QApplication.instance().quit)

        self.inicializar(
            is_admin=True if self.role.strip().lower() == "admin" else False
        )

    def inicializar(self, is_admin: str | bool) -> None:
        if is_admin or is_admin == "admin":
            self.setWindowTitle("Administrador")
            self.title.setText("Admin")
            self.roleBtn.setText("Reporte\nDiario")
            return

        self.setWindowTitle("Admin")
        self.title.setText("Soporte")
        self.roleBtn.setText("Administrar\nusuario")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    add = CrearCliente()
    add.guardar_cliente()
    add.show()  # Asegúrate de mostrar la ventana
    sys.exit(app.exec_())
