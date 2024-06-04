from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from GUI.sub_ventanas.custom.utils.css import CBackground
from API.Validaciones import (
    contraseña
)
from GUI.sub_ventanas.custom.validaciones import CustomValidaciones

cValidcion = CustomValidaciones()

class PasswordChange(QWidget, CBackground):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(
            r"GUI\sub_ventanas\ui\cambioDeContraseña.ui", 
            self
        )

        self.inicializar()

        self.cambiarBtn.clicked.connect(self.set_password)

    def inicializar(self) -> None:
        self.pintar()

    def validate_password(self):
        return contraseña(contra=self.password.strip())

    def set_password(self):
        self.password = self.userInput.text()
        if not self.password:
            cValidcion.caja_input_no_valido("Porfavor, asegurese de ingresar una contraseña")
            return None

        is_valid = self.validate_password()

        if not is_valid:
            cValidcion.caja_input_no_valido("La contraseña debe tener mas de 7 caracteres.")
            return None

        # backend, cambiar la contraseña

    def pintar(self) -> None:
        with open(r"GUI\sub_ventanas\css\cambio_contraseña.css", "r") as style_file:
            style_line = style_file.read()

        self.setStyleSheet(style_line)
        style_file.close()
