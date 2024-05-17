import customtkinter as ctk
import util.util_images as util_img
import util.util_window as util_win


class GUI(ctk.CTk):
    # Constructor que contiene la configuración de las ventanas
    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen(
            "C:/Users/ASUS/OneDrive/Escritorio/EDD_Project/GLAM_MAKEUP_STORE/GUI/images/logo.ico",
            (400, 400),
        )
        self.configuracion_ventana()

    # En esta función se cargan las demás funciones
    def configuracion_ventana(self):
        self.title("Makeup Store")
        self.iconbitmap(
            "C:/Users/ASUS/OneDrive/Escritorio/EDD_Project/GLAM_MAKEUP_STORE/GUI/images/logo.ico"
        )
        w, h = 1000, 720
        util_win.centrar_ventana(self, w, h)
        self.login()

    # Ventana de login con control de acceso
    def login(self):
        self.frame_medio = ctk.CTkFrame(self)
        self.frame_medio.place(relx=0.5, rely=0.5, anchor="center")
        label_logo = ctk.CTkLabel(self.frame_medio, image=self.logo)
        label_logo.pack()
        self.frame_inferior = ctk.CTkFrame(self, bg_color="red", height=100)
        self.frame_inferior.pack(side=ctk.BOTTOM, fill="both")
        boton_menu_principal = ctk.CTkButton(self.frame_inferior, text="Menu Principal", height=100)
        boton_menu_principal.pack()
