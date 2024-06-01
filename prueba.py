from DATA.DATA import GestionDatos
from Validaciones import *
class Cajero:
    def __init__(self, gestion_datos):
        self.gestion_datos = gestion_datos

    def crear_dataframe(self):
        self.gestion_datos.crear_dataframes()
        
    def login(self, usuario, contraseña):
    usuario_datos = self.usuarios[self.usuarios["usuario"] == usuario]
    if not usuario_datos.empty:
        return usuario_datos["contraseña"].values[0] == contraseña
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
        cedulas = []
        nombres = []
        for i in (self.gestion_datos.clientes["Cedula"]):
            cedulas.append(i)
        for i in (self.gestion_datos.clientes["Nombre"]):
            nombres.append(i)
        x = list(zip(nombres,cedulas))
        return x

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
        return self.gestion_datos.productos
        

    def crear_productos(self, referencia, precioA, precioV, codigoB, marca, stock):
        if validacion_Referencia(referencia) and validacion_Precio(precioA) and validacion_Precio(precioV) and validacion_Codigo_Barras(codigoB) and validacion_Marca(marca) and validacion_Stock(stock):
            if not codigoB in self.gestion_datos.productos["Codigo de barras"].values:
                self.gestion_datos.agregar_producto(referencia, codigoB, marca, precioA, precioV, stock)
                return True
            return False
        return False
    
#    def modificar_producto(self,codigoB,nuevos_datos):
#        x = GestionDatos("datos.xlsx")
#        producto = self.gestion_datos.productos[self.gestion_datos.productos["Codigo de barras"]==codigoB]
#        if not producto.empty:
#            for key, value in nuevos_datos.items():
#                if key in self.gestion_datos.productos.columns:
#                    self.gestion_datos.productos.loc[self.gestion_datos.productos['Codigo de barras'] ==  codigoB, key] = value
#            self.gestion_datos.guardar_dataframes()
#            print(f"Producto con código de barra {codigoB} ha sido actualizado.")
#        else:
#            print(f"Producto con código  de barra {codigoB} no encontrado.")
    
    def modificar_producto(self):
        marca=[]
        a = []
        v = []
        for i in (self.gestion_datos.productos["Marca"]):
            marca.append(i)
        for i in (self.gestion_datos.productos["Precio de adquisicion"]):
            a.append(i)
        for i in (self.gestion_datos.productos["Precio venta"]):
            v.append(i)
        x = list(zip(marca,a,v))
        return x
        
    def eliminar_producto(self):
        referecia = []
        barras = []
        marca=[]
        a = []
        v = []
        stock = []
        fecha = []
        for i in (self.gestion_datos.productos["Marca"]):
            marca.append(i)
        for i in (self.gestion_datos.productos["Precio de adquisicion"]):
            a.append(i)
        for i in (self.gestion_datos.productos["Precio venta"]):
            v.append(i)
        for i in (self.gestion_datos.productos["Referencia"]):
            referecia.append(i)
        for i in (self.gestion_datos.productos["Codigo de barras"]):
            barras.append(i)
        for i in (self.gestion_datos.productos["Unidades actuales"]):
            stock.append(i)
        for i in (self.gestion_datos.productos["Fecha"]):
            fecha.append(i)
        x = list(zip(referecia,barras,marca,a,v,stock,fecha))
        return x

    def comprar_stock(self,codigoB,cantidad):
        producto = self.gestion_datos.productos[self.gestion_datos.productos["Codigo de barras"]==codigoB]
        if not producto.empty:
            self.gestion_datos.productos.loc[self.gestion_datos.productos['Codigo de barras'] ==  codigoB, "Unidades actuales"] += cantidad
            self.gestion_datos.guardar_dataframes()
            
            
            
x = GestionDatos("datos.xlsx")
y = Cajero(x)
z = Inventario(x)
z.crear_productos("papas",300,500,1234567890986,"motorola",4)
z.crear_productos("camas",300,500,1234567890988,"iphone",4)
z.crear_productos("zapato",300,500,1234567890989,"Asus",4)
#z.modificar_producto(1234567890986,{"Marca":"kadio","Precio de adquisicion":250,"Precio de venta":450})
print(z.modificar_producto())
print(z.eliminar_producto())
z.comprar_stock(1234567890986,6)
print(z.ver_productos())













