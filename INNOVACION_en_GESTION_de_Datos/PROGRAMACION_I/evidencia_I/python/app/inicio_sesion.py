import re  #Importamos la biblioteca para trabajar con expresiones regulares lovamos a usar para validar contraseña
import random  # Se usa para generar números y operaciones aleatorias pensando en el captcha
import time  # Importamos la función time para trabajar con tiempos
from datetime import datetime  # lo usamos con fecha y horas  registrarmos los ingresos de usuarios
from aritmetica import sumar, restar, multiplicar, dividir  # Importamos lsa funciones de aritmética 

usuarios = {}  # es el diccionario para almacenar los usuarios registrados.
intentos_fallidos = {}  # con ete diccionatio contams los intentos fallidos de inicio de sesión por usuario.

# creamos la función para generar un captcha matemático simple
def generar_captcha():
    operaciones = ['+', '-', '*', '/']  # Listamos operaciones disponibles para usar.
    num1 = round(random.uniform(1, 100), 2)  # Generamos un número aleatorio con 2 decimales.
    num2 = round(random.uniform(1, 100), 2)  # crramos número aleatorio con 2 decimales.
    operacion = random.choice(operaciones)  # hacemos una operación aleatoria.

    # Según la operación que sale se realiza la operación aritmética correspondiente.
    if operacion == '+':
        resultado_correcto = round(sumar(num1, num2), 2)
    elif operacion == '-':
        resultado_correcto = round(restar(num1, num2), 2)
    elif operacion == '*':
        resultado_correcto = round(multiplicar(num1, num2), 2)
    elif operacion == '/':
        if num2 != 0:  # Evitamos asi división por cero.
            resultado_correcto = round(dividir(num1, num2), 2)
        else:
            return generar_captcha()  # regresamos a generar otro captcha Si num2 es 0

    print(f"Captcha: {num1} {operacion} {num2} = ?")  # Mostramos con un print el captcha al usuario.
    return resultado_correcto  # Devolvemos el resultado correcto del captcha.

# creamos una funcin para validar el captcha generado
def validar_captcha():
    while True:
        resultado_correcto = generar_captcha()  # Genera aca el captcha.
        try:
            respuesta_usuario = float(input("Ingrese el resultado con dos decimales: "))  # pedimos el rdo.
            if round(respuesta_usuario, 2) == resultado_correcto:  # Comparamos la respuesta con el resultado correcto.
                print("Captcha correcto.")
                return True  # Si es correcto, devuelve True.
            else:
                print("Captcha incorrecto. Intente nuevamente.")
        except ValueError:  # Manejamos el error si el usuario ingresa un valor no numérico.
            print("Respuesta inválida. Intente nuevamente.")

        # consukto si el usuario quiere volver a intentar el captcha.
        opcion = input("¿Desea intentar de nuevo? (S/N): ").lower()
        if opcion != 's':
            return False  # Si no quiere volver a intentar, retorna False.

# creamos la función para validar el nombre de usuario
def validar_nombre_usuario(nombre_usuario):
    return 6 <= len(nombre_usuario) <= 12  # aclaramos que el nombre de usuario debe tener entre 6 y 12 caracteres.

# creaos la función para validar la contraseña
def validar_contraseña(contraseña):
    condiciones = 0
    # indico que la contraseña debe tener al menos 8 caracteres.
    if len(contraseña) >= 8:
        # Verificamos si contiene al menos una letra minúscula.
        if re.search("[a-z]", contraseña):
            condiciones += 1
        # Verificamos si contiene al menos una letra mayúscula.
        if re.search("[A-Z]", contraseña):
            condiciones += 1
        # Verificamos si contiene al menos un número.
        if re.search("[0-9]", contraseña):
            condiciones += 1
        # Verificams si contiene al menos un caracter especial.
        if re.search("[^a-zA-Z0-9]", contraseña):
            condiciones += 1
    # indico que la contraseña debe cumplir con al menos 2 de las 4 condiciones.
    return condiciones >= 2

