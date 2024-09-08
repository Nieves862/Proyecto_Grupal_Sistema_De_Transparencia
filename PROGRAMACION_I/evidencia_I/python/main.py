#inicio importando las funciones
from inicio_sesion import iniciar_sesion  
from gestionar_estudiantes import gestionar_estudiantes
from gestionar_materias import gestionar_materias
from gestionar_calificaciones import gestionar_calificaciones
from gestionar_asistencia import gestionar_asistencia
from realizar_consultas import realizar_consultas
import sys

def mostrar_menu(): #mostramos el menu
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

def obtener_opcion():
    while True:
        try:
            opcion = int(input())
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Opción inválida. Ingrese un número entre 1 y 6:")
        except ValueError:
            print("Por favor, ingrese una opción válida (número entero).")

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
        raise SystemExit(0)  # Manejar la excepción SystemExit para salir limpiamente

def main():
    if iniciar_sesion():  # Llama al inicio de sesión antes de mostrar el menú
        while True:
            mostrar_menu()
            opcion = obtener_opcion()
            ejecutar_opcion(opcion)

if __name__ == "__main__":
    try:
        main()
    except SystemExit as e:
        if e.code != 0:
            raise  # permite que cualquier exepcion que no sea una salida correcta se la pueda tratar mostrando un mensaje y no genere un error que bloquee todo
