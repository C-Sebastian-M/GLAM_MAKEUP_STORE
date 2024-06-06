import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "3245619850",
    database = "glam_makeup_store"
)

cursor = db.cursor()

cursor.execute("CREATE TABLE ")
