from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from GUI.sub_ventanas.custom.utils.css import CBackground

class PasswordChange(QWidget, CBackground):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(
            r"GUI\sub_ventanas\ui\cambioDeContraseña.ui", 
            self
        )

        self.inicializar()

    def inicializar(self) -> None:
        self.pintar()

    def pintar(self) -> None:
        with open(r"GUI\sub_ventanas\css\cambio_contraseña.css", "r") as style_file:
            style_line = style_file.read()

        self.setStyleSheet(style_line)
        style_file.close()
