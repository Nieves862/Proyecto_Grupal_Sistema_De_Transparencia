
from manejoc import Sistema  # Importamos la clase Sistema desde el módulo manejoc

def mostrar_menu():
    # Esta función muestra el menú principal al usuario
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar un nuevo usuario")
    print("2. Modificar un usuario")
    print("3. Eliminar un usuario")
    print("4. Buscar un usuario (por username o email)")
    print("5. Mostrar todos los usuarios")
    print("6. Ingresar al sistema")
    print("7. Salir de la aplicación")

def main():
    # Se crea una instancia de la clase Sistema que permite interactuar con la base de datos
    sistema = Sistema()

    # Ciclo principal del programa que permite la interacción continua con el menú
    while True:
        mostrar_menu()  # Muestra el menú principal
        opcion = input("Seleccione una opción: ")  # El usuario selecciona una opción

        if opcion == '1':
            # Agregar un nuevo usuario
            username = input("Ingrese username: ")
            password = input("Ingrese password: ")
            email = input("Ingrese email: ")
            sistema.agregar_usuario(username, password, email)  # Llama al método creado para agregar usuario

        elif opcion == '2':
            # Modificar un usuario existente
            username = input("Ingrese el username del usuario a modificar: ")
            # Si el campo se deja vacío, se asigna None para que no se modifique
            nuevo_username = input("Nuevo username (dejar en blanco si no quiere cambiar): ")
            nuevo_password = input("Nuevo password (dejar en blanco si no quiere cambiar): ")
            nuevo_email = input("Nuevo email (dejar en blanco si no quiere cambiar): ")
            # Llama al método de modificar usuario con los datos ingresados
            sistema.modificar_usuario(username, nuevo_username or None, nuevo_password or None, nuevo_email or None)

        elif opcion == '3':
            # Eliminar un usuario por username o email
            criterio = input("¿Eliminar por username o email? (u/e): ").lower()
            if criterio == 'u':
                username = input("Ingrese el username: ")
                sistema.eliminar_usuario(username=username)  # Llama al método eliminación_usuario para eliminar segun username
            elif criterio == 'e':
                email = input("Ingrese el email: ")
                sistema.eliminar_usuario(email=email)  # Llama al método de eliminación por email
            else:
                print("Opción inválida")  # Muestro si hay error si el usuario ingresa una opción no válida

        elif opcion == '4':
            # Buscar un usuario por username o email
            criterio = input("¿Buscar por username o email? (u/e): ").lower()
            if criterio == 'u':
                username = input("Ingrese el username: ")
                sistema.buscar_usuario(username=username)  # Llama al método de búsqueda por username cuando elegimos la letra u
            elif criterio == 'e':
                email = input("Ingrese el email: ")
                sistema.buscar_usuario(email=email)  # Llama al método de búsqueda por email si colocamos antes la letra e
            else:
                print("Opción inválida")  # Manejamos un error que se generaria cuando la opcion de entrada no es válida

        elif opcion == '5':
            # Mostramos todos los usuarios registrados
            sistema.mostrar_usuarios()  # Llama al método que muestra todos los usuarios

        elif opcion == '6':
            # Ingresar al sistema
            username = input("Ingrese username: ")
            password = input("Ingrese password: ")
            if sistema.ingresar_sistema(username, password):  # Llama al método para iniciar sesión
                # Menú de sesión una vez que el usuario ha ingresado correctamente
                while True:
                    print("\n--- MENÚ DE SESIÓN ---")
                    print("1. Volver al menú principal")
                    print("2. Salir de la aplicación")
                    sub_opcion = input("Seleccione una opción: ")

                    if sub_opcion == '1':
                        break  # Vuelve al menú principal
                    elif sub_opcion == '2':
                        print("Saliendo de la aplicación...")
                        exit()  # Sale completamente de la aplicación
                    else:
                        print("Opción inválida")  # Manejo de error en caso de entrada inválida en el menú de sesión

        elif opcion == '7':
            # Opción para salir de la aplicación
            print("Saliendo de la aplicación...")
            break  # Rompe el ciclo principal y termina el programa

        else:
            # Manejo de opción inválida en el menú principal
            print("Opción inválida, intente nuevamente.")

# El bloque principal que ejecuta el programa si este es el archivo principal
if __name__ == "__main__":
    main()

