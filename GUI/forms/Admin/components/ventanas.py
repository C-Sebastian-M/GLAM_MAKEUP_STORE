from typing import Union

import tkinter as tk
import customtkinter as ctk

from PIL import Image, ImageTk

from components.utils import Global, Funciones

##################################### Codigo de reportes #####################################
class RInventario(Global):
    def __init__(self) -> None:
        self.funciones = Funciones()
        super().__init__()

    def panel(self, root: ctk.CTk):
        root.title('Panel de reportes')

        contenedor = ctk.CTkFrame(root, width=380, height=500, fg_color='transparent')
        contenedor.pack(expand=True, padx=50, pady=50)

        def volver_command():
            contenedor.destroy()

            if not self.stack:
                return

            anterior_frame = self.stack.pop()
            anterior_frame(root)

        # botones
        volver = ctk.CTkButton(
            root,
            width=80,
            height=35,
            corner_radius=0,
            text="Volver", 
            fg_color="#493F44",
            hover_color="#6a3954",
            command=volver_command
        )
        volver.place(x=0, y=20)

        def abrir_productos():
            self._ventana_general('productos')

        def abrir_servicios():
            self._ventana_general('servicios')

        productos_btn = ctk.CTkButton(
            contenedor,
            width=100,
            height=50,
            corner_radius=4,
            text="Productos", 
            fg_color="#4c2c43",
            hover_color="#ad4174",
            command=abrir_productos
        )
        productos_btn.pack(padx=10, side="left")

        servicios_btn = ctk.CTkButton(
            contenedor,
            width=100,
            height=50,
            corner_radius=4,
            text="Servicios",
            fg_color="#4c2c43",
            hover_color="#ad4174",
            command=abrir_servicios
        )
        servicios_btn.pack(padx=10, side="right")

    def _ventana_general(self, default: str  = "Productos"):
        if not default.strip().lower() in ['productos', 'servicios']:
            raise ValueError("El default solo acepta dos strings ('productos' y 'servicios'). ")

        ancho, alto = 800, 600
        root: ctk.CTk = self.crear_ventana(ancho, alto)

        self.inventario_producto(root) if default.lower() == 'productos' else self.inventario_servicios(root)

        root.mainloop()

    def inventario_producto(self, root: ctk.CTk):
        root.title("Productos")

        inp_contenedor = ctk.CTkFrame(root)
        inp_contenedor.place(x=0, y=30)

        ## Entry
        label = ctk.CTkLabel(inp_contenedor, text="Filtrar", font=ctk.CTkFont(family="Helvetica", size=12))
        label.pack(side='left')
        user_input = ctk.CTkEntry(inp_contenedor)
        user_input.pack(side="right")

    def inventario_servicios(self, root: ctk.CTk):
        root.title("Servicios")
        pass

class RVentas(Global):
    def __init__(self) -> None:
        self.funciones = Funciones()
        super().__init__()

    def panel(self, root):
        contenedor = ctk.CTkFrame(root, width=380, height=500, fg_color='transparent')
        contenedor.pack(expand=True, padx=50, pady=50)

        def volver_command():
            contenedor.destroy()

            if not self.stack:
                return

            anterior_frame = self.stack.pop()
            anterior_frame(root)

        # botones
        volver = ctk.CTkButton(
            root,
            width=80,
            height=35,
            corner_radius=0,
            text="Volver", 
            fg_color="#493F44",
            hover_color="#6a3954",
            command=volver_command
        )
        volver.place(x=0, y=20)

        productos_btn = ctk.CTkButton(
            contenedor,
            width=100,
            height=50,
            corner_radius=4,
            text="Productos", 
            fg_color="#4c2c43",
            hover_color="#ad4174"
        )
        productos_btn.pack(padx=10, side="left")

        servicios_btn = ctk.CTkButton(
            contenedor,
            width=100,
            height=50,
            corner_radius=4,
            text="Servicios",
            fg_color="#4c2c43",
            hover_color="#ad4174"
        )
        servicios_btn.pack(padx=10, side="right")

    def ventas_productos(self):
        pass

    def ventas_servicios(self):
        pass

class Reportes_Customizados(Global):
    def __init__(self) -> None:
        self.inv = RInventario()
        self.ven = RVentas()
        super().__init__()

    def principal(self):
        ventana = self.instancia()
        ventana.title("Reporte de productos")
        ventana.resizable(width=False, height=False)

        ancho, alto = 400, 600
        self.centrar_ventana(ventana, ancho, alto)

        self.cargar_cuadro_rep(root=ventana)

        ventana.mainloop()

    def cargar_cuadro_rep(self, root):
        contenedor = ctk.CTkFrame(root, width=380, height=500, fg_color='transparent')
        contenedor.pack(expand=True, padx=50, pady=50)

        def abrir_inventario():
            self.inventario(root, contenedor)

        def abrir_ventas():
            self.ventas(root, contenedor)

        # botones
        cerrar = ctk.CTkButton(
            root,
            width=80,
            height=35,
            corner_radius=0,
            text="Volver", # Cerrar Reportes
            fg_color="#493F44",
            hover_color="#6a3954",
            command=root.destroy
        )
        cerrar.place(x=0, y=20)

        inventario_btn = ctk.CTkButton(
            contenedor,
            width=100,
            height=50,
            corner_radius=4,
            text="Inventario", 
            fg_color="#4c2c43",
            hover_color="#ad4174",
            command=abrir_inventario
        )
        inventario_btn.pack(padx=10, side="left")

        ventas_btn = ctk.CTkButton(
            contenedor,
            width=100,
            height=50,
            corner_radius=4,
            text="Ventas",
            fg_color="#4c2c43",
            hover_color="#ad4174",
            command=abrir_ventas
        )
        ventas_btn.pack(padx=10, side="right")

    def inventario(self, parent: ctk.CTk, frame_to_replace: ctk.CTkFrame):
        self.stack.append(self.cargar_cuadro_rep)
        self.inv.stack = self.stack
        frame_to_replace.destroy()

        self.inv.panel(parent)

    def ventas(self, parent: ctk.CTk, frame_to_replace: ctk.CTkFrame):
        self.stack.append(self.cargar_cuadro_rep)
        self.ven.stack = self.stack
        frame_to_replace.destroy()

        self.ven.panel(parent)

##################################### final del codigo de reportes #####################################


class Ventas(Global):
    pass

class Gestion_Personalizada(Global):
    pass

class Administrador_Usuarios(Global):
    pass

class Ventanas():
    def __init__(self) -> None:
        self.reportes_customizados = Reportes_Customizados()

    def reporte_producto_customizado(self):
        self.reportes_customizados.principal()
