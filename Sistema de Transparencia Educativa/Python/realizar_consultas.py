import mysql.connector  # Importa el conector de MySQL
from database import get_db_connection  # Importa la función para obtener la conexión a la base de datos

def consultar_estudiantes():
    conexion = get_db_connection()
    cursor = conexion.cursor()

    # Consulta 1: Una sola tabla mostrando todos los datos
    consulta = "SELECT * FROM cuarto_año"
    cursor.execute(consulta)
    estudiantes = cursor.fetchall()

    if estudiantes:
        print("\nListado de estudiantes:")
        for estudiante in estudiantes:
            print(f"- ID: {estudiante[0]}, Nombre: {estudiante[1]} {estudiante[2]}, DNI: {estudiante[3]}")
    else:
        print("No hay estudiantes registrados.")

    cursor.close()
    conexion.close()

def consultar_materias():
    conexion = get_db_connection()
    cursor = conexion.cursor()

    # Consulta 1: Una sola tabla mostrando todos los datos
    consulta = "SELECT * FROM Materia"
    cursor.execute(consulta)
    materias = cursor.fetchall()

    if materias:
        print("\nListado de materias:")
        for materia in materias:
            print(f"- ID: {materia[0]}, Espacio: {materia[1]}, Profesor: {materia[2]}")
    else:
        print("No hay materias registradas.")

    cursor.close()
    conexion.close()

def consultar_estudiantes_por_nombre():
    nombre = input("Ingrese el nombre del estudiante a buscar: ")
    
    conexion = get_db_connection()
    cursor = conexion.cursor()

    # Consulta 2: Una sola tabla con WHERE
    consulta = "SELECT * FROM cuarto_año WHERE Nombre = %s"
    cursor.execute(consulta, (nombre,))
    estudiantes = cursor.fetchall()

    if estudiantes:
        print(f"\nEstudiantes encontrados con el nombre {nombre}:")
        for estudiante in estudiantes:
            print(f"- ID: {estudiante[0]}, Nombre: {estudiante[1]} {estudiante[2]}, DNI: {estudiante[3]}")

            # Consulta adicional para obtener las notas del estudiante
            consulta_notas = """
            SELECT Materia.Espacio, Nota_Formativa.Nota
            FROM Nota_Formativa
            INNER JOIN Materia ON Nota_Formativa.ID_MATERIA = Materia.ID_MATERIA
            WHERE Nota_Formativa.ID_ESTUDIANTE = %s
            """
            cursor.execute(consulta_notas, (estudiante[0],))
            notas = cursor.fetchall()

            if notas:
                print("  Notas:")
                for nota in notas:
                    print(f"  - Materia: {nota[0]}, Nota: {nota[1]}")
            else:
                print("  No se encontraron notas para este estudiante.")
    else:
        print(f"No se encontraron estudiantes con el nombre {nombre}.")

    cursor.close()
    conexion.close()

def consultar_estudiante_y_notas():
    id_estudiante = input("Ingrese el ID del estudiante: ")

    conexion = get_db_connection()
    cursor = conexion.cursor()

    # Consulta 3: Más de 1 tabla con INNER JOIN
    consulta = """
    SELECT cuarto_año.Nombre, cuarto_año.Apellido, Materia.Espacio, Nota_Formativa.Nota
    FROM cuarto_año
    INNER JOIN Nota_Formativa ON cuarto_año.ID_ESTUDIANTE = Nota_Formativa.ID_ESTUDIANTE
    INNER JOIN Materia ON Nota_Formativa.ID_MATERIA = Materia.ID_MATERIA
    WHERE cuarto_año.ID_ESTUDIANTE = %s
    """
    cursor.execute(consulta, (id_estudiante,))
    resultados = cursor.fetchall()

    if resultados:
        print(f"\nNotas del estudiante con ID {id_estudiante}:")
        for resultado in resultados:
            print(f"- Nombre: {resultado[0]} {resultado[1]}, Materia: {resultado[2]}, Nota: {resultado[3]}")
    else:
        print(f"No se encontraron notas para el estudiante con ID {id_estudiante}.")

    cursor.close()
    conexion.close()

def consultar_notas_por_materia():
    id_materia = input("Ingrese el ID de la materia: ")

    conexion = get_db_connection()
    cursor = conexion.cursor()

    # Consulta 4: Más de 1 tabla con INNER JOIN y con filtros
    consulta = """
    SELECT cuarto_año.Nombre, cuarto_año.Apellido, Materia.Espacio, Nota_Formativa.Nota
    FROM cuarto_año
    INNER JOIN Nota_Formativa ON cuarto_año.ID_ESTUDIANTE = Nota_Formativa.ID_ESTUDIANTE
    INNER JOIN Materia ON Nota_Formativa.ID_MATERIA = Materia.ID_MATERIA
    WHERE Materia.ID_MATERIA = %s
    """
    cursor.execute(consulta, (id_materia,))
    resultados = cursor.fetchall()

    if resultados:
        print(f"\nNotas de la materia con ID {id_materia}:")
        for resultado in resultados:
            print(f"- Nombre: {resultado[0]} {resultado[1]}, Materia: {resultado[2]}, Nota: {resultado[3]}")
    else:
        print(f"No se encontraron notas para la materia con ID {id_materia}.")

    cursor.close()
    conexion.close()

def realizar_consultas():
    while True:
        print("\nRealización de Consultas")
        print("========================")
        print("1. Consultar estudiantes")
        print("2. Consultar materias")
        print("3. Consultar estudiante y notas")
        print("4. Consultar estudiantes por nombre")
        print("5. Consultar notas por materia")
        print("6. Volver al menú principal")
        print("========================")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            consultar_estudiantes()
        elif opcion == "2":
            consultar_materias()
        elif opcion == "3":
            consultar_estudiante_y_notas()
        elif opcion == "4":
            consultar_estudiantes_por_nombre()
        elif opcion == "5":
            consultar_notas_por_materia()
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

