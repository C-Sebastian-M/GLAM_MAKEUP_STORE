import mysql.connector
from mysql.connector import Error


class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        # Establece la conexión a la base de datos.
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("Conexión exitosa a la base de datos")
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")

    def create_table(self, table_name, columns):
        # """Crea una nueva tabla en la base de datos."""
        try:
            create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
            self.cursor.execute(create_table_query)
            self.connection.commit()
            print(f"Tabla {table_name} creada exitosamente")
        except Error as e:
            print(f"Error al crear la tabla: {e}")

    def alter_table(self, table, column, column_definition):
        try:
            alter_table_query = (
                f"ALTER TABLE {table} ADD COLUMN {column} {column_definition}"
            )
            self.cursor.execute(alter_table_query)
            self.connection.commit()
            print(f"Columna {column} agregada a la tabla {table} exitosamente")
        except Error as e:
            print(f"Error al modificar la tabla: {e}")
            
    def check_cliente(self, cedula):
        check = f"SELECT COUNT(*) FROM cliente WHERE cedula = %s"
        self.cursor.execute(check, (cedula,))
        value = self.cursor.fetchone()[0]
        return value
            
    def insert_cliente(self, cedula, nombre, telefono) -> bool:
        try:
            value = self.check_cliente(cedula)
            if value == 0:
                add_cliente = f"INSERT INTO cliente ({cedula}, {nombre}, {telefono}) VALUES (%s, %s, %s)"
                self.cursor.execute(add_cliente)
                self.connection.commit()
                print(f"Cliente {nombre} añadido exitosamente.")
                return True
            return False
        except Error as e:
            print(f"Error al añadir el cliente {nombre}: {e}")
            
    def modify_cliente(self, cedula, nueva_cedula ,nombre, telefono):
        try:
            value = self.check_cliente(cedula)
            if value == 0:
                modify = f"UPDATE cliente SET cedula = %s, nombre = %s, telefono = %s WHERE cedula = %s" 
                self.cursor.execute(modify, (nueva_cedula, nombre, telefono, cedula))
                self.connection.commit()
                return True
            return False
        except Error as e:
            print(f"Error al modificar al ciente con cedula {cedula}: {e}")
            
    def close_connection(self):
        """Cierra la conexión a la base de datos."""
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Conexión a MySQL cerrada")


if __name__ == "__main__":
    db_manager = DatabaseManager(
        host="localhost",
        user="root",
        password="3245619850",
        database="glam_makeup_store",
    )

    db_manager.connect()

    # Ejemplo de creación de una nueva tabla
    """db_manager.create_table(
        "NuevaTabla", "id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(50), edad INT"
    )"""
    #Modificar una tabla, agregarle nueva columna
    """db_manager.alter_table("cliente", "estado", "BOOLEAN DEFAULT FALSE")"""
    
    #db_manager.create_table("", "")

    db_manager.close_connection()