#creamos la función para registrar un nuevo usuario
def registrar_usuario():
    while True:
        dni = input("Ingrese el DNI: ")  # Solicitamos el DNI del usuario.
        if dni in usuarios:  # Verificamos si el DNI ya está registrado.
            print("El DNI ya está registrado. Intente nuevamente.")
        else:
            break  # Si no está registrado, continiams.

    while True:
        nombre_usuario = input("Ingrese el nombre de usuario: ")  # pedimos el nombre de usuario.
        # Verificamos si el nombre de usuario ya está en uso.
        if any(u['nombre_usuario'] == nombre_usuario for u in usuarios.values()):
            print("El nombre de usuario ya está en uso. Intente con otro.")
        # Verificamos si el nombre cumple con la longitud permitida.
        elif not validar_nombre_usuario(nombre_usuario):
            print("El nombre de usuario debe tener entre 6 y 12 caracteres.")
        else:
            break  # Si el nombre es válido entonces continúa.

    while True:
        contraseña = input("Ingrese la contraseña: ")  # Solicitamos la contraseña.
        if validar_contraseña(contraseña):  # Verificamos si la contraseña cumple con los requisitos.
            break
        else:
            print("La contraseña debe tener al menos 8 caracteres y cumplir con 2 de las siguientes condiciones:")
            print("- Al menos 1 minúscula")
            print("- Al menos 1 mayúscula")
            print("- Al menos 1 número")
            print("- Al menos 1 caracter especial")

    # se solicita otros datos personales del usuario.
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    email = input("Ingrese el correo electrónico: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento (AAAA-MM-DD): ")

    # se genera el captcha antes de completar el registro.
    if validar_captcha():
        # Si el captcha es correcto, guarda los datos del usuario en el diccionario usuarios.
        usuarios[dni] = {
            'nombre': nombre,
            'apellido': apellido,
            'email': email,
            'fecha_nacimiento': fecha_nacimiento,
            'nombre_usuario': nombre_usuario,
            'contraseña': contraseña
        }

        print("Usuario registrado con éxito.")
        
        # Guarda los datos del usuario en un archivo de texto.
        with open("usuariosCreados.txt", "a") as file:
            file.write(f"{nombre_usuario}, {nombre}, {apellido}, {email}, {fecha_nacimiento}\n")
        print("Datos guardados en usuariosCreados.txt.")
    else:
        print("No se pudo completar el registro debido a un fallo en el captcha.")

# Función para iniciar sesión con control de intentos fallidos
def iniciar_sesion():
    print("Bienvenido al sistema de gestión de estudiantes")
    while True:
        # Menú principal con opciones.
        print("1. Iniciar sesión")
        print("2. Registrar nuevo usuario")
        print("3. Olvidé mi contraseña")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Opción de iniciar sesión.
            nombre_usuario = input("Ingrese su nombre de usuario: ")
            contraseña = input("Ingrese su contraseña: ")
            
            usuario_encontrado = None
            # Busca el usuario en el diccionario.
            for usuario in usuarios.values():
                if usuario['nombre_usuario'] == nombre_usuario:
                    usuario_encontrado = usuario
                    break

            if usuario_encontrado:
                # Verifica si la contraseña es correcta.
                if usuario_encontrado['contraseña'] == contraseña:
                    print(f"Bienvenido {usuario_encontrado['nombre']} {usuario_encontrado['apellido']}!")
                    # Guarda el ingreso en el archivo ingresos.txt.
                    with open("ingresos.txt", "a") as file:
                        file.write(f"{nombre_usuario}, {datetime.now()}\n")
                    return True
                else:
                    # Registra intentos fallidos.
                    intentos_fallidos[nombre_usuario] = intentos_fallidos.get(nombre_usuario, 0) + 1
                    print(f"Contraseña incorrecta. Intento {intentos_fallidos[nombre_usuario]} de 4.")
                    
                    # Bloquea el usuario después de 4 intentos fallidos.
                    if intentos_fallidos[nombre_usuario] == 4:
                        print(f"El usuario {nombre_usuario} ha sido bloqueado.")
                        with open("log.txt", "a") as file:
                            file.write(f"Usuario bloqueado: {nombre_usuario}, {datetime.now()}\n")
                        return False
            else:
                print("Usuario no encontrado. Intente nuevamente.")
        
        elif opcion == "2":
            # Opción para registrar un nuevo usuario.
            registrar_usuario()

        elif opcion == "3":  # Opción "Olvidé mi contraseña" no implementada aún
            print("Función no implementada.")
            pass
        
        elif opcion == "4":
            # Salir del sistema.
            print("Saliendo del sistema...")
            return False
        
        else:
            print("Opción inválida. Intente nuevamente.")