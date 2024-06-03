from datetime import datetime
from PyQt5.QtWidgets import QMessageBox

class CustomValidaciones:
    def validar_fechas(self, rango_fechas: str) -> bool:
        fecha1, fecha2 = rango_fechas.split(" - ")

        # Definir el formato de fecha
        formato = "%Y-%m-%d"
        # Convertir las cadenas de fecha a objetos datetime
        fecha1 = datetime.strptime(fecha1, formato)
        fecha2 = datetime.strptime(fecha2, formato)

        if fecha1 > fecha2:
            return False

        return True

    def validar_condicional(self, cadena: str) -> bool:
        delimiters = ['>', '<', '>=', '<=', '=', 'equal', 'greaterThan', 'lessThan']
        cadena = self._remover_espacios(cadena) if len(cadena) >= 2 else cadena

        if cadena.isdigit():
            return True

        if cadena[0] in delimiters:
            cadena_sep: str = self._separar(cadena, cadena[0])
            if len(cadena_sep) > 2 or not cadena_sep[1].isdigit() or not self.__is_float(cadena_sep[1]):
                return False 
            return True

        cadena_sep = None
        for delimiter in delimiters:
            if delimiter in cadena: # cuando encuentro el delimiter
                if delimiter == '>' or delimiter == '<':
                    posicion = cadena.find(delimiter)
                    delimiter = delimiter + '=' if cadena[posicion + 1] == '=' else delimiter

                cadena_sep = self._separar(cadena, delimiter)
                break

        print(cadena_sep)
        if cadena_sep is not None:
            if len(cadena_sep) > 2:
                return False
            if (cadena_sep[0].isdigit() or self.__is_float(cadena_sep[0])) and (cadena_sep[1].isdigit() or self.__is_float(cadena_sep[1])):
                return True

        return False

    def _separar(self, cadena: str, delimiter: str) -> str:
        return cadena.strip().split(sep=delimiter)

    def _remover_espacios(self, cadena: str):
        if '.' in cadena:
            cadena.replace('.', '_')

        dummy = 0
        list_cadena = list(cadena)
        while dummy < len(list_cadena) - 1:
            if ord(list_cadena[dummy]) == 32:
                list_cadena.pop(dummy)
                continue
            dummy += 1
        return "".join(list_cadena)
    
    def __is_float(self, cadena: str):
        try:
           float(cadena)
           return True
        except ValueError:
           return False

    def caja_input_no_valido(self, mensaje: str):
        caja = QMessageBox()
        caja.setWindowTitle("Input no valido")
        caja.setText(mensaje)

        salir = caja.exec_()


prueba = CustomValidaciones()
