import customtkinter as ctk
import util.util_images as util_img
import util.util_window as util_win


class GUI(ctk.CTk):
    # Constructor que contiene la configuración de las ventanas
    def __init__(self):
        super().__init__()
        self.imgFondo = util_img.leer_imagen("GUI/Images/logo.png", (800, 600))
        self.configuracion_ventana()

    # En esta función se cargan las demás funciones y es la ejecutura
    def configuracion_ventana(self):
        self.crear_ventana_login()

    # Función para crear y configurar la ventana de login
    def crear_ventana_login(self):
        self.ventana_login = util_win.sub_ventana(self, "GLAM MAKEUP STORE" ,self.imgFondo)
        frame_cerrar = ctk.CTkFrame(self.ventana_login)
        frame_cerrar.place(relx=0.01, rely=0.01)
        frame_ingreso = ctk.CTkFrame(self.ventana_login)
        frame_ingreso.place(relx=0.5, rely=0.8, anchor="center")
        boton_ingreso = util_win.diseno_boton(
            frame_ingreso, "Ingrese con una cuenta", self.ingresar_con_cuenta
        )
        boton_ingreso.pack()
        boton_cerrar = util_win.diseno_boton(
            frame_cerrar, "Cerrar Programa", self.destroy
        )
        boton_cerrar.pack()

    def navegar_login_ingreso(self):
        self.ventana_ingreso.destroy()
        self.ventana_login.deiconify()

    def ingresar_con_cuenta(self):
        self.ventana_login.withdraw()
        self.ventana_ingreso = util_win.sub_ventana(self, "Login", self.imgFondo)
        frame_entrada_usuario = ctk.CTkFrame(self.ventana_ingreso, fg_color="#ff50b5")
        frame_entrada_usuario.place(relx=0.5, rely=0.4, anchor="center")
        frame_entrada_contrasena = ctk.CTkFrame(
            self.ventana_ingreso, fg_color="#ff50b5"
        )
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
        boton_cancelar = util_win.diseno_boton(
            self.ventana_ingreso, "Cancelar", self.navegar_login_ingreso
        )
        boton_cancelar.place(relx=0.20, rely=0.90)
        boton_confirmar = util_win.diseno_boton(
            self.ventana_ingreso, "Confirmar", self.verificar_credenciales_ingreso
        )
        boton_confirmar.place(relx=0.60, rely=0.90)
        self.error_label = ctk.CTkLabel(
            self.ventana_ingreso, fg_color="#eb4996", text_color="black"
        )
        self.error_label.place(relx=0.5, rely=0.03, anchor="center")

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
            self.error_label.configure(
                text="Usuario/Contraseña icorrectos, ingrese de nuevo"
            )

    def admin(self):
        self.ventana_ingreso.destroy()
        self.ventana_admin = util_win.sub_ventana(self, "Admin", self.imgFondo)
        clientes_boton = util_win.diseno_boton(self.ventana_admin, "Gestión Clientes", None)
        clientes_boton.place(relx=0.2, rely=0.2)
        ventas_boton = util_win.diseno_boton(self.ventana_admin, "Ventas", None)
        ventas_boton.place(relx=0.6, rely=0.2)
        admin_usuario = util_win.diseno_boton(self.ventana_admin, "Administrar Usuarios", None)
        admin_usuario.place(relx=0.2, rely=0.6)
        cerrar_boton = util_win.diseno_boton(
            self.ventana_admin, "Cerrar Programa", self.destroy
        )
        cerrar_boton.place(relx=0.01, rely=0.01)
