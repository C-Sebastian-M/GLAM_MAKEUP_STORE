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

    # En esta función se cargan las demas funciones
    def configuracion_ventana(self):
        self.title("Makeup Store")
        self.iconbitmap(
            "C:/Users/ASUS/OneDrive/Escritorio/EDD_Project/GLAM_MAKEUP_STORE/GUI/images/logo.ico"
        )
        w, h = 800, 600
        util_win.centrar_ventana(self, w, h)
        self.login()

    def login(self):
        self.frame_superior = ctk.CTkFrame(self, bg_color="blue", height=100)
        self.frame_superior.pack(side=ctk.TOP, fill="both")
        self.frame_medio = ctk.CTkFrame(self, bg_color="pink", height=400)
        self.frame_medio.pack(anchor=ctk.CENTER, fill="both")
        label_logo = ctk.CTkLabel(self.frame_medio, image=self.logo)
        label_logo.pack()
        self.frame_inferior = ctk.CTkFrame(self, bg_color="red", height=100)
        self.frame_inferior.pack(side=ctk.BOTTOM, fill="both")
        boton_menu_principal = ctk.CTkButton(self.frame_inferior, text="Menu Principal", height=100)
        boton_menu_principal.pack()