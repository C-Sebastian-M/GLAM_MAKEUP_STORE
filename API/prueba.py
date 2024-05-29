from DATA import GestionDatos
from Validaciones import *
class Cajero:
    def __init__(self, gestion_datos):
        self.gestion_datos = gestion_datos

    def crear_dataframe(self):
        self.gestion_datos.crear_dataframes()

    def añadir_cliente(self, cedula, nombre, telefono):
        if validar_Cedula(cedula) and validar_NombreCom(nombre) and validacion_Telefono(telefono):
            if not cedula in self.gestion_datos.clientes["Cedula"].values: #Comprobar si dato ya existe
                self.gestion_datos.agregar_cliente(cedula, nombre, telefono)
                return True
            
            return False
        else:
            return False
            
        
    def seleccionar_cliente(self): 
        return self.gestion_datos.clientes.loc[:,["Nombre","Cedula"]]
       

x = GestionDatos("Prueba.xlsx")
y = Cajero(x)
y.añadir_cliente(12356784, "Daniel", 4566666660)
y.añadir_cliente(12356684, "Daniel", 4566666660)
print(y.seleccionar_cliente())



