import customtkinter as ctk


def centrar_ventana(ventana, aplicacion_ancho, aplicacion_largo):
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()
    x = int((pantall_ancho / 2) - (aplicacion_ancho / 2))
    y = int((pantall_largo / 2) - (aplicacion_largo / 2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")


def sub_ventana(ventana_padre, titulo, imagen):
    ventana = ctk.CTkToplevel(ventana_padre)
    ventana.title(titulo)
    fondo = frame_fondo(ventana)
    fondo.pack(fill="both", expand=True)
    imagen_fondo = ctk.CTkLabel(fondo, image=imagen, text=None, fg_color="red")
    imagen_fondo.place(relx=0.5, rely=0.5, anchor="center")
    ventana.attributes('-toolwindow', True)
    ventana.resizable(False, False)
    centrar_ventana(ventana,800,600)
    return ventana


def diseno_boton(master, texto, comando):
    return ctk.CTkButton(
        master=master,  # El frame o ventana donde se colocará el botón
        text=texto,  # El texto del botón
        fg_color="white",  # Color de fondo del botón (rosa oscuro)
        hover_color="#c2185b",  # Color al pasar el cursor (rosa más oscuro)
        text_color="#4d2f41",  # Color del texto
        corner_radius=10,  # Esquinas redondeadas
        font=("Helvetica", 16, "bold"),  # Fuente elegante
        command=comando,  # La función que se ejecuta al hacer clic
    )


def frame_fondo(ventana):
    return ctk.CTkFrame(
        ventana,
        fg_color="#f16fb3",  # Fondo
        border_color="#4c2c43",
        border_width=5,  # Ancho del borde
        corner_radius=15,)# Esquinas redondeadas
