from DATA import GestionDatos
from Validaciones import *
class Cajero:
    def __init__(self, gestion_datos):
        self.gestion_datos = gestion_datos

    def crear_dataframe(self):
        self.gestion_datos.crear_dataframes()
    
    def login(self, usuario, contraseña):
        if usuario in self.gestion_datos.contraseñas["Usuario"].values and contraseña in self.gestion_datos.contraseñas["Contraseña"].values:
            return True
        else:
            return False

    def añadir_cliente(self, cedula, nombre, telefono):
        if validar_Cedula(cedula) and validar_NombreCom(nombre) and validacion_Telefono(telefono):
            if not cedula in self.gestion_datos.clientes["Cedula"].values: #Comprobar si dato ya existe
                self.gestion_datos.agregar_cliente(cedula, nombre, telefono)
                return True
            
            return False
        else:
            return False
            
        
    def mostrar_clientes(self): 
        return self.gestion_datos.clientes.loc[:,["Nombre","Cedula"]]

    def reporte_diario(self):
        pass

    def mostrar_servicios(self):
        return self.gestion_datos.servicios.loc[:,["Nombre","Costo"]]

    def mostrar_productos(self):
        return self.gestion_datos.productos.loc[:,["Referencia","Precio venta"]]
    
    def agregar_usuario(self, usuario, contraseña,rol):
        self.gestion_datos.agregar_contraseña(usuario, contraseña, rol)
    
    def comprar_producto(self, producto, cantidad):
        #Necesitamos que hagan los cambios en la tabla inventario
        pass
    
    def comprar_servicio(self, producto, cantidad):
        #Necesitamos que hagan los cambios en la tabla inventario
        pass
    
    def mostra_total(self):
        #este depende de la compra de productos y servicios
        pass 
    
    def seleccionar_mediopago(self):
        #Necesitamos que creen la tabla de medios de pago
        pass
    
    
   
        
       

x = GestionDatos("Prueba.xlsx")
y = Cajero(x)






