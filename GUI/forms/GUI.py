import customtkinter as ctk
import util.util_images as util_img
import util.util_window as util_win


class GUI(ctk.CTk):
    # Constructor que contiene la configuración de las ventanas
    def __init__(self):
        super().__init__()
        self.icono = "GUI/images/logo.ico"  # Definimos el icono de la ventana padre
        self.logo = util_img.leer_imagen(
            "GUI/images/logo.png",
            (400, 400),
        )
        self.configuracion_ventana()

    # En esta función se cargan las demás funciones
    def configuracion_ventana(self):
        self.iconbitmap(self.icono)  # Aplicamos el icono a la ventana padre
        w, h = 1000, 720
        util_win.centrar_ventana(self, w, h)
        self.crear_ventana_login()

    def cerrar_ventana(self, ventana):
        ventana.destroy()

    # Función para crear y configurar la ventana de login
    def crear_ventana_login(self):
        self.ventana_login = ctk.CTkToplevel(self)
        self.ventana_login.title("Login")
        self.ventana_login.iconbitmap(
            self.icono
        )  # Heredamos el icono de la ventana padre
        frame_fondo = ctk.CTkFrame(self.ventana_login, fg_color="pink")
        frame_fondo.pack(fill="both", expand=True)
        frame_medio = ctk.CTkFrame(frame_fondo, fg_color="#ff50b5")
        frame_medio.place(relx=0.5, rely=0.5, anchor="center")
        label_logo = ctk.CTkLabel(frame_medio, image=self.logo)
        label_logo.pack()
        login_boton = ctk.CTkButton(
            frame_medio,
            text="Ingresar con una cuenta",
            command=self.ingresar_con_cuenta,
        )
        login_boton.pack(pady=20)
        cerrar_boton = ctk.CTkButton(
            master=frame_fondo,
            text="Cerrar Programa",
            command=lambda: self.cerrar_ventana(self.ventana_login),
        )
        cerrar_boton.place(relx=0.01, rely=0.01)
        # Centrar la ventana de login
        util_win.centrar_ventana(self.ventana_login, 800, 600)
        self.ventana_login.mainloop()

    def ingresar_con_cuenta(self):
        self.ventana_login.withdraw()
        self.ventana_ingreso = ctk.CTkToplevel(self)
        self.ventana_ingreso.title("Ingresar con cuenta")
        self.ventana_ingreso.geometry("800x600")
        self.ventana_ingreso.iconbitmap(
            self.icono
        )  # Heredamos el icono de la ventana padre
        util_win.centrar_ventana(self.ventana_ingreso, 800, 600)
        frame_fondo = ctk.CTkFrame(self.ventana_ingreso, fg_color="pink")
        frame_fondo.pack(fill="both", expand=True)
        frame_entrada_usuario = ctk.CTkFrame(frame_fondo, fg_color="#ff50b5")
        frame_entrada_usuario.place(relx=0.5, rely=0.4, anchor="center")
        frame_entrada_contrasena = ctk.CTkFrame(frame_fondo, fg_color="#ff50b5")
        frame_entrada_contrasena.place(relx=0.5, rely=0.7, anchor="center")
        entrada_usuario = ctk.CTkEntry(
            master=frame_entrada_usuario, width=400, placeholder_text="Ingrese Usuario"
        )
        entrada_usuario.pack()
        entrada_contrasena = ctk.CTkEntry(
            master=frame_entrada_contrasena,
            width=400,
            placeholder_text="Ingrese Contraseña",
        )
        entrada_contrasena.pack()
        boton_cancelar = ctk.CTkButton(
            frame_fondo,
            text="Cancelar",
            command=print("Acá debe ir el regreso a la ventana anterior"),
        )
        boton_cancelar.place(relx=0.10, rely=0.70)
        self.ventana_ingreso.mainloop()
