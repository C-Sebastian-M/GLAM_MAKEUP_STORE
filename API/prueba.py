from API.DATA import GestionDatos
from API.Validaciones import *
import pandas as pd
class Cajero:
    def __init__(self):
        self.gestion_datos = GestionDatos()
        self.df = pd.DataFrame(columns=["Producto","Precio Total"])
    
    def añadir_cliente(self, cedula, nombre, telefono):
        if validar_Cedula(cedula) and validar_NombreCom(nombre) and validacion_Telefono(telefono):
            if not cedula in self.gestion_datos.clientes["Cedula"].values or str(cedula not in self.gestion_datos.clientes["Cedula"].values): #Comprobar si dato ya existe
                self.gestion_datos.agregar_cliente(cedula, nombre, telefono)
                return True
            
            return False
        else:
            return False
                 
    def modificar_cliente(self, cedulaN, nombreN, telefonoN, cedulaO, datosU ):
        if( 
           cedulaN not in self.gestion_datos.clientes["Cedula"].values or
           str(cedulaN not in self.gestion_datos.clientes["Cedula"].values) and
            validar_Cedula(cedulaN) and
            validacion_Telefono(telefonoN) and
            validar_NombreCli(nombreN)
        ): #Caso en el que se actualizan los 3 datos
            nuevos_datos = {
                "Nombre": nombreN,
                "Telefono": telefonoN,
                "Cedula": cedulaN,
            }
            self.gestion_datos.actualizar_cliente(cedulaO, nuevos_datos)
            return True
        
        elif(
            cedulaN == "" and
            validacion_Telefono(telefonoN) and
            validar_NombreCli(nombreN)
        ): #Caso en el que se actualizan el telefono y el nombre
            nuevos_datos = {
                "Nombre": nombreN,
                "Telefono": telefonoN,
                "Cedula": cedulaO,
            }
            self.gestion_datos.actualizar_cliente(cedulaO, nuevos_datos)
            return True
        
        elif(
            cedulaN == "" and
            telefonoN == "" and
            validar_NombreCli(nombreN)
        ): #Caso en el que solo se actualiza el nombre
            nuevos_datos = {
                "Nombre": nombreN,
                "Telefono": datosU["Telefono"],
                "Cedula": cedulaO,
            }
            self.gestion_datos.actualizar_cliente(cedulaO, nuevos_datos)
            return True
        
        elif(
            cedulaN not in self.gestion_datos.clientes["Cedula"].values or 
            str(cedulaN not in self.gestion_datos.clientes["Cedula"].values) and
             validar_Cedula(cedulaN) and
             nombreN == "" and
             telefonoN == ""
        ):#Caso en el que solo se actualiza la cedula
            nuevos_datos = {
                "Nombre": datosU["Nombre"],
                "Telefono": datosU["Telefono"],
                "Cedula": cedulaN,
            }
            self.gestion_datos.actualizar_cliente(cedulaO, nuevos_datos)
            return True

        elif(
            validacion_Telefono(telefonoN) and
            cedulaN == "" and
            nombreN == ""
        ):#Caso en el que solo se actualiza el telefono
            nuevos_datos = {
                "Nombre": datosU["Nombre"],
                "Telefono": telefonoN,
                "Cedula": cedulaO,
            }
            self.gestion_datos.actualizar_cliente(cedulaO, nuevos_datos)
            return True
        
        elif (
            cedulaN not in self.gestion_datos.clientes["Cedula"].values 
            or str(cedulaN not in self.gestion_datos.clientes["Cedula"].values) and
            validacion_Telefono(telefonoN) and
            validar_Cedula(cedulaN) and
            nombreN == ""
        ): #Caso en el que se actualiza el telefono y cedula
            nuevos_datos = {
                "Nombre": datosU["Nombre"],
                "Telefono": telefonoN,
                "Cedula": cedulaN,
            }
            self.gestion_datos.actualizar_cliente(cedulaO, nuevos_datos)
            return True
        
        elif(cedulaN not in self.gestion_datos.clientes["Cedula"].values 
             or str(cedulaN not in self.gestion_datos.clientes["Cedula"].values) and
             validar_NombreCom(nombreN) and
             validar_Cedula(cedulaN) and
             telefonoN == ""
        ): #Cedula y nombre
            nuevos_datos = {
                "Nombre": nombreN,
                "Telefono": datosU["Telefono"],
                "Cedula": cedulaN,
            }
            self.gestion_datos.actualizar_cliente(cedulaO, nuevos_datos)
            return True

        else:
            return False
        
    def reporte_diario(self):
        pass
    
    def validar_stock(self, x):
        if x <= self.gestion_datos.productos["Producto disponible"]:
            return True
        return False
    
    def mostra_total_productos(self,codigo_barras,cantidad):
        if(
            codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values or
            str(codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values) and
            validacion_Codigo_Barras(codigo_barras) and
            validar_cantidad(cantidad)
        ):
          if codigo_barras in  self.gestion_datos.productos["Codigo de barras"]: 
            x = self.self.gestion_datos.productos[self.self.gestion_datos.productos['Codigo de barras']== codigo_barras]
            fila = {'Producto': x["Referencia"], 'Precio total':(float(x["Precio venta"]) * cantidad)}
            self.df.loc[len(self.df)+1] = fila
            return self.df
     
    def comprar_servicio(self, producto, cantidad):
        #Necesitamos que hagan los cambios en la tabla inventario
        pass
    
    def mostra_total_servicios(self):
        pass 
    
    def seleccionar_mediopago(self):
        #Necesitamos que creen la tabla de medios de pago
        pass
    
