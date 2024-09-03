from gestionar_estudiantes import gestionar_estudiantes  # Importamos la función para gestionar estudiantes
from gestionar_materias import gestionar_materias        # Importams la función para gestionar materias
from gestionar_calificaciones import gestionar_calificaciones  # Importamos la función para gestionar calificaciones
from gestionar_asistencia import gestionar_asistencia    # Importams la función para gestionar asistencia
from realizar_consultas import realizar_consultas        # Importmos la función para realizar consultas
import sys  # Importamos el módulo sys para manejar la salida del sistema, para termnar el programa de manera controlada


#creamos la función mostrar menu principal
def mostrar_menu():
    
    print("Bienvenido al software de gestión de estudiantes")
    print("")
    print("1. Gestionar estudiantes")
    print("2. Gestionar materias")
    print("3. Gestionar calificaciones")
    print("4. Gestionar asistencia")
    print("5. Realizar consultas")
    print("6. Salir")
    print("")
    print("Por favor, elija la opción deseada:")

#creamos la función para obtener selecciconar una opción
def obtener_opcion():
    
    while True: # Declaro True, mientras exista ejecutamos lo siguiente, hasta encontrar un break o return
        try: # podemos tener una excepcion entonces la trataremos con un except
            opcion = int(input())  # Intentamos convertir la entrada del usuario a un número entero, sino tendremos una excepcion
            if 1 <= opcion <= 6:   # Verificamos que la opción esté dentro del rango válido
                return opcion      # Devolvemos la opción si es válida
            else: #de lo contrario ejecutamos el mensaje
                print("Opción inválida. Ingrese un número entre 1 y 6:")  # Mensaje de error si el número no está en el rango
        except ValueError:
            print("Por favor, ingrese una opción válida (número entero).")  # Mensaje de error si la entrada no es un número

#creamos la función para ejecutar la opción elegida
def ejecutar_opcion(opcion):
   
    if opcion == 1:
        gestionar_estudiantes()
    elif opcion == 2:
        gestionar_materias()
    elif opcion == 3:
        gestionar_calificaciones()
    elif opcion == 4:
        gestionar_asistencia()
    elif opcion == 5:
        realizar_consultas()
    elif opcion == 6:
        print("Saliendo del programa")
        raise SystemExit(0)  # Maneja la excepción SystemExit para salir correctamente, de otro modo me generaba un error

#creamos la función principal para ejecutar directamente el menu
def main():
    
    while True: #Mientras tenga True, ejecutamos mostrar el menu, pedir una opcion y ejecutarla luego 
        mostrar_menu()            # Muestra el menú al usuario
        opcion = obtener_opcion() # Obtiene la opción seleccionada por el usuario
        ejecutar_opcion(opcion)   # Ejecuta la opción seleccionada

if __name__ == "__main__": #l codigo se ejecuta solo si el archivo es el principal main y le asigno el nombre
    # Punto de entrada del programa
    try: #aplico try para manejar excepcones
        main()  # Ejecuta la función principal
    except SystemExit as e: #se ejecuta la excepcion si no es cero el codigo de la salida
        if e.code != 0:
            raise  # Re-lanza cualquier excepción que no sea una salida con codigo cero, para tener un mensaje de error aropiado en ultima instancia
