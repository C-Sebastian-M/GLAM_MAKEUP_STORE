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
    
    def login(self,username, password):
        usuario_datos = self.gestion_datos.usuarios[self.gestion_datos.usuarios["usuario"] == username]
        if not usuario_datos.empty:
            if password in usuario_datos["contraseña"].values:
                rol = usuario_datos["Rol ID"].values
                return int(rol)
            return False
        return False
    #REPORTES  
class Reportes:
    def filtrar_productos(self, referencia=None, codigo_barras=None, marca=None,
                      precio_adquisicion=None, stock=None, precio_venta=None, comparacion_precio_venta=None,
                      fecha_min=None, fecha_max=None):
        filtered_products = self.productos.copy()
    
        if referencia is not None:
            filtered_products = filtered_products[filtered_products["Referencia"] == referencia]
        if codigo_barras is not None:
            filtered_products = filtered_products[filtered_products["Codigo de barras"] == codigo_barras]
        if marca is not None:
            filtered_products = filtered_products[filtered_products["Marca"] == marca]
        if precio_adquisicion is not None:
            filtered_products = filtered_products[filtered_products["Precio de adquisicion"] == precio_adquisicion]
        if stock is not None:
            filtered_products = filtered_products[filtered_products["Unidades actuales"] == stock]
        if precio_venta is not None and comparacion_precio_venta is not None:
            if comparacion_precio_venta == "menor":
                filtered_products = filtered_products[filtered_products["Precio venta"] < precio_venta]
            elif comparacion_precio_venta == "mayor":
                filtered_products = filtered_products[filtered_products["Precio venta"] > precio_venta]
            elif comparacion_precio_venta == "igual":
                filtered_products = filtered_products[filtered_products["Precio venta"] == precio_venta]
            else:
                print("Error: Comparación de precio de venta no válida.")
        if fecha_min is not None:
            fecha_min = datetime.strptime(fecha_min, "%d/%m/%Y")
            filtered_products = filtered_products[filtered_products["Fecha"] >= fecha_min]
        if fecha_max is not None:
            fecha_max = datetime.strptime(fecha_max, "%d/%m/%Y")
            filtered_products = filtered_products[filtered_products["Fecha"] <= fecha_max]
    
        return filtered_products
    
    def filtrar_servicios(self, nombre=None, id_servicio=None, precio=None, comparacion_precio=None,
                     fecha_min=None, fecha_max=None):
        filtered_services = self.servicios.copy()
    
        if nombre is not None:
            filtered_services = filtered_services[filtered_services["Nombre Servicio"] == nombre]
        if id_servicio is not None:
            filtered_services = filtered_services[filtered_services["ID servicio"] == id_servicio]
        if precio is not None and comparacion_precio is not None:
            if comparacion_precio == "menor":
                filtered_services = filtered_services[filtered_services["Costo"] < precio]
            elif comparacion_precio == "mayor":
                filtered_services = filtered_services[filtered_services["Costo"] > precio]
            elif comparacion_precio == "igual":
                filtered_services = filtered_services[filtered_services["Costo"] == precio]
            else:
                print("Error: Comparación de precio no válida.")
        if fecha_min is not None:
            fecha_min = datetime.strptime(fecha_min, "%d/%m/%Y")
            filtered_services = filtered_services[filtered_services["Fecha"] >= fecha_min]
        if fecha_max is not None:
            fecha_max = datetime.strptime(fecha_max, "%d/%m/%Y")
            filtered_services = filtered_services[filtered_services["Fecha"] <= fecha_max]
    
        return filtered_services
                         
    def filtrar_ventas(self, id_venta=None, cantidad=None, cliente=None, subtotal=None, comparacion_subtotal=None,
                   producto_o_servicio=None, fecha_min=None, fecha_max=None, id_caja=None):
        filtered_sales = pd.concat([self.venta_productos, self.venta_servicios], ignore_index=True)

        if id_venta is not None:
            filtered_sales = filtered_sales[filtered_sales["ID venta"] == id_venta]
        if cantidad is not None:
            filtered_sales = filtered_sales[filtered_sales["Cantidad"] == cantidad]
        if cliente is not None:
            filtered_sales = filtered_sales[filtered_sales["Cliente"] == cliente]
        if subtotal is not None and comparacion_subtotal is not None:
            if comparacion_subtotal == "menor":
                filtered_sales = filtered_sales[filtered_sales["Subtotal"] < subtotal]
            elif comparacion_subtotal == "mayor":
                filtered_sales = filtered_sales[filtered_sales["Subtotal"] > subtotal]
            elif comparacion_subtotal == "igual":
                filtered_sales = filtered_sales[filtered_sales["Subtotal"] == subtotal]
            else:
                print("Error: Comparación de subtotal no válida.")
        if producto_o_servicio is not None:
            filtered_sales = filtered_sales[filtered_sales["Producto" if "producto" in producto_o_servicio.lower() else "Servicio"] == producto_o_servicio]
        if fecha_min is not None:
            fecha_min = datetime.strptime(fecha_min, "%d/%m/%Y")
            filtered_sales = filtered_sales[filtered_sales["Fecha"] >= fecha_min]
        if fecha_max is not None:
            fecha_max = datetime.strptime(fecha_max, "%d/%m/%Y")
            filtered_sales = filtered_sales[filtered_sales["Fecha"] <= fecha_max]
        if id_caja is not None:
            filtered_sales = filtered_sales[filtered_sales["ID_Caja"] == id_caja]

        return filtered_sales

    #CATALOGO DE SERVICIOS 
class Catalogo_Servicios:
    def crear_servicio(self, id_servicio, nombre_servicio, costo):
        nuevo_servicio = pd.DataFrame([[id_servicio, nombre_servicio, costo]], columns=self.columnas_servicios)
        self.servicios = pd.concat([self.servicios, nuevo_servicio], ignore_index=True)
        self.guardar_dataframes()
        return True

    # Método para modificar un servicio
    def modificar_servicio(self, id_servicio, nuevos_datos):
        servicio = self.servicios[self.servicios["ID servicio"] == id_servicio]
        if not servicio.empty:
            for key, value in nuevos_datos.items():
                if key in self.servicios.columns:
                    self.servicios.loc[self.servicios["ID servicio"] == id_servicio, key] = value
            self.guardar_dataframes()
            return True
        else:
            return False

    # Método para descontinuar un servicio
    def descontinuar_servicio(self, id_servicio):
        servicio = self.servicios[self.servicios["ID servicio"] == id_servicio]
        if not servicio.empty:
            self.servicios = self.servicios[self.servicios["ID servicio"] != id_servicio]
            self.guardar_dataframes()
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
print(x.login("cajero", "cajero"))