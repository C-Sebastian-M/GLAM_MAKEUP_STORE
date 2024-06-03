from typing import List

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from GUI.sub_ventanas.utils.css import CBackground

class ReportesDiarios(QWidget, CBackground):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(
            r"GUI\sub_ventanas\ui\reportesDiarios\reportesDiarios.ui", 
            self
        )

class Plantilla(QWidget):
    def __init__(self, title: str, columns: List[str]) -> None:
        pass

    def imprimir(self):
        pass

    def abrir_PDF(self):
        pass
