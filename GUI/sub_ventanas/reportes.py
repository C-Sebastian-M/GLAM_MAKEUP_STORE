import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor

# Tipado
from typing import List

class Plantilla(QWidget):
    pass

class Servicios(Plantilla):
    pass

class Productos(Plantilla):
    pass

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


class Ventas(QWidget, CBackground):
    def __init__(self):
        super().__init__()

        self.ui = None # plantilla de consultas de servicio y productos

class Inventario(QWidget, CBackground):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(r"C:\GLAM_MAKEUP_STORE\GUI\sub_ventanas\ui\reportes\inventarioPanelDesigner.ui", self)

    def inicializar(self):
        pass

class ReportePanel(QWidget, CBackground):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\GLAM_MAKEUP_STORE\GUI\sub_ventanas\ui\reportes\reportesDesigner.ui", self)

class Admin(QMainWindow, CBackground):
    def __init__(self) -> None:
        super(QMainWindow, self).__init__()
        uic.loadUi(r"C:\GLAM_MAKEUP_STORE\GUI\sub_ventanas\ui\reportes\adminDesigner.ui", self)

        self.cerrarBtn.clicked.connect(QApplication.instance().quit)

        self.inicializar(es_admin=False)

    def inicializar(self, es_admin: str | bool) -> None:
        if es_admin or es_admin == "admin":
            self.setWindowTitle("Administrador")
            self.title.setText("Admin")
            self.roleBtn.setText("Reporte\nDiario")
            return None

        self.setWindowTitle("Soporte")
        self.title.setText("Soporte")
        self.roleBtn.setText("Administrar\nusuario")

class AdminManager(QMainWindow):
    def __init__(self) -> None:
        super(QMainWindow, self).__init__()
        self.stack = []

        # Inicializando ventanas
        self.admin = Admin()
        self.reportePanel = ReportePanel()
        self.inventarioPanel = Inventario()

        # Insertando al stack
        self.widgets_stack = QStackedWidget(self)
        self.widgets_stack.addWidget(self.admin)
        self.widgets_stack.addWidget(self.reportePanel)
        self.widgets_stack.addWidget(self.inventarioPanel)

        # asignando el widget central
        self.setCentralWidget(self.widgets_stack)
        # set actual
        self.widgets_stack.setCurrentWidget(self.admin)

        # conexiones
        self.inicializar()

    def inicializar(self):
        self.resize(800, 600)
        self.conexiones()

    def conexiones(self):
        # Main
        self.admin.reportesBtn.clicked.connect(self.ventana_reportes)

        # Panel de reportes
        self.reportePanel.volverBtn.clicked.connect(self.anterior)
        self.reportePanel.inventarioBtn.clicked.connect(self.ventana_inventario)

        # Panel de inventario
        self.inventarioPanel.volverBtn.clicked.connect(self.anterior)

    def ventana_reportes(self):
        self.widgets_stack.setCurrentWidget(self.reportePanel)
        self.stack.append(self.admin)

    def ventana_inventario(self):
        self.widgets_stack.setCurrentWidget(self.inventarioPanel)
        self.stack.append(self.reportePanel)

    def anterior(self):
        anterior = self.admin

        if self.stack:
            anterior = self.stack.pop()
        self.widgets_stack.setCurrentWidget(anterior)

    def leer_estilos(self, app: QApplication, paths: List[str]) -> None: # Toca organizar esta funcion
        for path in paths:
            with open(path, 'r') as style_file:
                style_line = style_file.read()

        app.setStyleSheet(style_line)
        style_file.close()

    def run(self):
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # styles
    admin = AdminManager()
    admin.leer_estilos(app, [
        "C:\GLAM_MAKEUP_STORE\GUI\sub_ventanas\qss\\reportes\\admin.qss",
    ])

    admin.run()

    sys.exit(app.exec_())
