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
<<<<<<< HEAD
                   
    def mostrar_clientes(self): 
        cedulas = []
        nombres = []
        for i in (self.gestion_datos.clientes["Cedula"]):
            cedulas.append(i)
        for i in (self.gestion_datos.clientes["Nombre"]):
            nombres.append(i)
        x = list(zip(nombres,cedulas))
        return x
=======
            
        
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
    
    
   
        
       
>>>>>>> 0f4613dcbb7b14732fdd5e7c2796f7e3d59254a5

    def reporte_diario(self):
        pass

    def mostrar_servicios(self):
        nombre = []
        precio = []
        for i in (self.gestion_datos.servicios["Nombre Servicio"]):
            nombre.append(i)
        for i in (self.gestion_datos.servicios["Costo"]):
            precio.append(i)
        x = list(zip(nombre,precio))
        return x
    
    def mostrar_productos(self):
        nombre = []
        precio = []
        for i in (self.gestion_datos.productos["Referencia"]):
            nombre.append(i)
        for i in (self.gestion_datos.productos["Precio Venta"]):
            precio.append(i)
        x = list(zip(nombre,precio))
        return x
    
    def validar_stock(self, x):
        if x <= self.gestion_datos.productos["Producto disponible"]:
            return True
        return False
     
    def comprar_servicio(self, producto, cantidad):
        #Necesitamos que hagan los cambios en la tabla inventario
        pass
    
    def mostra_total(self):
        #este depende de la compra de productos y servicios
        pass 
    
    def seleccionar_mediopago(self):
        #Necesitamos que creen la tabla de medios de pago
        pass
    
class Inventario:
    def __init__(self, gestion_datos):
        self.gestion_datos = gestion_datos
    
    def ver_productos(self):
        x = self.gestion_datos.productos.columns=["Referencia", "Codigo de barras", "Marca", "Precio de adquisicion", "Precio venta", "Unidades actuales", "Producto disponible", "Fecha"]
        return x

    def crear_productos(self, referencia, precioA, precioV, codigoB, marca, stock):
        if validacion_Referencia(referencia) and validacion_Precio(precioA) and validacion_Precio(precioV) and validacion_Codigo_Barras(codigoB) and validacion_Marca(marca) and validacion_Stock(stock):
            self.gestion_datos.agregar_producto(referencia, codigoB, marca, precioA, precioV, stock)
            return True
        return False
            
    
x = GestionDatos("Prueba.xlsx")
y = Cajero(x)
<<<<<<< HEAD
z = Inventario(x)
print(z.ver_productos())



=======
>>>>>>> 0f4613dcbb7b14732fdd5e7c2796f7e3d59254a5






