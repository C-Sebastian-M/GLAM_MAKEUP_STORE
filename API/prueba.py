from API.DATA import GestionDatos
from API.Validaciones import *
import pandas as pd
import datetime 

class Cajero:
    def __init__(self):
        self.gestion_datos = GestionDatos()
        self.df = pd.DataFrame(columns=["Nombre","Precio total"])
        self.serviciosC = pd.DataFrame(columns=["Nombre","Precio total"])
        self.servF = pd.DataFrame(columns=["Nombre","Precio total"])
    
    def añadir_cliente(self, cedula, nombre, telefono):
        if (
            validar_Cedula(cedula)
            and validar_NombreCom(nombre)
            and validacion_Telefono(telefono)
        ):
            if not cedula in self.gestion_datos.clientes["Cedula"].values or str(
                cedula not in self.gestion_datos.clientes["Cedula"].values
            ):  # Comprobar si dato ya existe
                self.gestion_datos.agregar_cliente(cedula, nombre, telefono)
                return True

            return False
        else:
            return False

    def modificar_cliente(self, cedulaN, nombreN, telefonoN, cedulaO, datosU):
        if (
            cedulaN not in self.gestion_datos.clientes["Cedula"].values
            or str(cedulaN not in self.gestion_datos.clientes["Cedula"].values)
            and validar_Cedula(cedulaN)
            and validacion_Telefono(telefonoN)
            and validar_NombreCli(nombreN)
        ):  # Caso en el que se actualizan los 3 datos
            nuevos_datos = {
                "Nombre": nombreN,
                "Telefono": telefonoN,
                "Cedula": cedulaN,
            }
            self.gestion_datos.actualizar_cliente(cedulaO, nuevos_datos)
            return True

        elif (
            cedulaN == ""
            and validacion_Telefono(telefonoN)
            and validar_NombreCli(nombreN)
        ):  # Caso en el que se actualizan el telefono y el nombre
            nuevos_datos = {
                "Nombre": nombreN,
                "Telefono": telefonoN,
                "Cedula": cedulaO,
            }
            self.gestion_datos.actualizar_cliente(cedulaO, nuevos_datos)
            return True

        elif (
            cedulaN == "" and telefonoN == "" and validar_NombreCli(nombreN)
        ):  # Caso en el que solo se actualiza el nombre
            nuevos_datos = {
                "Nombre": nombreN,
                "Telefono": datosU["Telefono"],
                "Cedula": cedulaO,
            }
            self.gestion_datos.actualizar_cliente(cedulaO, nuevos_datos)
            return True

        elif (
            cedulaN not in self.gestion_datos.clientes["Cedula"].values
            or str(cedulaN not in self.gestion_datos.clientes["Cedula"].values)
            and validar_Cedula(cedulaN)
            and nombreN == ""
            and telefonoN == ""
        ):  # Caso en el que solo se actualiza la cedula
            nuevos_datos = {
                "Nombre": datosU["Nombre"],
                "Telefono": datosU["Telefono"],
                "Cedula": cedulaN,
            }
            self.gestion_datos.actualizar_cliente(cedulaO, nuevos_datos)
            return True

        elif (
            validacion_Telefono(telefonoN) and cedulaN == "" and nombreN == ""
        ):  # Caso en el que solo se actualiza el telefono
            nuevos_datos = {
                "Nombre": datosU["Nombre"],
                "Telefono": telefonoN,
                "Cedula": cedulaO,
            }
            self.gestion_datos.actualizar_cliente(cedulaO, nuevos_datos)
            return True

        elif (
            cedulaN not in self.gestion_datos.clientes["Cedula"].values
            or str(cedulaN not in self.gestion_datos.clientes["Cedula"].values)
            and validacion_Telefono(telefonoN)
            and validar_Cedula(cedulaN)
            and nombreN == ""
        ):  # Caso en el que se actualiza el telefono y cedula
            nuevos_datos = {
                "Nombre": datosU["Nombre"],
                "Telefono": telefonoN,
                "Cedula": cedulaN,
            }
            self.gestion_datos.actualizar_cliente(cedulaO, nuevos_datos)
            return True

        elif (
            cedulaN not in self.gestion_datos.clientes["Cedula"].values
            or str(cedulaN not in self.gestion_datos.clientes["Cedula"].values)
            and validar_NombreCom(nombreN)
            and validar_Cedula(cedulaN)
            and telefonoN == ""
        ):  # Cedula y nombre
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
       if codigo_barras in self.gestion_datos.productos["Codigo de barras"].values and cantidad <= 15:
           datos_producto = self.gestion_datos.productos[self.gestion_datos.productos["Codigo de barras"] == (codigo_barras)]
       elif int(codigo_barras) in self.gestion_datos.productos["Codigo de barras"].values and cantidad <= 15:
           datos_producto = self.gestion_datos.productos[self.gestion_datos.productos["Codigo de barras"] == int(codigo_barras)]
       precio = datos_producto["Precio venta"]
       preciot = cantidad*precio
       nuevo_producto = pd.DataFrame([[codigo_barras, preciot]], columns=["Producto","Precio total"])
       self.df = pd.concat([self.df, nuevo_producto], ignore_index=True)
       print(self.df)
        
    def mostra_total_servicios(self, id, cantidad):
        if id in self.gestion_datos.productos["ID servicio"].values:
            datos_producto = self.gestion_datos.productos[self.gestion_datos.productos["ID servicio"] == (id)]
        elif int(id) in self.gestion_datos.productos["ID servicio"].values:
            datos_producto = self.gestion_datos.productos[self.gestion_datos.productos["ID servicio"] == int(id)]
        precio = datos_producto["Costo"]
        preciot = cantidad*precio
        nombre_servicio = datos_producto["Nombre Servicio"]
        nuevo_producto = pd.DataFrame([[nombre_servicio, preciot]], columns=["Servicio" , "Precio total"])
        self.serviciosC = pd.concat([self.df, nuevo_producto], ignore_index=True)

    def df_carro(self):
        for index, fila in self.df.iterrows():
           self.servF = self.servF.append(fila)

        for index, fila in self.serviciosC.iterrows():
           self.servF = self.servF.append(fila)
        return not self.servF.empty
         
    def vaciar_carrito(self):
        #Necesitamos que creen la tabla de medios de pago
        pass

    

