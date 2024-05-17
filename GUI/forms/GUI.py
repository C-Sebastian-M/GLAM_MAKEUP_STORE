import customtkinter as ctk
import util.util_images as util_img
import util.util_window as util_win


class GUI(ctk.CTk):
    # Constructor que contiene la configuración de las ventanas
    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen(
            "C:/Users/Sebastian/OneDrive - INSTITUTO TECNOLOGICO METROPOLITANO - ITM/Estructura de datos/GLAM_MAKEUP_STORE/GUI/images/logo.png",
            (400, 400),
        )
        self.configuracion_ventana()

    # En esta función se cargan las demás funciones
    def configuracion_ventana(self):
        self.title("Makeup Store")
        self.iconbitmap(
            "C:/Users/Sebastian/OneDrive - INSTITUTO TECNOLOGICO METROPOLITANO - ITM/Estructura de datos/GLAM_MAKEUP_STORE/GUI/images/logo.ico"
        )
        w, h = 1000, 720
        util_win.centrar_ventana(self, w, h)
        self.login()

    # Ventana de login con control de acceso
    def login(self):
        self.frame_medio = ctk.CTkFrame(self)
        self.frame_medio.place(relx=0.5, rely=0.5, anchor="center")
        #label_logo = ctk.CTkLabel(self.frame_medio, image=self.logo)
        #label_logo.pack()
        self.usuario_entry = ctk.CTkEntry(self.frame_medio, placeholder_text="Usuario")
        self.usuario_entry.pack(pady=5)
        self.password_entry = ctk.CTkEntry(
            self.frame_medio, placeholder_text="Contraseña", show="*"
        )
        self.password_entry.pack(pady=5)

        login_button = ctk.CTkButton(
            self.frame_medio, text="Login", command=self.verificar_credenciales
        )
        login_button.pack(pady=20)

    def verificar_credenciales(self):
        usuario = self.usuario_entry.get()
        password = self.password_entry.get()

        # Aquí se implementaría la verificación de credenciales
        if usuario == "admin" and password == "admin123":
            self.menu_principal("admin")
        elif usuario == "usuario" and password == "usuario123":
            self.menu_principal("usuario")
        else:
            self.error_label.configure(text="Credenciales incorrectas")

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
