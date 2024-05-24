from typing import Dict, Union, List

import tkinter as tk

import customtkinter as ctk

class Global:
    def __init__(self) -> None:
        self.stack = []
        self.instancia = ctk.CTk
        #self.fonts = {
        #    "helvatica": ctk.CTkFont(family="Helvetica", size=12),
        #    "arial": ctk.CTkFont(family="Arial", size=12),
        #    "pacifico": ctk.CTkFont(family="Pacifico", size=12),
        #    "roboto": ctk.CTkFont(family="Roboto", size=12),
        #}

    def crear_ventana(self, ancho: int, alto: int, title: str = 'sin titulo'):
        ventana = self.instancia()
        ventana.title(title)
        # ventana.iconbitmap("C:\GLAM_MAKEUP_STORE\GUI\images\shop_logo.ico")
        ventana.config(bg="")
        ventana.resizable(width=False, height=False)

        self.centrar_ventana(ventana, ancho, alto)

        return ventana

    def centrar_ventana(self, root, ancho: int, altura: int):
        x = (root.winfo_screenwidth() // 2) - (ancho // 2)
        y = (root.winfo_screenheight() // 2) - (altura // 2)
        root.geometry("{}x{}+{}+{}".format(ancho, altura, x, y))

class Funciones(Global):
    def iniciar_ventana(self, ventana_fn):
        return ventana_fn 
    
    def crear_tabla(self, Data: Dict[str, Union[List[str], List[Union[int, float]]]]):
        tabla = tk
