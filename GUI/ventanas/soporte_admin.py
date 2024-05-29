from typing import List

from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from sub_ventanas.reportes import AdminSoporte, ReportePanel, Inventario

class AdminSoporteManager(QMainWindow):
    def __init__(self, user_role: str) -> None: # pass role as argument (soporte or admin)
        super(QMainWindow, self).__init__()
        if not user_role:
            raise TypeError("El rol de usuario no puede estar vacio.")

        self.stack = []

        # Inicializando ventanas
        self.admin_soporte = AdminSoporte(user_role)
        self.reportePanel = ReportePanel()
        self.inventarioPanel = Inventario()

        # Insertando al stack
        self.widgets_stack = QStackedWidget(self)
        self.widgets_stack.addWidget(self.admin_soporte)
        self.widgets_stack.addWidget(self.reportePanel)
        self.widgets_stack.addWidget(self.inventarioPanel)

        # asignando el widget central
        self.setCentralWidget(self.widgets_stack)
        # set actual
        self.widgets_stack.setCurrentWidget(self.admin_soporte)

        # conexiones
        self.inicializar()

    def inicializar(self):
        self.resize(800, 600)
        self.conexiones()

        buttons = self.findChildren(QPushButton)
        for button in buttons:
            button.setCursor(QCursor(Qt.PointingHandCursor))

    def conexiones(self):
        # Main
        self.admin_soporte.reportesBtn.clicked.connect(self.ventana_reportes)

        # Panel de reportes
        self.reportePanel.volverBtn.clicked.connect(self.anterior)
        self.reportePanel.inventarioBtn.clicked.connect(self.ventana_inventario)


        # Panel de inventario
        self.inventarioPanel.volverBtn.clicked.connect(self.anterior)

    def ventana_reportes(self):
        self.widgets_stack.setCurrentWidget(self.reportePanel)
        self.stack.append(self.admin_soporte)

    def ventana_inventario(self):
        self.widgets_stack.setCurrentWidget(self.inventarioPanel)
        self.stack.append(self.reportePanel)

    def anterior(self):
        anterior = self.admin_soporte

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
