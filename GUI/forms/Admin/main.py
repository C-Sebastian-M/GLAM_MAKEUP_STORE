import customtkinter as ctk
from components.utils import Global, Funciones
from components.ventanas import Ventanas

class Admin(Global):
    def __init__(self):
        self.ventanas = Ventanas()
        self.funciones = Funciones()
        super().__init__()

    def principal(self):
        root = self.instancia()
        root.title("Ventana de administración")
        root.iconbitmap("C:\GLAM_MAKEUP_STORE\GUI\images\shop_logo.ico")
        root.config(bg="")
        root.resizable(width=False, height=False)

        ancho, alto = 800, 600
        self.centrar_ventana(root, ancho, alto)

        # title
        cerrar_btn = ctk.CTkButton(
            root, 
            text="Cerrar", 
            text_color="white", 
            fg_color="#61615e",
            hover_color="#744464",
            font=('Arial', 15), 
            command=root.destroy
        )
        cerrar_btn.place(x=10, y=10)
        
        # contenedor
        cuadro = ctk.CTkFrame(master=root, width=400, height=300, fg_color="white")
        cuadro.pack(expand=True, padx=50, pady=50)

        # grid
        cuadro.columnconfigure(0, weight = 1, minsize=100, pad=80)
        cuadro.columnconfigure(1, weight = 1, minsize=100, pad=80)
        cuadro.rowconfigure(0, weight = 1, minsize=100, pad=80)
        cuadro.rowconfigure(1, weight = 1, minsize=100, pad=80)

        # botones
        ventas_btn = ctk.CTkButton(
            cuadro,
            width=100,
            height=50,
            corner_radius=4,
            text="Ventas", 
            fg_color="#4c2c43",
            hover_color="#4c2c43",
        )
        ventas_btn.grid(row=0, column=0)

        gestionar_btn = ctk.CTkButton(
            cuadro,
            width=100,
            height=50,
            corner_radius=4,
            text="Gestionar",
            fg_color="#4c2c43",
            hover_color="#ad4174"
        )
        gestionar_btn.grid(row=0, column=1)

        reportes_btn = ctk.CTkButton(
            cuadro,
            width=100,
            height=50,
            corner_radius=4,
            text="Reportes",
            fg_color="#4c2c43",
            hover_color="#ad4174",
            command=self.funciones.iniciar_ventana(self.ventanas.reporte_producto_customizado)
        )
        reportes_btn.grid(row=1, column=0)

        administrador_btn = ctk.CTkButton(
            cuadro,
            width=100,
            height=50,
            corner_radius=4,
            text="Administrar",
            fg_color="#4c2c43",
            hover_color="#ad4174"
        )
        administrador_btn.grid(row=1, column=1)

        root.mainloop()

    def run(self):
        self.principal()

admin = Admin()

admin.run()
