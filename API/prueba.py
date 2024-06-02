from API.DATA import GestionDatos
from API.Validaciones import *
import pandas as pd
import datetime
class Cajero:
    def __init__(self):
        self.gestion_datos = GestionDatos()

    def crear_dataframe(self):
        self.gestion_datos.crear_dataframes()
        
    def buscar_y_modificar_cliente(self, cedula, nuevos_datos):
        #Parámetros:
        #- cedula: La cédula del cliente a buscar.
        #- nuevos_datos: Un diccionario con los datos a actualizar.
    
            if cedula in self.gestion_datos.clientes["Cedula"].values:
                cliente_index = self.gestion_datos.clientes.index[self.gestion_datos.clientes["Cedula"] == cedula].tolist()[0]
                for key, value in nuevos_datos.items():
                    if key in self.gestion_datos.clientes.columns:
                        self.gestion_datos.clientes.at[cliente_index, key] = value
                self.gestion_datos.guardar_dataframes()
                return True
            else:
                return False
    
    def eliminar_cliente(self, cedula):
        if cedula in self.gestion_datos.clientes["Cedula"].values:
            self.gestion_datos.clientes = self.gestion_datos.clientes[self.gestion_datos.clientes["Cedula"] != cedula]
            self.gestion_datos.guardar_dataframes()
            return True
        else:
            return False
    
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
      
    def login(self, username, password, user_role=-1):
            usuario_datos = self.gestion_datos.usuarios[self.gestion_datos.usuarios["usuario"] == username]
            if not usuario_datos.empty:
                if password in usuario_datos["contraseña"].values:
                    user_role = usuario_datos.loc[0,"Rol ID"]     
                    return user_role
                else:
                    return False
            else:
                return False
      
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
            
            
            
x = Cajero()
