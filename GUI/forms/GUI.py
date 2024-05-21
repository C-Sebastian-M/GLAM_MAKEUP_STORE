import customtkinter as ctk
import util.util_images as util_img
import util.util_window as util_win


class GUI(ctk.CTk):
    # Constructor que contiene la configuración de las ventanas
    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen(
            "GUI/images/logo.png",
            (400, 400),
        )
        self.configuracion_ventana()

    # En esta función se cargan las demás funciones
    def configuracion_ventana(self):
        self.title("Makeup Store")
        self.iconbitmap(
            "GUI/images/logo.ico"
        )
        w, h = 1000, 720
        util_win.centrar_ventana(self, w, h)
        self.login()

    # Ventana de login con control de acceso
    def login(self):
        self.frame_fondo = ctk.CTkFrame(self, fg_color="pink")
        self.frame_fondo.pack(fill="both", expand=True)
        self.frame_medio = ctk.CTkFrame(self, fg_color="#ff50b5")
        self.frame_medio.place(relx=0.5, rely=0.5, anchor="center")
        label_logo = ctk.CTkLabel(self.frame_medio, image=self.logo)
        label_logo.pack()
        login_button = ctk.CTkButton(
            self.frame_medio, text="Ingresar con una cuenta", command=self.ingresar_con_cuenta
        )
        login_button.pack(pady=20)

    def ingresar_con_cuenta(self):
        self.withdraw()
        ventana_ingreso = ctk.CTkToplevel(self)
        ventana_ingreso.title("Ingresar con cuenta")
        ventana_ingreso.geometry("800x600")
        util_win.centrar_ventana(ventana_ingreso, 800, 600)
        ventana_ingreso.mainloop()

    def menu_principal(self, rol):
        # Ocultar la ventana de login en lugar de destruirla
        self.withdraw()
        ventana_menu = ctk.CTkToplevel(self)
        ventana_menu.title("Menu Principal")
        ventana_menu.geometry("800x600")
        util_win.centrar_ventana(ventana_menu, 800, 600)

        if rol == "admin":
            ctk.CTkButton(ventana_menu, text="Gestionar Productos").pack(pady=10)
            ctk.CTkButton(ventana_menu, text="Gestionar Clientes").pack(pady=10)
            ctk.CTkButton(ventana_menu, text="Gestionar Ventas").pack(pady=10)
            ctk.CTkButton(ventana_menu, text="Gestionar Servicios").pack(pady=10)
            ctk.CTkButton(ventana_menu, text="Generar Reportes").pack(pady=10)
        elif rol == "usuario":
            ctk.CTkButton(ventana_menu, text="Ver Productos").pack(pady=10)
            ctk.CTkButton(ventana_menu, text="Registrar Venta").pack(pady=10)
        ventana_menu.mainloop()
