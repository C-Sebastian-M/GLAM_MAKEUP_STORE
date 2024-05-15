import tkinter as tk
import customtkinter


def open_registration_window():
    registration_window = customtkinter.CTk()
    registration_window.geometry("400x300")
    registration_window.title("Registro")

    # Agregar contenido a la ventana de registro, como etiquetas, campos de entrada, etc.
    # Por ejemplo:
    label = customtkinter.CTkLabel(
        master=registration_window, text="Formulario de Registro", font=("Arial", 18)
    )
    label.pack(pady=20)

    # Agregar más widgets aquí, como campos de entrada, botones, etc.

    registration_window.mainloop()


def open_income_window():
    income_window = customtkinter.CTk()
    income_window.geometry("400x300")
    income_window.title("Ingresar")

    label = customtkinter.CTkLabel(
        master=income_window, text="Formulario de Ingreso", font=("Arial", 18)
    )
    label.pack(pady=20)
    income_window.mainloop()


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("600x440")
app.title("Login")

# Crear botón de registro
register_button = customtkinter.CTkButton(
    master=app, text="REGISTRARSE", command=open_registration_window
)
register_button.pack(pady=20)
income_button = customtkinter.CTkButton(master=app,text="INGRESE", command=open_income_window)
income_button.pack(pady = 50)
app.mainloop()