class Inventario:
    def __init__(self):
        self.gestion_datos = GestionDatos()

    def crear_productos(self, referencia, precioA, precioV, codigoB, marca, stock):
        if (
            validacion_Referencia(referencia)
            and validacion_Precio(precioA)
            and validacion_Precio(precioV)
            and validacion_Codigo_Barras(codigoB)
            and validacion_Marca(marca)
            and validacion_Stock(stock)
        ):
            print(type(referencia))
            if not codigoB in self.gestion_datos.productos["Codigo de barras"].values:
                self.gestion_datos.agregar_producto(
                    referencia, codigoB, marca, precioA, precioV, stock
                )
                return True
            return False
        return False

    def modificar_producto(
        self, marca, precio_a, precio_v, codigo_barras, datosP):
        if (
            codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values
            or str(codigo_barras not in self.gestion_datos.productos["Codigo de barras"].values)
            and validacion_Marca(marca)
            and validacion_Precio(precio_a)
            and validacion_Precio(precio_v)
        ):  # Caso en el que se actualizan Todos
            
            nuevos_datos = {
                "Codigo de barras": codigo_barras,
                "Referencia": datosP["Referencia"],
                "Marca": marca,
                "Precio venta": float(precio_v),
                "Precio de adquisicion": float(precio_a),
                "Unidades actuales": datosP["Unidades actuales"],
            }
            self.gestion_datos.actualizar_producto(codigo_barras, nuevos_datos)
            return True
        else:
            return False


    def descontinuar_producto(self,codigo):
        GestionDatos.descontinuar_producto(codigo)

    def comprar_stock(self, codigoB, cantidad):
        if codigoB in self.gestion_datos.productos["Codigo de barras"].values:
            print("hola")
        else:
            print("adios")
        producto = self.gestion_datos.productos[
            self.gestion_datos.productos["Codigo de barras"] == codigoB
        ]
        if not producto.empty:
            self.gestion_datos.productos.loc[
                self.gestion_datos.productos["Codigo de barras"] == codigoB,
                "Unidades actuales",
            ] += cantidad
            self.gestion_datos.guardar_dataframes()
    
    def crear_servicio(self, id, nombre_servicio, precio):
        #id nombre servicio y precio
        if (id not in self.gestion_datos.servicios["ID servicio"].values
            or str(id not in self.gestion_datos.servicios["ID servicio"].values)
            and validacion_Stock(id)
            and validar_NombreServ(nombre_servicio)
            and validacion_Precio(precio)
   
        ):
            if not id in self.gestion_datos.servicios["ID servicio"].values:
                self.gestion_datos.agregar_servicio(id,nombre_servicio,precio)
                return True
            return False
        return False
    
    def eliminar_servicio(self,servicio):
        self.gestion_datos.eliminar_servicio(servicio)
    
    def modificar_servicio(self, id, nombreN, precioN, idO,datosS):

        if (idO not in self.gestion_datos.servicios["ID servicio"].values
            or str(idO not in self.gestion_datos.servicios["ID servicio"].values)
            and id  in self.gestion_datos.servicios["ID servicio"].values
            or str(id  in self.gestion_datos.servicios["ID servicio"].values)
            and validacion_Precio(id)
            and validacion_Precio(idO)
            and validar_NombreServ(nombreN)
            and validacion_Precio(precioN)
        ):  # Caso en el que se actualizan Todos
            
            nuevos_datos = {
                "ID servicio": id,
                "Nombre Servicio": nombreN,
                "Costo": precioN
            }
            self.gestion_datos.actualizar_servicio(idO, nuevos_datos)
            return True
        else:
            return False
        
        
