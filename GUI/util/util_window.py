import customtkinter as ctk


def centrar_ventana(ventana, aplicacion_ancho, aplicacion_largo):
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()
    x = int((pantall_ancho / 2) - (aplicacion_ancho / 2))
    y = int((pantall_largo / 2) - (aplicacion_largo / 2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")


def diseno_boton(master, texto, comando):
    return ctk.CTkButton(
        master=master,  # El frame o ventana donde se colocará el botón
        text=texto,  # El texto del botón
        fg_color="#d63384",  # Color de fondo del botón (rosa oscuro)
        hover_color="#c2185b",  # Color al pasar el cursor (rosa más oscuro)
        text_color="white",  # Color del texto
        corner_radius=10,  # Esquinas redondeadas
        font=("Helvetica", 16, "bold"),  # Fuente elegante
        command=comando,  # La función que se ejecuta al hacer clic
    )


def frame_fondo(ventana):
    return ctk.CTkFrame(
        ventana,
        fg_color="pink",  # Fondo rosado
        border_color="#d63384",  # Borde de color rosa oscuro
        border_width=5,  # Ancho del borde
        corner_radius=15,
    )  # Esquinas redondeadas


def frame_medio(frame):
    return ctk.CTkFrame(
        frame,
        fg_color="#ff50b5",  # Fondo rosado más oscuro
        border_color="white",  # Borde blanco
        border_width=3,  # Ancho del borde
        corner_radius=10,  # Esquinas redondeadas
    )
