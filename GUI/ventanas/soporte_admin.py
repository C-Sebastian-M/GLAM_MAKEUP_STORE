from typing import List
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from GUI.sub_ventanas.reportes import ReportePanel, InventarioPanel, Ventas, CBackground

from GUI.sub_ventanas.GestionClientes import (
    GestionClientes
)

from GUI.sub_ventanas.inventario_productos import (
    InventarioProductos,
    CrearProducto,
    ModificarProducto,
    ModificarAtributosProducto
)

class AdminSoporte(QMainWindow, CBackground):
    def __init__(self, role: str) -> None:
        super(QMainWindow, self).__init__()
        self.role = role

        uic.loadUi(
            r"GUI\sub_ventanas\ui\reportes\adminDesigner.ui",
            self,
        )

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
    def __init__(self, ventana_login ,user_role: str) -> None:  # pass role as argument (soporte or admin)
        super(QMainWindow, self).__init__()
        self.ventana_login=ventana_login
        if not user_role:
            raise TypeError("El rol de usuario no puede estar vacio.")

        self.setWindowFlags(
            Qt.Window | Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint
        )
        self.setFixedSize(800, 600)
        self.setWindowIcon(QIcon(r"GUI\recursos\images\icono.ico"))
        self.setWindowTitle("GLAM MAKEUP STORE")

        self.stack = []  # Guarda las ventanas anteriores

        self.widgets_stack = QStackedWidget(self)
        ########################### Inicializando ventanas de reporte ###########################
        self.admin_soporte = AdminSoporte(user_role)
        self.reportePanel = ReportePanel()
        self.inventarioPanel = InventarioPanel()
        self.ventas = Ventas(
            "Ventas", ["id", "cantidad", "cliente", "productos", "box_id"]
        )

        self.widgets_stack.addWidget(self.admin_soporte)
        self.widgets_stack.addWidget(self.reportePanel)
        self.widgets_stack.addWidget(self.inventarioPanel)
        self.widgets_stack.addWidget(self.ventas)
        ########################### fin ###########################
        self.admin_soporte.cerrarBtn.clicked.connect(self.volver_login)

        ########################### Inicializando ventanas de gestion de cliente ###########################
        self.gestionPanel = GestionClientes()
        self.widgets_stack.addWidget(self.gestionPanel)
        ########################### fin ###########################
        
        ########################### Inicializando ventanas de inventario de productos ###########################
        self.inventarioProductosPanel = InventarioProductos()
        self.crearProductoPanel = CrearProducto()
        self.modificarProductoPanel = ModificarProducto()
        self.modificarAtributosProductoPanel = ModificarAtributosProducto()
        
        self.widgets_stack.addWidget(self.inventarioProductosPanel)
        self.widgets_stack.addWidget(self.crearProductoPanel)
        self.widgets_stack.addWidget(self.modificarProductoPanel)
        self.widgets_stack.addWidget(self.modificarAtributosProductoPanel)
        ########################### fin ###########################

        # asignando el widget central
        self.setCentralWidget(self.widgets_stack)
        # set actual
        self.widgets_stack.setCurrentWidget(self.admin_soporte)

        # conexiones
        self.inicializar()
    
    #Volver al login
    def volver_login(self):
        self.ventana_login.show()
        self.close()

    def inicializar(self):
        self.resize(800, 600)
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
        self.admin_soporte.inventarioBtn.clicked.connect(
            self.ventana_inventario_productos
        )  # Conexión a ventanas Inventario de productos

        # Panel de reportes
        self.reportePanel.volverBtn.clicked.connect(self.anterior)
        self.reportePanel.ventasBtn.clicked.connect(self.ventana_ventas)
        self.reportePanel.inventarioBtn.clicked.connect(self.ventana_inventario)
        # inventario
        self.inventarioPanel.volverBtn.clicked.connect(self.anterior)

        # Panel de gestion cliente
        self.gestionPanel.atrasBtn.clicked.connect(self.anterior)

        # Panel de inventario de productos
        self.inventarioProductosPanel.volverBtn.clicked.connect(self.anterior)
        self.inventarioProductosPanel.crear_producto_boton.clicked.connect(self.ventana_crear_producto)
        self.inventarioProductosPanel.modificar_producto_boton.clicked.connect(self.ventana_modificar_producto)
        
        self.crearProductoPanel.volverBtn.clicked.connect(self.anterior)
        
        self.modificarProductoPanel.volverBtn.clicked.connect(self.anterior)
        self.modificarProductoPanel.seleccionar_producto_combobox.currentIndexChanged.connect(self.ventana_modificar_atributos_producto)
        self.modificarAtributosProductoPanel.volverBtn.clicked.connect(self.anterior)
        self.modificarAtributosProductoPanel.cancelar_boton.clicked.connect(self.anterior)

    ###### Reportes ######
    def ventana_reportes(self):
        self.widgets_stack.setCurrentWidget(self.reportePanel)
        self.stack.append(self.admin_soporte)

    def ventana_ventas(self):
        self.widgets_stack.setCurrentWidget(self.ventas)
        self.stack.append(self.reportePanel)

    def ventana_inventario(self):
        self.widgets_stack.setCurrentWidget(self.inventarioPanel)
        self.stack.append(self.reportePanel)

    ###### Gestion clientes ######
    def ventana_gestionClientes(self):
        self.widgets_stack.setCurrentWidget(self.gestionPanel)
        self.stack.append(self.admin_soporte)

    def ventana_addCliente(self):
        self.widgets_stack.setCurrentWidget(self.addClientePanel)
        self.stack.append(self.gestionPanel)

    def ventana_modificarCliente(self):
        self.widgets_stack.setCurrentWidget(self.modificarCliente)
        self.stack.append(self.gestionPanel)

    def ventana_eliminarCliente(self):
        self.widgets_stack.setCurrentWidget(self.eliminarPanel)
        self.stack.append(self.gestionPanel)
        
    ###### Inventario de productos ######
    def ventana_inventario_productos(self):
        self.widgets_stack.setCurrentWidget(self.inventarioProductosPanel)
        self.stack.append(self.admin_soporte)

    def ventana_crear_producto(self):
        self.widgets_stack.setCurrentWidget(self.crearProductoPanel)
        self.stack.append(self.inventarioProductosPanel)

    def ventana_modificar_producto(self):
        self.widgets_stack.setCurrentWidget(self.modificarProductoPanel)
        self.stack.append(self.inventarioProductosPanel)
        
    def ventana_modificar_atributos_producto(self):
        self.update_producto_seleccionado()
        self.widgets_stack.setCurrentWidget(self.modificarAtributosProductoPanel)
        self.stack.append(self.modificarProductoPanel)
    
    def update_producto_seleccionado(self):
        self.producto_seleccionado = self.modificarProductoPanel.seleccionar_producto_combobox.currentText()
        self.modificarAtributosProductoPanel.label_producto_seleccionado.setText(self.producto_seleccionado)

    ###### Volver ######
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