class Reportes:
    def __init__(self):
        self.gestion_datos = GestionDatos()
        self.filtrado_productos = pd.DataFrame(columns=["Referencia","Codigo de barras","Marca","Precio de adquisicion", "Precio venta","Unidades actuales","Producto disponible","Fecha"])    
        self.filtrado_servicios = pd.DataFrame(columns= ["ID servicio", "Nombre Servicio", "Costo"])
        
    def filtrar_referencia(self, referencia):
        self.filtrado_productos = (self.gestion_datos.productos[self.gestion_datos.productos["Referencia"]== referencia])
        self.filtrado_productos = self.filtrado_productos.reset_index(drop=True)
        print(self.filtrado_productos)
        return not self.filtrado_productos.empty
    
    def filtrar_codigo_de_barras(self, codB):
        self.filtrado_productos = self.gestion_datos.productos[self.gestion_datos.productos["Codigo de barras"]== codB]
        self.filtrado_productos = self.filtrado_productos.reset_index(drop=True)
        print(self.filtrado_productos)
        return not self.filtrado_productos.empty
    
    def filtrar_marca(self,marca):
        self.filtrado_productos = self.gestion_datos.productos[self.gestion_datos.productos["Marca"]== marca]
        self.filtrado_productos = self.filtrado_productos.reset_index(drop=True)
        print(self.filtrado_productos)
        return not self.filtrado_productos.empty
    
    def filtrar_precioA(self,precio):
        self.filtrado_productos = self.gestion_datos.productos[self.gestion_datos.productos["Precio de adquisicion"]== precio]
        self.filtrado_productos = self.filtrado_productos.reset_index(drop=True)
        print(self.filtrado_productos)
        return not self.filtrado_productos.empty
    
    def filtrar_precioV(self,precio):
        self.filtrado_productos = self.gestion_datos.productos[self.gestion_datos.productos["Precio venta"]== precio]
        self.filtrado_productos = self.filtrado_productos.reset_index(drop=True)
        print(self.filtrado_productos)
        return not self.filtrado_productos.empty
    
    def filtrar_stock(self,unidades):
        self.filtrado_productos = self.gestion_datos.productos[self.gestion_datos.productos["Unidades actuales"]== unidades]
        self.filtrado_productos = self.filtrado_productos.reset_index(drop=True)
        print(self.filtrado_productos)
        return not self.filtrado_productos.empty

    def filtrar_disponibilidad(self,disponibles = True):
        self.filtrado_productos = self.gestion_datos.productos[self.gestion_datos.productos["Producto disponible"]== disponibles]
        self.filtrado_productos = self.filtrado_productos.reset_index(drop=True)
        print(self.filtrado_productos)
        return not self.filtrado_productos.empty
        
    def filtrar_fecha(self,fechas):
        fecha_str1, fecha_str2 = fechas.split(" - ")
        fecha1 = datetime.datetime.strptime(fecha_str1, "%Y-%m-%d")
        fecha2 = datetime.datetime.strptime(fecha_str2, "%Y-%m-%d")
        self.gestion_datos.productos['Fecha'] = pd.to_datetime(self.gestion_datos.productos['Fecha'])
        self.filtrado_productos = self.gestion_datos.productos[(self.gestion_datos.productos['Fecha'] >= fecha1) & (self.gestion_datos.productos['Fecha'] <= fecha2)]
        self.filtrado_productos = self.filtrado_productos.reset_index(drop=True)
        print(self.filtrado_productos)
        return not self.filtrado_productos.empty
    
    def filtrar_ID_Servicio(self,id):
        self.filtrado_servicios = self.gestion_datos.servicios[self.gestion_datos.servicios["ID servicio"]== id]
        self.filtrado_servicios = self.filtrado_productos.reset_index(drop=True)
        return  not self.filtrado_servicios.empty
    
    def filtrar_servicio(self,servicio):
        self.filtrado_servicios = self.gestion_datos.servicios[self.gestion_datos.servicios["Nombre Servicio"]== servicio]
        self.filtrado_servicios= self.filtrado_productos.reset_index(drop=True)
        return not self.filtrado_servicios.empty
    
    def filtrar_costo(self,costo):
        self.filtrado_servicios = self.gestion_datos.servicios[self.gestion_datos.servicios["Costo"]== costo]
        self.filtrado_servicios = self.filtrado_productos.reset_index(drop=True)
        return not self.filtrado_servicios.empty
x = Reportes()
x.filtrar_fecha("2024-06-04 - 2024-06-06")













