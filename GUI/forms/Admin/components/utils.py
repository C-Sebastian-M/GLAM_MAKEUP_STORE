import customtkinter as ctk

class Global:
    def __init__(self) -> None:
        self.stack = []
        self.instancia = ctk.CTk

    def centrar_ventana(self, root, ancho: int, altura: int):
        x = (root.winfo_screenwidth() // 2) - (ancho // 2)
        y = (root.winfo_screenheight() // 2) - (altura // 2)
        root.geometry("{}x{}+{}+{}".format(ancho, altura, x, y))

class Funciones(Global):
    def iniciar_ventana(self, ventana_fn):
        return ventana_fn 
    
    def tabTables(self):
        pass
