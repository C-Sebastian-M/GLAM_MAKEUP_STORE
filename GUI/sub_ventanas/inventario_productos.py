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

# Ventana Modificar producto
class ModificarProducto(QMainWindow, CBackground):
    def __init__(self):
        super().__init__()
        uic.loadUi(
            r"GUI\sub_ventanas\ui\inventario_productos\modificar_producto.ui",
            self,
        )
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    crear_producto = CrearProducto()
    modificar_producto = ModificarProducto()
    crear_producto.show()
    modificar_producto.show()
    sys.exit(app.exec_())