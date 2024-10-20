
from sistema import Sistema

def menu_principal():
    sistema = Sistema()

    while True:
        print("\nMenú Principal")
        print("1. Agregar un nuevo usuario")
        print("2. Modificar un usuario")
        print("3. Eliminar un usuario")
        print("4. Buscar un usuario por username o email")
        print("5. Mostrar todos los usuarios")
        print("6. Ingresar al sistema")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            username = input("Username: ")
            password = input("Password: ")
            email = input("Email: ")
            sistema.agregar_usuario(username, password, email)

        elif opcion == "2":
            username_o_email = input("Ingresa el username o email del usuario a modificar: ")
            nuevo_username = input("Nuevo username (dejar en blanco si no quieres cambiarlo): ")
            nuevo_password = input("Nuevo password (dejar en blanco si no quieres cambiarlo): ")
            nuevo_email = input("Nuevo email (dejar en blanco si no quieres cambiarlo): ")
            sistema.modificar_usuario(username_o_email, nuevo_username, nuevo_password, nuevo_email)

        elif opcion == "3":
            username_o_email = input("Ingresa el username o email del usuario a eliminar: ")
            sistema.eliminar_usuario(username_o_email)

        elif opcion == "4":
            username_o_email = input("Ingresa el username o email del usuario a buscar: ")
            usuario = sistema.buscar_usuario(username_o_email)
            if usuario:
                print(usuario)
            else:
                print(f"Usuario {username_o_email} no encontrado.")

        elif opcion == "5":
            sistema.mostrar_todos_usuarios()

        elif opcion == "6":
            username = input("Username: ")
            password = input("Password: ")
            usuario = sistema.buscar_usuario(username)
            if usuario and usuario.password == password:
                print(f"Bienvenido {usuario.username}, has ingresado al sistema.")
                sistema.registrar_acceso(usuario)
                while True:
                    print("\n1. Volver al menú principal")
                    print("2. Salir del sistema")
                    opcion_salida = input("Elige una opción: ")
                    if opcion_salida == "1":
                        break
                    elif opcion_salida == "2":
                        exit()
                    else:
                        print("Opción no válida.")
            else:
                sistema.registrar_intento_fallido(username, password)

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    menu_principal()
