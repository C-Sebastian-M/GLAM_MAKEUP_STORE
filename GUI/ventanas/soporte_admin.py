from typing import List
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QCursor
from PyQt5 import uic

from GUI.sub_ventanas.reportes import (
    ReportePanel, Ventas,
    Inventario, CBackground,
)

from GUI.sub_ventanas.inventario_productos import InventarioProductos

from GUI.sub_ventanas.GestionClientes import GestionClientes
from GUI.sub_ventanas.catalogo_servicios import GestionServicios

import API.DATA as GD
GD = GD.GestionDatos()


class AdminSoporte(QMainWindow, CBackground):
    def __init__(self, role: str) -> None:
        super(QMainWindow, self).__init__()
        self.role = role

        uic.loadUi(r"GUI\sub_ventanas\ui\reportes\adminDesigner.ui", self)

        self.inicializar(
            is_admin=True if self.role.strip().lower() == "admin" else False
        )

    def inicializar(self, is_admin: str | bool) -> None:
        if is_admin or is_admin == "admin":
            self.setWindowTitle("Administrador")
            self.title.setText("Admin")
            self.roleBtn.setText("Reporte\nDiario")
            return

        self.setWindowTitle("Soporte")
        self.title.setText("Soporte")
        self.roleBtn.setText("Administrar\nusuario")


class AdminSoporteManager(QMainWindow):
    def __init__(
        self, ventana_login, user_role: str
    ) -> None:  # pass role as argument (soporte or admin)
        super(QMainWindow, self).__init__()
        self.ventana_login = ventana_login
        if not user_role:
            raise TypeError("El rol de usuario no puede estar vacio.")
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowIcon(QIcon(r"GUI\recursos\images\icono.ico"))
        self.setWindowTitle("GLAM MAKEUP STORE")
        self.stack = []  # Guarda las ventanas anteriores
        self.widgets_stack = QStackedWidget(self)
        ########################### Inicializando ventanas de reporte ###########################
        self.admin_soporte = AdminSoporte(user_role)
        self.reportePanel = ReportePanel()
        # self.inventarioPanel = InventarioPanel()
        self.ventas = Ventas(
            "Ventas", GD.columnas_venta_productos
        )
        self.inventarioProductos = Inventario(
            "Inventario", GD.columnas_productos
        )
        self.inventarioServicios = Inventario(
            "Inventario", GD.columnas_servicios
        )
        self.widgets_stack.addWidget(self.admin_soporte)
        self.widgets_stack.addWidget(self.reportePanel)
        self.widgets_stack.addWidget(self.ventas)
        # self.widgets_stack.addWidget(self.inventario)
        self.widgets_stack.addWidget(self.inventarioProductos)
        self.widgets_stack.addWidget(self.inventarioServicios)
        ########################### fin ###########################
        self.admin_soporte.cerrarBtn.clicked.connect(self.volver_login)

        # Inicializando ventanas de gestion
        self.gestionPanel = GestionClientes()
        self.gestionServiciosPanel = GestionServicios()
        self.widgets_stack.addWidget(self.gestionPanel)
        self.widgets_stack.addWidget(self.gestionServiciosPanel)
        # fin

        # Inicializando ventana de Inventario de productos
        self.principalInventarioProductosPanel = InventarioProductos()
        self.widgets_stack.addWidget(self.principalInventarioProductosPanel)

        # asignando el widget central
        self.setCentralWidget(self.widgets_stack)
        # set actual
        self.widgets_stack.setCurrentWidget(self.admin_soporte)

        # conexiones
        self.inicializar()

    # Volver al login
    def volver_login(self):
        self.ventana_login.show()
        self.close()

    def inicializar(self):
        self.resize(1200, 800)
        self.conexiones()

        buttons = self.findChildren(QPushButton)
        for button in buttons:
            button.setCursor(QCursor(Qt.PointingHandCursor))

    def conexiones(self):
        # Main
        self.admin_soporte.reportesBtn.clicked.connect(
            self.ventana_reportes
        )  # Conexión a ventanas Reportes
        self.admin_soporte.gestionBtn.clicked.connect(
            self.ventana_gestionClientes
        )  # Conexión a ventanas Gestión Clientes
        self.admin_soporte.catalogoBtn.clicked.connect(
            self.ventana_gestionServicios
        )  # Conexión a ventanas Gestión servicios
        self.admin_soporte.inventarioBtn.clicked.connect(
            self.ventana_principalInventarioProductos
        )  # Conexión a ventanas Inventario de productos

        # Panel de reportes
        self.reportePanel.volverBtn.clicked.connect(self.anterior)

        self.reportePanel.inventarioBtn.clicked.connect(self.ventana_inventario)
        self.reportePanel.ventasBtn.clicked.connect(self.ventana_ventas)
        self.ventas.volverBtn.clicked.connect(self.anterior)

        self.inventarioServicios.productosBtn.clicked.connect(self.ventana_inventarioProductos)
        self.inventarioProductos.serviciosBtn.clicked.connect(self.ventana_inventarioServicios)

        self.inventarioServicios.volverBtn.clicked.connect(self.anterior)
        self.inventarioProductos.volverBtn.clicked.connect(self.anterior)

        # Panel de gestion cliente
        self.gestionPanel.atrasBtn.clicked.connect(self.anterior)

        # Panel de gestion servicios
        self.gestionServiciosPanel.atrasBtn.clicked.connect(self.anterior)

        # Panel de inventario de productos
        self.principalInventarioProductosPanel.atrasBtn.clicked.connect(self.anterior)

    ###### Reportes ######
    def ventana_reportes(self):
        self.widgets_stack.setCurrentWidget(self.reportePanel)
        self.stack.append(self.admin_soporte)

    def ventana_ventas(self):
        self.widgets_stack.setCurrentWidget(self.ventas)
        self.stack.append(self.reportePanel)

    def ventana_inventario(self):
        self.ventana_inventarioProductos()

    def ventana_inventarioServicios(self):
        self.widgets_stack.setCurrentWidget(self.inventarioServicios)
        if not self.reportePanel in self.stack:
            self.stack.append(self.reportePanel)

        self.inventarioServicios.serviciosBtn.setStyleSheet(
            "background-color: #FFFFFF;"
        )
        self.inventarioServicios.productosBtn.setStyleSheet("background-color: none;")

    def ventana_inventarioProductos(self):
        self.widgets_stack.setCurrentWidget(self.inventarioProductos)
        if not self.reportePanel in self.stack:
            self.stack.append(self.reportePanel)

        self.inventarioProductos.serviciosBtn.setStyleSheet("background-color: none;")
        self.inventarioProductos.productosBtn.setStyleSheet(
            "background-color: #FFFFFF;"
        )

    # Gestion clientes
    def ventana_gestionClientes(self):
        self.widgets_stack.setCurrentWidget(self.gestionPanel)
        self.stack.append(self.admin_soporte)

    def ventana_gestionServicios(self):
        self.widgets_stack.setCurrentWidget(self.gestionServiciosPanel)
        self.stack.append(self.admin_soporte)

    # Inventario de productos
    def ventana_principalInventarioProductos(self):
        self.widgets_stack.setCurrentWidget(self.principalInventarioProductosPanel)
        self.stack.append(self.admin_soporte)

    #################################### Volver ####################################
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
