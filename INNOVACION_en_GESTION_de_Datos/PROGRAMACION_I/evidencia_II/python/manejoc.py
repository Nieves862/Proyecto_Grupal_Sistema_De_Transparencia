from datetime import datetime #importamos para registrar las horas de conexion
from database import get_db_connection  # Importams la función para conectarnos a la base de datos
import mysql.connector  # importamos el conector

class Sistema:
    def __init__(self):
        self.usuarios = self.cargar_usuarios()  # Cargamos la lista de usuarios al inicializar el sistema

    def cargar_usuarios(self):
        # Establecems la conexión a la base de datos y obtnemoes todos los usuarios
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Usuario")
        usuarios = cursor.fetchall()  # Recuperamos todos los registros de la tabla Usuario
        cursor.close()
        connection.close()
        return usuarios  # Devuelvemos la lista de usuarios

    def agregar_usuario(self, username, password, email):
        # Agregamos un nuevo usuario a la base de datos
        connection = get_db_connection()
        cursor = None  # Inicializamos el cursor como None para evitar  problems en caso de error

        try:
            cursor = connection.cursor()
            # Ejecuta la consulta para insertar el nuevo usuario agraado
            cursor.execute("INSERT INTO Usuario (username, password, email) VALUES (%s, %s, %s)", (username, password, email))
            connection.commit()
            print(f"Usuario {username} agregado exitosamente.")  # Mensaje cuando logramos agragarlo
        except mysql.connector.IntegrityError as err:
            if err.errno == 1062:  # Maneja el error cuando es duplicado el dato ingresado,e s decir ya creamos ese usuaro
                print(f"Error: El nombre de usuario '{username}' ya está en uso. Por favor, elige otro.")
            else:
                print(f"Error al agregar usuario: {err}")  # para el manejo de otros errores
        except mysql.connector.Error as err:
            print(f"Error con la base de datos: {err}")
        finally:
            if cursor is not None:  # se cierra el cursor solo si fue creado
                cursor.close()
            connection.close()  #se cierra la conexión

    def modificar_usuario(self, username, nuevo_username=None, nuevo_password=None, nuevo_email=None):
        # Modificamos un usuario existente en la base de datos
        connection = get_db_connection()
        cursor = connection.cursor()

        query = "UPDATE Usuario SET"  # Iniciamos la consulta de actualización
        values = []
        if nuevo_username:
            query += " username = %s,"  # Agregaoms nuevo username si se proporciona
            values.append(nuevo_username)
        if nuevo_password:
            query += " password = %s,"  # Agregamos nuevo password si se proporciona
            values.append(nuevo_password)
        if nuevo_email:
            query += " email = %s"  # Agregamos nuevo email si se proporciona
            values.append(nuevo_email)
        
        query = query.rstrip(',')  # se leimina la última coma
        query += " WHERE username = %s"  # se crea condición para encontrar el usuario
        values.append(username)

        try:
            cursor.execute(query, tuple(values))  # ejecutamos la consulta de actualización
            connection.commit()
            if cursor.rowcount > 0:  # Verificamos si se modificó algún registro
                print("Usuario modificado exitosamente.")
            else:
                print("Usuario no encontrado.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            connection.close()

    def eliminar_usuario(self, username=None, email=None):
        # Eliminamos un usuario de la base de datos basado en username o email
        connection = get_db_connection()
        cursor = connection.cursor()

        query = "DELETE FROM Usuario WHERE username = %s OR email = %s"  # Consultamos para eliminar usuario
        try:
            cursor.execute(query, (username, email))  # Ejecutamos la consulta
            connection.commit()
            if cursor.rowcount > 0:  # Verificamos si se eliminó algún registro
                print("Usuario eliminado.")
            else:
                print("Usuario no encontrado.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            connection.close()

    def buscar_usuario(self, username=None, email=None):
        # Buscams un usuario en la base de datos basado en username o email
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM Usuario WHERE username = %s OR email = %s"  # hacmos lac onsulta de búsqueda
        cursor.execute(query, (username, email))
        usuario = cursor.fetchone()  # s obtiene el primer registro que coincide

        if usuario:
            print(f"Usuario encontrado: {usuario}")
        else:
            print("Usuario no encontrado.")

        cursor.close()
        connection.close()

    def mostrar_usuarios(self):
        # mostramos todos los usuarios registrados en la base de datos
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Usuario")  # Consultamos para obtener todos los usuarios
        usuarios = cursor.fetchall()

        if usuarios:  # Si hay usuarios, se los muestra
            for usuario in usuarios:
                print(usuario)
        else:
            print("No hay usuarios registrados.")

        cursor.close()
        connection.close()

    def ingresar_sistema(self, username, password):
        # Permitimos a un usuario ingresar al sistema si las credenciales son correctas
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM Usuario WHERE username = %s AND password = %s", (username, password))
        usuario = cursor.fetchone()  # Obtenmos el usuario que coincide con las credenciales

        if usuario:  # Si se encontró el usuario, entoncs se registra el acceso
            print(f"{username} ingresó exitosamente.")
            self.registrar_acceso(usuario['id'])
            return True
        else:
            print("Claves incorrectas.")  # Mensaje de error si las credenciales son incorrectas
            self.registrar_intento_fallido(username, password)
            return False

    def registrar_acceso(self, usuario_id):
        # Registramos el acceso de un usuario en la tabla Acceso
        connection = get_db_connection()
        cursor = connection.cursor()

        try:
            cursor.execute("INSERT INTO Acceso (fechaIngreso, fechaSalida, usuarioLogueado) VALUES (%s, NULL, %s)", 
                        (datetime.now(), usuario_id))  # Insertamos  el registro de acceso
            connection.commit()
            print("Acceso registrado.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            connection.close()

    def registrar_intento_fallido(self, username, password):
        # Registrams el intento fallido de ingreso en un archivo de logs
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"Intento fallido - Usuario: {username}, Password: {password}, Fecha: {datetime.now()}\n")  # Escribe en el archivo



