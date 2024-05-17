import pandas as pd
from openpyxl import load_workbook


class GestionDatos:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.crear_dataframes()
        self.guardar_dataframes()
        self.ajustar_columnas_excel()

    def crear_dataframes(self):
        columnas_clientes = ["Cedula", "Nombre", "Telefono"]
        columnas_productos = ["Referencia", "Codigo de barras", "Marca", "Precio de adquisicion", "Precio venta",
                              "Unidades actuales"]
        columnas_venta_productos = ["ID venta", "Cliente", "Producto", "Fecha", "Cantidad", "Subtotal"]
        columnas_venta_servicios = ["ID venta", "Cliente", "Servicio", "Fecha", "Costo"]
        columnas_servicios = ["ID servicio", "Nombre Servicio", "Costo"]
        columnas_contraseñas = ["Usuario", "Contraseña", "Rol"]
        columnas_inventario = ["Producto", "Stock"]

        self.clientes = pd.DataFrame(columns=columnas_clientes)
        self.productos = pd.DataFrame(columns=columnas_productos)
        self.venta_productos = pd.DataFrame(columns=columnas_venta_productos)
        self.venta_servicios = pd.DataFrame(columns=columnas_venta_servicios)
        self.servicios = pd.DataFrame(columns=columnas_servicios)
        self.contraseñas = pd.DataFrame(columns=columnas_contraseñas)
        self.inventario = pd.DataFrame(columns=columnas_inventario)

    def guardar_dataframes(self):
        with pd.ExcelWriter(self.nombre_archivo) as writer:
            self.clientes.to_excel(writer, sheet_name='Clientes', index=False)
            self.productos.to_excel(writer, sheet_name='Productos', index=False)
            self.venta_productos.to_excel(writer, sheet_name='VentaProductos', index=False)
            self.venta_servicios.to_excel(writer, sheet_name='VentaServicios', index=False)
            self.servicios.to_excel(writer, sheet_name='Servicios', index=False)
            self.contraseñas.to_excel(writer, sheet_name='Contraseñas', index=False)
            self.inventario.to_excel(writer, sheet_name='Inventario', index=False)

    def ajustar_columnas_excel(self):
        archivo = load_workbook(self.nombre_archivo)
        for hoja in archivo.sheetnames:
            hoja_actual = archivo[hoja]
            for columnas in hoja_actual.columns:
                max_length = 0
                columna = [celda for celda in columnas]
                for celda in columna:
                    try:
                        if len(str(celda.value)) > max_length:
                            max_length = len(str(celda.value))
                    except:
                        pass
                ajusta_ancho = (max_length + 2)
                columna_letra = columna[0].column_letter
                hoja_actual.column_dimensions[columna_letra].width = ajusta_ancho
        archivo.save(self.nombre_archivo)

    def verificar_admin_existente(self):
        return 'Admin' in self.contraseñas['Rol'].values

    def verificar_stock_no_negativo(self):
        return all(self.inventario['Stock'] >= 0)

    def realizar_verificaciones(self):
        if not self.verificar_admin_existente():
            print("Advertencia: No hay usuarios administradores en el sistema.")
        if not self.verificar_stock_no_negativo():
            print("Error: El stock no puede ser negativo en el inventario.")


# Uso de la clase
gestion_datos = GestionDatos("datos.xlsx")
gestion_datos.realizar_verificaciones()
