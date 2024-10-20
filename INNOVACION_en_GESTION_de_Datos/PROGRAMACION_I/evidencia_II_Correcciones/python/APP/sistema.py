import pickle
from datetime import datetime

class Usuario:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return f"ID: {self.id}, Username: {self.username}, Email: {self.email}"

class Acceso:
    def __init__(self, id, usuario_logueado):
        self.id = id
        self.fecha_ingreso = datetime.now()
        self.fecha_salida = None
        self.usuario_logueado = usuario_logueado

    def registrar_salida(self):
        self.fecha_salida = datetime.now()

    def __str__(self):
        return (f"ID Acceso: {self.id}, Usuario: {self.usuario_logueado.username}, "
                f"Fecha Ingreso: {self.fecha_ingreso}, Fecha Salida: {self.fecha_salida}")

class Sistema:
    def __init__(self):
        self.usuarios = self.cargar_datos("usuarios.ispc")
        self.ultimo_id = len(self.usuarios)
        self.accesos = self.cargar_datos("accesos.ispc")

    def cargar_datos(self, archivo):
        try:
            with open(archivo, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []

    def guardar_datos(self, archivo, datos):
        with open(archivo, 'wb') as file:
            pickle.dump(datos, file)

    def agregar_usuario(self, username, password, email):
        self.ultimo_id += 1
        nuevo_usuario = Usuario(self.ultimo_id, username, password, email)
        self.usuarios.append(nuevo_usuario)
        self.guardar_datos("usuarios.ispc", self.usuarios)
        print(f"Usuario {username} agregado correctamente.")

    def modificar_usuario(self, username_o_email, nuevo_username=None, nuevo_password=None, nuevo_email=None):
        usuario = self.buscar_usuario(username_o_email)
        if usuario:
            if nuevo_username:
                usuario.username = nuevo_username
            if nuevo_password:
                usuario.password = nuevo_password
            if nuevo_email:
                usuario.email = nuevo_email
            self.guardar_datos("usuarios.ispc", self.usuarios)
            print(f"Usuario {username_o_email} modificado correctamente.")
        else:
            print(f"Usuario {username_o_email} no encontrado.")

    def eliminar_usuario(self, username_o_email):
        usuario = self.buscar_usuario(username_o_email)
        if usuario:
            self.usuarios.remove(usuario)
            self.guardar_datos("usuarios.ispc", self.usuarios)
            print(f"Usuario {username_o_email} eliminado correctamente.")
        else:
            print(f"Usuario {username_o_email} no encontrado.")

    def buscar_usuario(self, username_o_email):
        for usuario in self.usuarios:
            if usuario.username == username_o_email or usuario.email == username_o_email:
                return usuario
        return None

    def mostrar_todos_usuarios(self):
        if self.usuarios:
            for usuario in self.usuarios:
                print(usuario)
        else:
            print("No hay usuarios registrados.")

    def registrar_acceso(self, usuario):
        nuevo_acceso = Acceso(len(self.accesos) + 1, usuario)
        self.accesos.append(nuevo_acceso)
        self.guardar_datos("accesos.ispc", self.accesos)
        print(f"Acceso registrado para el usuario {usuario.username}. Fecha de ingreso: {nuevo_acceso.fecha_ingreso}")

    def registrar_intento_fallido(self, username, password):
        with open("logs.txt", "a") as log_file:
            log_file.write(f"{datetime.now()} - Intento fallido: Usuario: {username}, Password: {password}\n")
        print("Datos incorrectos. Registro de intento fallido guardado.")

    def login(self, username, password):
        """Método para verificar si el usuario puede iniciar sesión"""
        for usuario in self.usuarios:
            if usuario.username == username and usuario.password == password:
                print(f"Bienvenido, {username}. Has ingresado al sistema.")
                # Registrar acceso exitoso
                return True
        # Si no encuentra un usuario válido, registrar el intento fallido
        print("Error: Username o password incorrecto.")
        self.registrar_intento_fallido(username, password)
        return False