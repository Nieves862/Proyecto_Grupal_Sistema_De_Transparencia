def verificar_credenciales(nombre_usuario, clave, usuarios):
    intentos_fallidos = 0

    while intentos_fallidos < 4:
        if nombre_usuario in usuarios and usuarios[nombre_usuario] == clave:
            print("Ingreso exitoso.")
            guardar_ingreso(nombre_usuario)
            return True
        else:
            intentos_fallidos += 1
            print(f"Contraseña incorrecta. Intento {intentos_fallidos} de 4.")
            with open("log.txt", "a") as file:
                file.write(f"Intento fallido para {nombre_usuario} a las {datetime.now()}\n")
            if intentos_fallidos == 4:
                print(f"Usuario {nombre_usuario} bloqueado.")
                return False

    return False
