from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QComboBox
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


class ModificarCliente(QMainWindow, CBackground):
    def __init__(self):
        super().__init__()
        uic.loadUi(
            r"GUI\sub_ventanas\ui\gestion_clientes\ModificarClientes.ui",
            self,
        )
        self.pushButton_2.clicked.connect(self.obtener_info)
        self.comboBoxClientes = self.findChild(QComboBox, "comboBoxClientes")

        # Asumiendo que el formulario a esconder/mostrar es un QWidget con el objectName "formulario"
        self.formulario = self.findChild(QWidget, "FormularioWidget")

        # Conecta el combobox a la función que manejará la visibilidad del formulario
        self.comboBoxClientes.currentIndexChanged.connect(self.toggleFormulario)

        # Inicialmente oculta el formulario si no hay ningún cliente seleccionado
        self.formulario.setVisible(False)

    def toggleFormulario(self):
        # Obtén el índice actual del combobox
        index = self.comboBoxClientes.currentIndex()

        # Si el índice es válido (es decir, no es -1), muestra el formulario, de lo contrario escóndelo
        if index != -1:
            self.formulario.setVisible(True)
        else:
            self.formulario.setVisible(False)

    
    def obtener_info(self):
        nombre = self.nombreLineEdit.text()
        telefono = self.telefonoLineEdit.text()    
        print(f"Nombre: {nombre}, Teléfono: {telefono}")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    add = CrearCliente()
    obt = ModificarCliente()
    add.guardar_cliente()
    obt.obtener_info()
    obt.show()
    add.show()  # Asegúrate de mostrar la ventana
    sys.exit(app.exec_())