class Inventario:
    def __init__(self):
        self.gestion_datos = GestionDatos()

    def crear_productos(self, referencia, precioA, precioV, codigoB, marca, stock):
        if validacion_Referencia(referencia) and validacion_Precio(precioA) and validacion_Precio(precioV) and validacion_Codigo_Barras(codigoB) and validacion_Marca(marca) and validacion_Stock(stock):
            if not codigoB in self.gestion_datos.productos["Codigo de barras"].values:
                self.gestion_datos.agregar_producto(referencia, codigoB, marca, precioA, precioV, stock)
                return True
            return False
        return False
    
    def modificar_producto(self,referencia, codigo_barras, marca, precio_adquisicion, precio_venta, unidades_actuales,barrasO,datosP):
       
        if(
            codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values or
            str(codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values) and
            validacion_Codigo_Barras(codigo_barras) and
            validar_NombreCli(referencia) and
            validar_NombreCli(marca) and
            validacion_Precio(precio_adquisicion) and
            validacion_Precio(precio_venta) and
            validacion_Stock(unidades_actuales)
       ): #Caso en el que se actualizan Todos
            nuevos_datos = {
                "Codigo de barras": codigo_barras,
                "Referencia": referencia,
                "Marca": marca,
                "Precio venta": int(precio_venta),
                "Precio de adquisicion": int(precio_adquisicion),
                "Unidades actuales": int(unidades_actuales)
            }
            self.gestion_datos.actualizar_producto(barrasO, nuevos_datos)
            return True
        
        elif(
            codigo_barras == "" and
            validar_NombreCli(referencia) and
            marca == "" and
            precio_adquisicion == "" and
            precio_venta == "" and
            unidades_actuales == ""
       ): # Modificar solo referencia
            nuevos_datos = {
                "Codigo de barras": barrasO,
                "Referencia": referencia,
                "Marca": datosP["Marca"],
                "Precio venta": int(datosP["Precio venta"]),
                "Precio adquisicion": int(datosP["Precio de adquisicion"]),
                "Unidades actuales": int(datosP["Unidades actuales"])
            }
            self.gestion_datos.actualizar_producto(barrasO, nuevos_datos)
            return True

        elif(
            codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values or
            str(codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values) and
            validacion_Codigo_Barras(codigo_barras) and
            referencia == "" and
            marca == "" and
            precio_adquisicion == "" and
            precio_venta == "" and
            unidades_actuales == "" 
        ): # Modificar solo codigo barras
            nuevos_datos = {
                "Codigo de barras": codigo_barras,
                "Referencia": datosP["Referencia"],
                "Marca": datosP["Marca"],
                "Precio venta": int(datosP["Precio venta"]),
                "Precio adquisicion": int(datosP["Precio de adquisicion"]),
                "Unidades actuales": int(datosP["Unidades actuales"])
            }
            self.gestion_datos.actualizar_producto(barrasO, nuevos_datos)
            return True
        
        elif(
            codigo_barras == "" and
            referencia == "" and
            validar_NombreCli(marca) and
            precio_adquisicion == "" and
            precio_venta == "" and
            unidades_actuales == ""
       ): # Modificar solo marca
            nuevos_datos = {
                "Codigo de barras": barrasO,
                "Referencia": datosP["Referencia"],
                "Marca": marca,
                "Precio venta": int(datosP["Precio venta"]),
                "Precio adquisicion": int(datosP["Precio de adquisicion"]),
                "Unidades actuales": int(datosP["Unidades actuales"])
            }
            self.gestion_datos.actualizar_producto(barrasO, nuevos_datos)
            return True 
    
        elif(
            codigo_barras == "" and
            referencia == "" and
            marca == "" and
            validacion_Precio(precio_adquisicion) and
            precio_venta == "" and
            unidades_actuales == ""
        ): #Modificar solo precio adquisicion
            nuevos_datos = {
                "Codigo de barras": barrasO,
                "Referencia": datosP["Referencia"],
                "Marca": datosP["Marca"],
                "Precio venta": int(datosP["Precio venta"]),
                "Precio adquisicion": int(precio_adquisicion),
                "Unidades actuales": int(datosP["Unidades actuales"])
            }
            self.gestion_datos.actualizar_producto(barrasO, nuevos_datos)
            return True    

        elif(
            codigo_barras == "" and
            referencia == "" and
            marca == "" and
            validacion_Precio(precio_venta) and
            precio_adquisicion == "" and
            unidades_actuales == ""
       ): # Modificar solo precio venta
            nuevos_datos = {
                "Codigo de barras": barrasO,
                "Referencia": datosP["Referencia"],
                "Marca": datosP["Marca"],
                "Precio adquisicion": int(datosP["Precio adquisicion"]),
                "Precio venta": int(precio_venta),
                "Unidades actuales": int(datosP["Unidades actuales"])
            }
            self.gestion_datos.actualizar_producto(barrasO, nuevos_datos)
            return True
        
        elif(
            codigo_barras == "" and
            referencia == "" and
            marca == "" and
            precio_adquisicion == "" and
            precio_venta == "" and
            validacion_Stock(unidades_actuales)
       ): # Modificar solo unidades actuales
            nuevos_datos = {
                "Codigo de barras": barrasO,
                "Referencia": datosP["Referencia"],
                "Marca": datosP["Marca"],
                "Precio venta": int(datosP["Precio venta"]),
                "Precio adquisicion": int(datosP["Precio adquisicion"]),
                "Unidades actuales": int(unidades_actuales)
            }
            self.gestion_datos.actualizar_producto(barrasO, nuevos_datos)
            return True
        
        elif(
            codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values or
            str(codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values) and
            validacion_Referencia(referencia) and
            marca == "" and
            precio_venta == "" and
            precio_venta == "" and
            unidades_actuales == ""
       ): # referencia y codigo de barras
            nuevos_datos = {
                "Codigo de barras": codigo_barras,
                "Referencia": referencia,
                "Marca": datosP["Marca"],
                "Precio venta": int(datosP["Precio venta"]),
                "Precio adquisicion": int(datosP["Precio adquisicion"]),
                "Unidades actuales": int(datosP["Referencia"])
            }
            self.gestion_datos.actualizar_producto(barrasO, nuevos_datos)
            return True
        
        elif(
            codigo_barras == "" and
            validar_NombreCli(referencia) and
            validar_NombreCli(marca) and
            precio_adquisicion == "" and
            precio_venta == "" and
            unidades_actuales == ""
       ): # Modificar referanci y marca
            nuevos_datos = {
                "Codigo de barras": barrasO,
                "Referencia": referencia,
                "Marca": marca,
                "Precio venta": int(datosP["Precio venta"]),
                "Precio adquisicion": int(datosP["Precio de adquisicion"]),
                "Unidades actuales": int(datosP["Unidades actuales"])
            }
            self.gestion_datos.actualizar_producto(barrasO, nuevos_datos)
            return True
        
        elif(
            codigo_barras == "" and
            validar_NombreCli(referencia) and
            marca == "" and
            validacion_Precio(precio_adquisicion) and
            precio_venta == "" and
            unidades_actuales == ""
       ): # Modificar referancia y precio adquisicion
            nuevos_datos = {
                "Codigo de barras": barrasO,
                "Referencia": referencia,
                "Marca": datosP["Marca"],
                "Precio venta": int(datosP["Precio venta"]),
                "Precio adquisicion": int(precio_adquisicion),
                "Unidades actuales": int(datosP["Unidades actuales"])
            }
            self.gestion_datos.actualizar_producto(barrasO, nuevos_datos)
            return True
        
        elif(
            codigo_barras == "" and
            validar_NombreCli(referencia) and
            marca == "" and
            precio_adquisicion == "" and
            validacion_Precio(precio_venta) and
            unidades_actuales == ""
       ): # Modificar referancia y precio venta
            nuevos_datos = {
                "Codigo de barras": barrasO,
                "Referencia": referencia,
                "Marca": datosP["Marca"],
                "Precio venta": int(datosP["Precio venta"]),
                "Precio adquisicion": int(precio_venta),
                "Unidades actuales": int(datosP["Unidades actuales"])
            }
            self.gestion_datos.actualizar_producto(barrasO, nuevos_datos)
            return True
        
        elif(
            codigo_barras == "" and
            validar_NombreCli(referencia) and
            marca == "" and
            precio_adquisicion == "" and
            precio_venta == "" and
            validacion_Stock(unidades_actuales)
       ): # Modificar referancia y stock
            nuevos_datos = {
                "Codigo de barras": barrasO,
                "Referencia": referencia,
                "Marca": datosP["Marca"],
                "Precio venta": int(datosP["Precio venta"]),
                "Precio adquisicion": int(datosP["Precio adquisicion"]),
                "Unidades actuales": unidades_actuales
            }
            self.gestion_datos.actualizar_producto(barrasO, nuevos_datos)
            return True
        
        elif(
            codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values or
            str(codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values)and
            validacion_Codigo_Barras(codigo_barras) and 
            validar_NombreCli(referencia) and
            validar_NombreCli(marca) == "" and
            precio_adquisicion == "" and
            precio_venta == "" and
            unidades_actuales == ""
       ): # Modificar referancia y codigo barras y marca
            nuevos_datos = {
                "Codigo de barras": barrasO,
                "Referencia": referencia,
                "Marca": marca,
                "Precio venta": int(datosP["Precio venta"]),
                "Precio adquisicion": int(datosP["Precio adquisicion"]),
                "Unidades actuales": unidades_actuales
            }
            self.gestion_datos.actualizar_producto(barrasO, nuevos_datos)
            return True
        
        elif(
            codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values or
            str(codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values)and
            validacion_Codigo_Barras(codigo_barras) and
            validar_NombreCli(referencia) and
            marca == "" and
            validacion_Precio(precio_adquisicion) == "" and
            precio_venta == "" and
            unidades_actuales==""
       ): # Modificar referancia codigo de barras y precio adquisicion
            nuevos_datos = {
                "Codigo de barras": barrasO,
                "Referencia": referencia,
                "Marca": datosP["Marca"],
                "Precio venta": int(datosP["Precio venta"]),
                "Precio adquisicion": int(precio_adquisicion),
                "Unidades actuales": int(datosP["Unidades actuales"])
            }
            self.gestion_datos.actualizar_producto(barrasO, nuevos_datos)
            return True
        
        elif(
            codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values or
            str(codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values)and
            validacion_Codigo_Barras(codigo_barras) and
            validar_NombreCli(referencia) and
            validacion_Codigo_Barras(codigo_barras) and
            precio_adquisicion == "" and
            validacion_Precio(precio_venta) and
            unidades_actuales==""
       ): # Modificar referancia codigo de barras y precio venta
            nuevos_datos = {
                "Codigo de barras": codigo_barras,
                "Referencia": referencia,
                "Marca": datosP["Marca"],
                "Precio venta": int(precio_venta),
                "Precio adquisicion": int(datosP["Precio adquisicion"]),
                "Unidades actuales": datosP["Unidades actuales"]
            }
            self.gestion_datos.actualizar_producto(barrasO, nuevos_datos)
            return True
        
        elif(
            codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values or
            str(codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values)and
            validacion_Codigo_Barras(codigo_barras) and
            validar_NombreCli(referencia) and
            marca == "" and
            precio_adquisicion == "" and
            precio_venta == "" and
            validacion_Stock(unidades_actuales)
       ): # Modificar referancia codigo de barras y unidades actuales
            nuevos_datos = {
                "Codigo de barras": barrasO,
                "Referencia": referencia,
                "Marca": datosP["Marca"],
                "Precio venta": int(datosP["Precio venta"]),
                "Precio adquisicion": int(datosP["Precio adquisicion"]),
                "Unidades actuales": unidades_actuales
            }
            self.gestion_datos.actualizar_producto(barrasO, nuevos_datos)
            return True
        
        elif(
            codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values or
            str(codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values)and
            validacion_Codigo_Barras(codigo_barras) and
            validar_NombreCli(referencia) and
            validacion_Marca(marca) and
            validacion_Precio(precio_adquisicion) and
            precio_venta == "" and
            unidades_actuales==""
       ): # Modificar referencia, codigo de barras, marca y precio_adquisicion
            nuevos_datos = {
                "Codigo de barras": barrasO,
                "Referencia": referencia,
                "Marca": marca,
                "Precio venta": int(datosP["Precio venta"]),
                "Precio adquisicion": int(precio_adquisicion),
                "Unidades actuales": int(datosP["Unidades actuales"])
            }
            self.gestion_datos.actualizar_producto(barrasO, nuevos_datos)
            return True
        
        elif(
            codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values or
            str(codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values)and
            validar_NombreCli(referencia) and
            validacion_Codigo_Barras(codigo_barras) and
            marca == "" and
            precio_adquisicion == "" and
            validacion_Precio(precio_adquisicion) and
            unidades_actuales == ""
       ): # Modificar referencia, codigo de barras, marca y precio_venta
            nuevos_datos = {
                "Codigo de barras": codigo_barras,
                "Referencia": referencia,
                "Marca": datosP["Marca"],
                "Precio venta": int(datosP["Precio venta"]),
                "Precio adquisicion": int(precio_adquisicion),
                "Unidades actuales": int(datosP["Unidades actuaes"])
            }
            self.gestion_datos.actualizar_producto(barrasO, nuevos_datos)
            return True
       
        elif(
            codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values or
            str(codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values)and
            validacion_Codigo_Barras(codigo_barras) and
            validar_NombreCli(referencia) and
            validacion_Marca(marca) and
            precio_adquisicion == "" and
            precio_venta == "" and
            validar_cantidad(unidades_actuales)
       ): # Modificar referencia, codigo de barras, marca y precio_adquisicion
            nuevos_datos = {
                "Codigo de barras": barrasO,
                "Referencia": referencia,
                "Marca": marca,
                "Precio venta": int(datosP["Precio venta"]),
                "Precio adquisicion": int(datosP["Precio adquisicion"]),
                "Unidades actuales": int(unidades_actuales)
            }
            self.gestion_datos.actualizar_producto(barrasO, nuevos_datos)
            return True
     
        elif(
            codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values or
            str(codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values)and
            validacion_Codigo_Barras(codigo_barras) and
            validar_NombreCli(referencia) and
            validacion_Marca(marca) and
            precio_adquisicion == "" and
            validacion_Precio(precio_venta) and
            unidades_actuales == ""
       ): # Modificar referencia, codigo de barras, marca, precio de adquisicion y precio de venta
            nuevos_datos = {
                "Codigo de barras": codigo_barras,
                "Referencia": referencia,
                "Marca": marca,
                "Precio venta": int(precio_venta),
                "Precio adquisicion": int(datosP["Precio adquisicion"]),
                "Unidades actuales": int(datosP["Unidades actuales"])
            }
            self.gestion_datos.actualizar_producto(barrasO, nuevos_datos)
            return True
        
        elif(
            codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values or
            str(codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values)and
            validacion_Codigo_Barras(codigo_barras) and
            validar_NombreCli(referencia) and
            validacion_Marca(marca) and
            validacion_Precio(precio_adquisicion) == "" and
            precio_venta == "" and
            validar_cantidad(unidades_actuales)
       ): # Modificar referencia, codigo de barras, marca, precio adquisicion y unidades actuales
            nuevos_datos = {
                "Codigo de barras": barrasO,
                "Referencia": referencia,
                "Marca": marca,
                "Precio venta": int(datosP["Precio venta"]),
                "Precio adquisicion": int(precio_adquisicion),
                "Unidades actuales": int(unidades_actuales)
            }
            self.gestion_datos.actualizar_producto(barrasO, nuevos_datos)
            return True
        
        # Modificar todos los datos <- Ya esta
        # Modificar solo referencia <- Ya esta
        # Modificar solo codigo barras <- Ya esta
        # Modificar solo marca <- Ya esta
        # Modificar solo precio Adquisicion <- Ya esta
        # Modificar solo precio venta <- Ya esta
        # Modificar solo stock <- Ya esta 
        # Modificar referencia y codigo de barras <- Ya esta
        # Modificar referencia y marca <- Ya esta 
        # Modificar referencia y precio de venta <- Ya esta 
        # Modificar referencia y precio de adquisicion <- Ya esta
        # Modificar referencia y stock <- Ya esta 
        # Modificar referencia codigo de barras y marca <- Ya esta 
        # Modificar referencia, codigo de barras y precio_a <- Ya esta
        # Modificar referencia, codigo de barras y precio venta <- Ya esta
        # Modificar referencia, codigo de barras y unidades actuales <- Ya esta
        # Modificar referencia, codigo de barras, marca y precio_adquisicion <- Ya esta
        # Modificar referencia, codigo de barras, marca y precio_venta <- Ya esta
        # Modificar referencia, codigo de barras, marca y unidades actuales <- Ya esta
        # Modificar referencia, codigo de barras, marca, precio de adquisicion y precio de vebta <- Ya esta 
        # Modificar referencia, codigo de barras, marca, precio de adquisicion y unidades actuales <- Ya esta

    def comprar_stock(self,codigoB,cantidad):
        producto = self.gestion_datos.productos[self.gestion_datos.productos["Codigo de barras"]==codigoB]
        if not producto.empty:
            self.gestion_datos.productos.loc[self.gestion_datos.productos['Codigo de barras'] ==  codigoB, "Unidades actuales"] += cantidad
            self.gestion_datos.guardar_dataframes()
    
    def ver_clientes(self):
        x = self.gestion_datos.Clientes
        return x













