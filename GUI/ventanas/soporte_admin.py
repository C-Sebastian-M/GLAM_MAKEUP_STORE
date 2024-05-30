from typing import List

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

<<<<<<< HEAD
from sub_ventanas.reportes import AdminSoporte, ReportePanel, Inventario
from sub_ventanas.GestionClientes import GestionClientes, CrearCliente
=======
# reportes
from sub_ventanas.reportes import (
    CBackground, ReportePanel, 
    InventarioPanel, Inventario, 
    Ventas
)
# gestion de clientes
# import

class AdminSoporte(QMainWindow, CBackground):
    def __init__(self, role: str) -> None:
        super(QMainWindow, self).__init__()
        self.role = role

        uic.loadUi(r"GUI\sub_ventanas\ui\reportes\adminDesigner.ui", self)

        self.inventarioPanel = InventarioPanel()
        self.inventario = Inventario("Inventario", [])
        self.ventas = Ventas("Ventas", [])

        self.widgets_stack = QStackedWidget(self)
        self.widgets_stack.addWidget(self.inventarioPanel)
        self.widgets_stack.addWidget(self.inventario)
        self.widgets_stack.addWidget(self.ventas)

        self.cerrarBtn.clicked.connect(QApplication.instance().quit)

        self.inicializar(is_admin = True if self.role.strip().lower() == "admin" else False)

    def inicializar(self, is_admin: str | bool) -> None:
        self.resize(800, 600)

        if is_admin or is_admin == "admin":
            self.setWindowTitle("Administrador")
            self.title.setText("Admin")
            self.roleBtn.setText("Reporte\nDiario")

            return None

        self.setWindowTitle("Soporte")
        self.title.setText("Soporte")
        self.roleBtn.setText("Administrar\nusuario")
>>>>>>> 92812e82879a4089e69fed641d8b074b70ec2e2e


class AdminSoporteManager(QMainWindow):
    def __init__(
        self, user_role: str
    ) -> None:  # pass role as argument (soporte or admin)
        super(QMainWindow, self).__init__()
        if not user_role:
            raise TypeError("El rol de usuario no puede estar vacio.")
<<<<<<< HEAD
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
=======
        
        self.role = user_role

>>>>>>> 92812e82879a4089e69fed641d8b074b70ec2e2e
        self.stack = []

        ######################## Inicializando/conectando ventanas de reportes ########################
        self.admin_soporte = AdminSoporte(self.role)
        self.reportePanel = ReportePanel()
<<<<<<< HEAD
        self.inventarioPanel = Inventario()
        self.gestionPanel = GestionClientes()
        self.addClientePanel = CrearCliente()
=======
        self.inventarioPanel = InventarioPanel()
        self.ventas = Ventas("Ventas", [])
>>>>>>> 92812e82879a4089e69fed641d8b074b70ec2e2e

        self.widgets_stack = QStackedWidget(self) # cada ventana debe tener su propio QStackedWidget
        self.widgets_stack.addWidget(self.admin_soporte)
        self.widgets_stack.addWidget(self.reportePanel)
        self.widgets_stack.addWidget(self.inventarioPanel)
<<<<<<< HEAD
        self.widgets_stack.addWidget(self.gestionPanel)
        self.widgets_stack.addWidget(self.addClientePanel)
=======
        ######################## final ########################

        ######################## Inicializando/conectando ventanas de gestion de clientes ########################

        ######################## final ########################
>>>>>>> 92812e82879a4089e69fed641d8b074b70ec2e2e

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
        self.admin_soporte.gestionBtn.clicked.connect(self.ventana_gestionClientes)

        ######################## Reportes ########################
        # Panel de reportes
        self.reportePanel.volverBtn.clicked.connect(self.anterior)
        self.reportePanel.inventarioBtn.clicked.connect(self.ventana_reportes_inventario)

        # Panel de gestion cliente
        self.gestionPanel.atrasBtn.clicked.connect(self.anterior)
        self.gestionPanel.addClienteBtn.clicked.connect(self.ventana_addCliente)
        self.addClientePanel.BotonAtrasCC.clicked.connect(self.anterior)

        # Panel de inventario
        self.inventarioPanel.volverBtn.clicked.connect(self.anterior)
        ######################## final ########################


        ######################## Gestion clientes ########################

        ######################## final ########################

    def ventana_reportes(self):
        self.widgets_stack.setCurrentWidget(self.reportePanel)
        self.stack.append(self.admin_soporte)

    def ventana_reportes_inventario(self):
        self.widgets_stack.setCurrentWidget(self.inventarioPanel)
        self.stack.append(self.reportePanel)

    def ventana_gestionClientes(self):
        self.widgets_stack.setCurrentWidget(self.gestionPanel)
        self.stack.append(self.admin_soporte)

    def ventana_addCliente(self):
        self.widgets_stack.setCurrentWidget(self.addClientePanel)
        self.stack.append(self.gestionPanel)

    def anterior(self):
        anterior = self.admin_soporte

        if self.stack:
            anterior = self.stack.pop()
        self.widgets_stack.setCurrentWidget(anterior)

    def leer_estilos(
        self, app: QApplication, paths: List[str]
    ) -> None:  # Toca organizar esta funcion
        for path in paths:
            with open(path, "r") as style_file:
                style_line = style_file.read()

        app.setStyleSheet(style_line)
        style_file.close()

    def run(self):
        self.show()
