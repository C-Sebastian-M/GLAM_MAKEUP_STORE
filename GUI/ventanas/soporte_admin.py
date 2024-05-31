from typing import List
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from PyQt5 import uic

from sub_ventanas.reportes import ReportePanel, InventarioPanel, Ventas, CBackground
from sub_ventanas.GestionClientes import GestionClientes, CrearCliente, ModificarCliente, EliminarCliente
from sub_ventanas.inventario_productos import InventarioProductos, CrearProducto, ModificarProducto

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
            is_admin=True 
            if self.role.strip().lower() == "admin" 
            else False
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
        self, user_role: str
    ) -> None:  # pass role as argument (soporte or admin)
        super(QMainWindow, self).__init__()
        if not user_role:
            raise TypeError("El rol de usuario no puede estar vacio.")

        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint)
        self.setFixedSize(800, 600)

        self.stack = [] # Guarda las ventanas anteriores

        self.widgets_stack = QStackedWidget(self)
        ########################### Inicializando ventanas de reporte ###########################
        self.admin_soporte = AdminSoporte(user_role)
        self.reportePanel = ReportePanel()
        self.inventarioPanel = InventarioPanel()
        self.ventas = Ventas("Ventas", ["id", "cantidad", "cliente", "productos", "box_id"])

        self.widgets_stack.addWidget(self.admin_soporte)
        self.widgets_stack.addWidget(self.reportePanel)
        self.widgets_stack.addWidget(self.inventarioPanel)
        self.widgets_stack.addWidget(self.ventas)
        ########################### fin ###########################

        ########################### Inicializando ventanas de gestion de cliente ###########################
        self.gestionPanel = GestionClientes()
        self.addClientePanel = CrearCliente()
        self.modificarCliente = ModificarCliente()
        self.eliminarPanel = EliminarCliente()

        self.widgets_stack.addWidget(self.gestionPanel)
        self.widgets_stack.addWidget(self.addClientePanel)
        self.widgets_stack.addWidget(self.modificarCliente)
        self.widgets_stack.addWidget(self.eliminarPanel)
        ########################### fin ###########################
        
        ########################### Inicializando ventanas de inventario de productos ###########################
        self.inventarioProductosPanel = InventarioProductos()
        self.crearProductoPanel = CrearProducto()
        self.modificarProductoPanel = ModificarProducto()
        
        self.widgets_stack.addWidget(self.inventarioProductosPanel)
        self.widgets_stack.addWidget(self.crearProductoPanel)
        self.widgets_stack.addWidget(self.modificarProductoPanel)
        ########################### fin ###########################


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
        self.admin_soporte.reportesBtn.clicked.connect(self.ventana_reportes) # Conexión a ventanas Reportes
        self.admin_soporte.gestionBtn.clicked.connect(self.ventana_gestionClientes) # Conexión a ventanas Gestión Clientes
        self.admin_soporte.inventarioBtn.clicked.connect(self.ventana_inventario_productos) # Conexión a ventanas Inventario de productos
        self.admin_soporte.reportesBtn.clicked.connect(self.ventana_reportes)
        self.admin_soporte.gestionBtn.clicked.connect(self.ventana_gestionClientes)
        self.admin_soporte.cambiarPassBtn.clicked.connect(self.ventana_cambiarPassword)

        # Panel de reportes
        self.reportePanel.volverBtn.clicked.connect(self.anterior)
        self.reportePanel.ventasBtn.clicked.connect(self.ventana_ventas)
        self.reportePanel.inventarioBtn.clicked.connect(self.ventana_inventario)
        # inventario
        self.inventarioPanel.volverBtn.clicked.connect(self.anterior)

        # Panel de gestion cliente
        self.gestionPanel.atrasBtn.clicked.connect(self.anterior)
        self.gestionPanel.addClienteBtn.clicked.connect(self.ventana_addCliente)
        self.gestionPanel.modificarBtn.clicked.connect(self.ventana_modificarCliente)
        self.gestionPanel.eliminarClienteBtn.clicked.connect(self.ventana_eliminarCliente)
        self.addClientePanel.BotonAtrasCC.clicked.connect(self.anterior)
        self.modificarCliente.BotonAtrasMC.clicked.connect(self.anterior)
        self.eliminarPanel.atrasBtnE.clicked.connect(self.anterior)
        self.eliminarPanel.cancelarBtnE.clicked.connect(self.anterior)
        self.eliminarPanel.guardarBtnE.clicked.connect(self.anterior)
        
        # Panel de inventario de productos
        self.inventarioProductosPanel.volver_boton.clicked.connect(self.anterior)
        self.inventarioProductosPanel.crear_producto_boton.clicked.connect(self.ventana_crear_producto)
        self.inventarioProductosPanel.modificar_producto_boton.clicked.connect(self.ventana_modificar_producto)
        self.crearProductoPanel.atras_boton.clicked.connect(self.anterior)
        self.modificarProductoPanel.atras_boton.clicked.connect(self.anterior)
        
        
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

    def ventana_cambiarPassword(self):
        None

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