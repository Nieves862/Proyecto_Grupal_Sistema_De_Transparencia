import mysql.connector
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',         
        password='tu clave', 
        database='gestion_usuarios',
        port=3306
    )
    return connection
