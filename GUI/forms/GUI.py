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

    # En esta función se cargan las demás funciones y es la ejecutura
    def configuracion_ventana(self):
        self.crear_ventana_login()

    # Función para crear y configurar la ventana de login
    def crear_ventana_login(self):
        self.ventana_login = ctk.CTkToplevel(self)
        self.ventana_login.title("Login")
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
            command=self.destroy,
        )
        cerrar_boton.place(relx=0.01, rely=0.01)
        # Centrar la ventana de login
        util_win.centrar_ventana(self.ventana_login, 800, 600)

    def navegar_login_ingreso(self):
        self.ventana_ingreso.destroy()
        self.ventana_login.deiconify()

    def ingresar_con_cuenta(self):
        self.ventana_login.withdraw()
        self.ventana_ingreso = ctk.CTkToplevel(self)
        self.ventana_ingreso.title("Ingresar con cuenta")
        self.ventana_ingreso.geometry("800x600")
        util_win.centrar_ventana(self.ventana_ingreso, 800, 600)
        frame_fondo = ctk.CTkFrame(self.ventana_ingreso, fg_color="pink")
        frame_fondo.pack(fill="both", expand=True)
        frame_entrada_usuario = ctk.CTkFrame(frame_fondo, fg_color="#ff50b5")
        frame_entrada_usuario.place(relx=0.5, rely=0.4, anchor="center")
        frame_entrada_contrasena = ctk.CTkFrame(frame_fondo, fg_color="#ff50b5")
        frame_entrada_contrasena.place(relx=0.5, rely=0.7, anchor="center")
        self.entrada_usuario = ctk.CTkEntry(
            master=frame_entrada_usuario, width=400, placeholder_text="Ingrese Usuario"
        )
        self.entrada_usuario.pack()
        self.entrada_contrasena = ctk.CTkEntry(
            master=frame_entrada_contrasena,
            width=400,
            placeholder_text="Ingrese Contraseña",
            show="*",
        )
        self.entrada_contrasena.pack()
        boton_cancelar = ctk.CTkButton(
            frame_fondo,
            text="Cancelar",
            command=self.navegar_login_ingreso,
        )
        boton_cancelar.place(relx=0.20, rely=0.90)
        boton_confirmar = ctk.CTkButton(
            frame_fondo,
            text="Confirmar",
            command=self.verificar_credenciales_ingreso,
        )
        boton_confirmar.place(relx=0.60, rely=0.90)
        self.error_label = ctk.CTkLabel(
            frame_fondo, text="", fg_color="red", text_color="black"
        )
        self.error_label.pack(pady=5)

    def verificar_credenciales_ingreso(self):
        usuario = self.entrada_usuario.get()
        contrasena = self.entrada_contrasena.get()
        if usuario == "Admin" and contrasena == "admin123":
            self.admin()
        elif usuario == "Usuario" and contrasena == "usuario123":
            # Acá iria la ventana de caja y derivados
            None
        elif usuario == "Soporte" and contrasena == "soporte123":
            # Acá iria la ventana de soporte y derivados
            None
        else:
            self.error_label.configure(text="Credenciales incorrectas")

    def admin(self):
        self.ventana_ingreso.destroy()
        self.ventana_admin = ctk.CTkToplevel(self)
        self.ventana_admin.title("Ingresar con cuenta")
        self.ventana_admin.geometry("800x600")
        util_win.centrar_ventana(self.ventana_admin, 800, 600)
        frame_fondo = ctk.CTkFrame(self.ventana_admin, fg_color="pink")
        frame_fondo.pack(fill="both", expand=True)
        cerrar_boton = ctk.CTkButton(
            master=frame_fondo,
            text="Cerrar Programa",
            command=self.destroy,
        )
        cerrar_boton.place(relx=0.01, rely=0.01)
