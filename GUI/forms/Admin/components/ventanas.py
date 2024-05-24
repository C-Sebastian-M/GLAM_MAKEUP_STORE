import tkinter as tk
import customtkinter as ctk

from PIL import Image, ImageTk

from components.utils import Global, Funciones

##################################### Codigo de reportes #####################################
class RInventario(Global):
    def __init__(self) -> None:
        self.funciones = Funciones()
        super().__init__()

    def principal(self, root):
        contenedor = ctk.CTkFrame(root, width=380, height=500, fg_color='transparent')
        contenedor.pack(expand=True, padx=50, pady=50)

        def volver_command():
            contenedor.destroy()

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

    def inventario_producto(self):
        pass

    def inventario_servicios(self):
        pass

class RVentas(Global):
    def __init__(self) -> None:
        self.funciones = Funciones()
        super().__init__()

    def principal(self, root):
        contenedor = ctk.CTkFrame(root, width=380, height=500, fg_color='transparent')
        contenedor.pack(expand=True, padx=50, pady=50)

        def volver_command():
            contenedor.destroy()

            contenedor = self.stack.pop()

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

        # comandos
        def volver_command():
            ventana.destroy()

        # botones
        volver = ctk.CTkButton(
            ventana,
            width=80,
            height=35,
            corner_radius=0,
            text="Volver", 
            fg_color="#493F44",
            hover_color="#6a3954",
            command=volver_command
        )
        volver.place(x=0, y=20)

        contenedor = ctk.CTkFrame(ventana, width=380, height=500, fg_color='transparent')
        contenedor.pack(expand=True, padx=50, pady=50)

        def abrir_inventario():
            self.inventario(ventana, contenedor)

        def abrir_ventas():
            self.ventas(ventana, contenedor)

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

        ventana.mainloop()

    def inventario(self, parent: ctk.CTk, frame_to_replace: ctk.CTkFrame):
        self.stack.append(frame_to_replace)
        frame_to_replace.destroy()

        self.inv.principal(parent)

    def ventas(self, parent: ctk.CTk, frame_to_replace: ctk.CTkFrame):
        self.stack.append(frame_to_replace)
        frame_to_replace.destroy()

        self.ven.principal(parent)

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
