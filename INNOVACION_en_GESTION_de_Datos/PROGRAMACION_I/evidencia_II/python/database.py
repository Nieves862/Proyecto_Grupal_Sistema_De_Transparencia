import mysql.connector
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',    
        user='root',         
        password='tu clave', 
        database='tu base de datos' 
    )
    return connection
