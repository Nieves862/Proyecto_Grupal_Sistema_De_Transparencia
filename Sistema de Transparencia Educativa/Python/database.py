import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',    # Cambia esto si tu base de datos no está en el mismo servidor
        user='root',         # Cambia esto por tu usuario de MySQL
        password='****', # Cambia esto por tu contraseña de MySQL
        database='ispc_g15b' # Nombre de tu base de datos
    )
    return connection