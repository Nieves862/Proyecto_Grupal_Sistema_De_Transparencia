import re # Se usa para trabajar con expresiones regulares, para valida y hacer coincidir contraseñas

# Diccionario temporal para almacenar los usuarios, los datos van a guardarse mientras el programa se esté ejecutando
usuarios = {}

# Se crea la función para valdar el nombre de usuario
def validar_nombre_usuario(nombre_usuario):
    return 6 <= len(nombre_usuario) <= 12 #comprobamos que tengan la medida pedida entre 6 y 12 caracteres

# Creamos la función para validar la contraseña
def validar_contraseña(contraseña):
    condiciones = 0
    if len(contraseña) >= 8: # contamos para ver que tenga menos de 8 caracteres
        if re.search("[a-z]", contraseña): # verificamos la condicion de que tenga al menos un minuscula
            condiciones += 1
        if re.search("[A-Z]", contraseña): # verificamos la condicion de que tenga al menos una mayuscula
            condiciones += 1
        if re.search("[0-9]", contraseña): # verificamos la condicion de que tenga al menos un nro
            condiciones += 1
        if re.search("[^a-zA-Z0-9]", contraseña):  # verificamos la condicion de que tenga al menos un caracter especial
            condiciones += 1
    return condiciones >= 2 # va a funcionar si cumple con al menos dos condiciones

# Se crea la función para registrar un nuevo usuario
def registrar_usuario():
    while True:
        dni = input("Ingrese el DNI: ") #pedimos el dni
        if dni in usuarios: #verifico si ya esta registrado y lo indico en un mensaje
            print("El DNI ya está registrado. Intente nuevamente.")
        else: #de lo contario salgo
            break

    while True: #mientras sea verdader solito un nombre de usuario
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        if any(u['nombre_usuario'] == nombre_usuario for u in usuarios.values()): #verificamos si el nombre ya exste
            print("El nombre de usuario ya está en uso. Intente con otro.")
        elif not validar_nombre_usuario(nombre_usuario): #sino existe seguimos verificando que cumple con la cantidad de caracteres solicitados
            print("El nombre de usuario debe tener entre 6 y 12 caracteres.")
        else:
            break

    while True: #mientras sea verdadero 
        contraseña = input("Ingrese la contraseña: ") #pedimos ingresar una clave
        if validar_contraseña(contraseña): #verificamos si la clave cumple con los rquisitos de la fucion validar_contraseña
            break
        else:
            print("La contraseña debe tener al menos 8 caracteres y cumplir con 2 de las siguientes condiciones:")
            print("- Al menos 1 minúscula")
            print("- Al menos 1 mayúscula")
            print("- Al menos 1 número")
            print("- Al menos 1 caracter especial")
    #pedimos los datos del usuario
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    email = input("Ingrese el correo electrónico: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento (AAAA-MM-DD): ")

    # ahora guardamos el usuario en el diccionario
    usuarios[dni] = {
        'nombre': nombre,
        'apellido': apellido,
        'email': email,
        'fecha_nacimiento': fecha_nacimiento,
        'nombre_usuario': nombre_usuario,
        'contraseña': contraseña
    }

    print("Usuario registrado con éxito.")

# creamos la función para inicio de sesión con un menu
def iniciar_sesion():
    print("Bienvenido al sistema de gestión de estudiantes")
    while True:
        print("1. Iniciar sesión")
        print("2. Registrar nuevo usuario")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1": #solicitamos usuario y clave
            nombre_usuario = input("Ingrese su nombre de usuario: ")
            contraseña = input("Ingrese su contraseña: ")
            
            usuario_encontrado = None
            for usuario in usuarios.values(): #buscamos el usuario en el diccionario usuarios
                if usuario['nombre_usuario'] == nombre_usuario and usuario['contraseña'] == contraseña:
                    usuario_encontrado = usuario
                    break

            if usuario_encontrado: #si lo encontramos mostramos el mensaje de bienvenida a ese usuaior
                print(f"Bienvenido {usuario_encontrado['nombre']} {usuario_encontrado['apellido']}!")
                return True
            else:
                print("Usuario o contraseña incorrectos. Intente nuevamente.")
        
        elif opcion == "2": # llamamos a la funcion para crear un nuevo usuario
            registrar_usuario()
        
        elif opcion == "3": #salimos del programa
            print("Saliendo del sistema...")
            return False
        
        else:
            print("Opción inválida. Intente nuevamente.")



