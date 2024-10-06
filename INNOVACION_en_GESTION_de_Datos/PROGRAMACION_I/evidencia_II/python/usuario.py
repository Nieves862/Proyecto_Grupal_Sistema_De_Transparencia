import pickle  # nos permite guardar y cargar datos de forma sencilla
import os      # se carga para operaciones del sistema, como verificar la existencia de archivos
from datetime import datetime  # lo usamos ara manejar fechas y horas

# Definimos la clase Usuario, que representa a un usuario del sistema
class Usuario:
    # Inicializamos los atributos del usuario
    def __init__(self, id, username, password, email):
        self.id = id  # Identificador único para el usuario
        self.username = username  # Nombre de usuario
        self.password = password  # Contraseña del usuario
        self.email = email  # Correo electrónico del usuario
        self.accesos = []  # Lista para almacenar los accesos del usuario

    # Método que define cómo se representará el objeto Usuario como cadena
    def __str__(self):
        return f"Usuario(id: {self.id}, username: {self.username}, email: {self.email})"

    # Método que convierte el objeto Usuario en un diccionario
    def to_dict(self):
        return {
            'id': self.id,  # Incluimos el id
            'username': self.username,  # Incluimos el username
            'password': self.password,  # Incluimos el password
            'email': self.email  # Incluimos el email
        }

# Definimos la clase Acceso, que representa un registro de acceso de un usuario
class Acceso:
    # Inicializamos los atributos del acceso
    def __init__(self, id, fecha_ingreso, fecha_salida, usuario_logueado):
        self.id = id  # Identificador único para el acceso
        self.fecha_ingreso = fecha_ingreso  # Fecha y hora de ingreso
        self.fecha_salida = fecha_salida  # Fecha y hora de salida (puede ser None si el usuario aún no ha salido)
        self.usuario_logueado = usuario_logueado  # Referencia al usuario que ha iniciado sesión

    # Método que define cómo se representará el objeto Acceso como cadena
    def __str__(self):
        return f"Acceso(id: {self.id}, usuario: {self.usuario_logueado.username}, ingreso: {self.fecha_ingreso}, salida: {self.fecha_salida})"

    # Método que convierte el objeto Acceso en un diccionario
    def to_dict(self):
        return {
            'id': self.id,  # Incluimos el id del acceso
            'fecha_ingreso': self.fecha_ingreso,  # Incluimos la fecha de ingreso
            'fecha_salida': self.fecha_salida,  # Incluimos la fecha de salida
            'usuario_logueado': self.usuario_logueado.to_dict()  # Convertimos el usuario a diccionario
        }
