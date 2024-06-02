from PyQt5 import uic

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox
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
        
# Ventana Inventario de productos
class InventarioProductos(QMainWindow, CBackground):
    def __init__(self):
        super().__init__()
        uic.loadUi(
            r"GUI\sub_ventanas\ui\inventario_productos\inventario_productos.ui",
            self,
        )


# Ventana Crear producto
class CrearProducto(QMainWindow, CBackground):
    def __init__(self):
        super().__init__()
        uic.loadUi(
            r"GUI\sub_ventanas\ui\inventario_productos\crear_producto.ui",
            self,
        )
        self.setupValidators()
    
    def setupValidators(self):
        validacion_numero = QtGui.QIntValidator(0, 999999999)
        self.precio_adquisicion_text.setValidator(validacion_numero)
        

# Ventana Modificar producto
class ModificarProducto(QMainWindow, CBackground):
    def __init__(self):
        super().__init__()
        uic.loadUi(
            r"GUI\sub_ventanas\ui\inventario_productos\modificar_producto.ui",
            self,
        )
    
        self.seleccionar_producto_combobox.addItems(["Producto1", "Producto2", "Producto3", "Producto4"])
        self.seleccionar_producto_combobox.currentIndexChanged.connect(self.abrir_modificar_atributos_producto)
    
    def abrir_modificar_atributos_producto(self):
        producto_seleccionado = self.seleccionar_producto_combobox.currentText()
        self.modificar_atributos = ModificarAtributosProducto(producto_seleccionado)
        self.modificar_atributos.show()

# Ventana Modificar atributos especificos de atributo
class ModificarAtributosProducto(QMainWindow, CBackground):
    def __init__(self, text):
        super().__init__()
        uic.loadUi(
            r"GUI\sub_ventanas\ui\inventario_productos\modificar_atributos_especificos.ui",
            self,
        )
        
        self.label_producto_seleccionado.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ModificarProducto()
    main_window.show()
    sys.exit(app.exec_())