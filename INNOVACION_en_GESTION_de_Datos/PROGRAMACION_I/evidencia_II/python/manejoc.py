from datetime import datetime #impotamos para registrar la hora cdo se ingresa al sistema o se intenta ingresar de forma fallida
from database import get_db_connection  # Importamos la función para conectarnos a la base de datos

class Sistema:
    def __init__(self):
        # En el constructor, cargamos los usuarios desde la base de datos
        self.usuarios = self.cargar_usuarios()

    def cargar_usuarios(self):
        # Obtenemos una conexión a la base de datos
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        # Ejecutamos una consulta para obtener todos los usuarios
        cursor.execute("SELECT * FROM Usuario")
        # Recuperamos los datos de los usuarios y cerramos la conexión
        usuarios = cursor.fetchall()  
        cursor.close()
        connection.close()
        # Devolvemos la lista de usuarios obtenidos
        return usuarios

    def agregar_usuario(self, username, password, email):
        # Nos conectamos a la base de datos
        connection = get_db_connection()
        cursor = connection.cursor()

        try:
            # Insertamos un nuevo usuario en la tabla Usuario
            cursor.execute("INSERT INTO Usuario (username, password, email) VALUES (%s, %s, %s)", 
                           (username, password, email))
            connection.commit()  # Confirmamos la carga
            print("Usuario agregado exitosamente.")
        except mysql.connector.Error as err:
            # Capturamos cualquier error que ocurra cuando se ejecuta
            print(f"Error: {err}")
        finally:
            # Cerramos el cursor y la conexión
            cursor.close()
            connection.close()

    def modificar_usuario(self, username, nuevo_username=None, nuevo_password=None, nuevo_email=None):
        # Nos conectamos a la base de datos
        connection = get_db_connection()
        cursor = connection.cursor()

        # Construimos la consulta SQL para actualizar los datos del usuario
        query = "UPDATE Usuario SET"
        values = []
        if nuevo_username:
            query += " username = %s,"  # Agregamos el campo username si es necesario
            values.append(nuevo_username)
        if nuevo_password:
            query += " password = %s,"  # Agregamos el campo password si es necesario
            values.append(nuevo_password)
        if nuevo_email:
            query += " email = %s"  # Agregamos el campo email si es necesario
            values.append(nuevo_email)
        
        # Limpiamos la coma sobrante si nos quedo colgada a final
        query = query.rstrip(',')
        query += " WHERE username = %s"
        values.append(username)

        try:
            # Ejecutamos la consulta y confirmamos los cambios
            cursor.execute(query, tuple(values))
            connection.commit()
            # Verificamos si se modificaron registros
            if cursor.rowcount > 0:
                print("Usuario modificado exitosamente.")
            else:
                print("Usuario no encontrado.")
        except mysql.connector.Error as err:
            # Capturamos cualquier error que ocurra durante el cambio que hagams
            print(f"Error: {err}")
        finally:
            # Cerramos el cursor y la conexión
            cursor.close()
            connection.close()

    def eliminar_usuario(self, username=None, email=None):
        # Nos conectamos a la base de datos
        connection = get_db_connection()
        cursor = connection.cursor()

        # Construimos la consulta para eliminar un usuario
        query = "DELETE FROM Usuario WHERE username = %s OR email = %s"
        try:
            # Ejecutamos la consulta
            cursor.execute(query, (username, email))
            connection.commit()
            # Verificamos si se eliminó algún registro
            if cursor.rowcount > 0:
                print("Usuario eliminado.")
            else:
                print("Usuario no encontrado.")
        except mysql.connector.Error as err:
            # Capturamos cualquier error durante la eliminación
            print(f"Error: {err}")
        finally:
            # Cerramos el cursor y la conexión
            cursor.close()
            connection.close()

    def buscar_usuario(self, username=None, email=None):
        # Nos conectamos a la base de datos
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        # Ejecutamos la consulta para buscar un usuario por nombre o email
        query = "SELECT * FROM Usuario WHERE username = %s OR email = %s"
        cursor.execute(query, (username, email))
        usuario = cursor.fetchone()  # Obtenemos el primer resultado

        if usuario:
            # Si el usuario es encontrado, lo mostramos
            print(f"Usuario encontrado: {usuario}")
        else:
            # Si no se encuentra el usuario, lo muestro tambin
            print("Usuario no encontrado.")

        # Cerramos el cursor y la conexión
        cursor.close()
        connection.close()

    def mostrar_usuarios(self):
        # Nos conectamos a la base de datos
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        # Ejecutamos una consulta para obtener todos los usuarios
        cursor.execute("SELECT * FROM Usuario")
        usuarios = cursor.fetchall()

        # Si hay usuarios, los mostramos
        if usuarios:
            for usuario in usuarios:
                print(usuario)
        else:
            # Si no hay usuarios registrados, lo indicamos
            print("No hay usuarios registrados.")

        # Cerramos el cursor y la conexión
        cursor.close()
        connection.close()

    def ingresar_sistema(self, username, password):
        # Nos conectamos a la base de datos
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        # Ejecutamos la consulta para verificar las credenciales del usuario
        cursor.execute("SELECT * FROM Usuario WHERE username = %s AND password = %s", (username, password))
        usuario = cursor.fetchone()

        if usuario:
            # Si las credenciales son correctas, registramos el acceso y devolvemos True
            print(f"{username} ingresó exitosamente.")
            self.registrar_acceso(usuario['id'])
            return True
        else:
            # Si las claves son incorrectas, registramos el intento fallido y devolvemos False
            print("Claves incorrectas.")
            self.registrar_intento_fallido(username, password)
            return False

    def registrar_acceso(self, usuario_id):
        # Nos conectamos a la base de datos
        connection = get_db_connection()
        cursor = connection.cursor()

        try:
            # Registramos el acceso del usuario en la tabla Acceso
            cursor.execute("INSERT INTO Acceso (fechaIngreso, fechaSalida, usuarioLogueado) VALUES (%s, NULL, %s)", 
                           (datetime.now(), usuario_id))
            connection.commit()  # Confirmamos los cambios
            print("Acceso registrado.")
        except mysql.connector.Error as err:
            # Capturamos cualquier error que ocurra al registrar el acceso
            print(f"Error: {err}")
        finally:
            # Cerramos el cursor y la conexión
            cursor.close()
            connection.close()

    def registrar_intento_fallido(self, username, password):
        # Registramos los intentos fallidos de inicio de sesión en un archivo de logs
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"Intento fallido - Usuario: {username}, Password: {password}, Fecha: {datetime.now()}\n")

