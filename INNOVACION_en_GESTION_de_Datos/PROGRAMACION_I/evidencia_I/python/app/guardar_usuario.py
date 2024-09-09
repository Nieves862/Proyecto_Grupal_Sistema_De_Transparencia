def guardar_usuario(nombre_usuario, clave):
    with open("usuariosCreados.txt", "a") as file:
        file.write(f"Usuario: {nombre_usuario}, Clave: {clave}\n")
        file.write("Usuario creado correctamente.\n")
    print("Usuario registrado y guardado correctamente.")
