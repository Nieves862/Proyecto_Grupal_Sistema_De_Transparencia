from database import get_db_connection

def crear_materia():
    conexion = get_db_connection()
    cursor = conexion.cursor()

    espacio = input("Ingrese el nombre del espacio: ")
    profesor = input("Ingrese el nombre del profesor: ")
    detalle = input("Ingrese los detalles de la materia: ")
    carga_horaria = int(input("Ingrese la carga horaria de la materia: "))

    consulta = """
        INSERT INTO Materia (Espacio, Profesor, Detalle, Carga_Horaria)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(consulta, (espacio, profesor, detalle, carga_horaria))
    conexion.commit()

    print("Materia creada exitosamente!")
    cursor.close()
    conexion.close()

def consultar_materia():
    conexion = get_db_connection()
    cursor = conexion.cursor()

    id_materia = input("Ingrese el ID de la materia a consultar: ")
    consulta = "SELECT * FROM Materia WHERE ID_MATERIA = %s"
    cursor.execute(consulta, (id_materia,))
    materia = cursor.fetchone()

    if materia:
        print(f"ID: {materia[0]}, Espacio: {materia[1]}, Profesor: {materia[2]}, Detalle: {materia[3]}, Carga Horaria: {materia[4]}")
    else:
        print(f"No se encontró materia con el ID: {id_materia}")

    cursor.close()
    conexion.close()

def actualizar_materia():
    conexion = get_db_connection()
    cursor = conexion.cursor()

    id_materia = input("Ingrese el ID de la materia a actualizar: ")
    espacio = input("Ingrese el nuevo nombre del espacio: ")
    profesor = input("Ingrese el nuevo nombre del profesor: ")
    detalle = input("Ingrese los nuevos detalles de la materia: ")
    carga_horaria = int(input("Ingrese la nueva carga horaria de la materia: "))

    consulta = """
        UPDATE Materia
        SET Espacio = %s, Profesor = %s, Detalle = %s, Carga_Horaria = %s
        WHERE ID_MATERIA = %s
    """
    cursor.execute(consulta, (espacio, profesor, detalle, carga_horaria, id_materia))
    conexion.commit()

    print("Materia actualizada exitosamente!")
    cursor.close()
    conexion.close()

def eliminar_materia():
    conexion = get_db_connection()
    cursor = conexion.cursor()

    id_materia = input("Ingrese el ID de la materia a eliminar: ")
    consulta = "DELETE FROM Materia WHERE ID_MATERIA = %s"
    cursor.execute(consulta, (id_materia,))
    conexion.commit()

    print("Materia eliminada exitosamente!")
    cursor.close()
    conexion.close()

def gestionar_materias():
    while True:
        print("\nGestión de Materias")
        print("========================")
        print("1. Registrar materia")
        print("2. Consultar materia")
        print("3. Modificar materia")
        print("4. Eliminar materia")
        print("5. Volver al menú principal")
        print("========================")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            crear_materia()
        elif opcion == "2":
            consultar_materia()
        elif opcion == "3":
            actualizar_materia()
        elif opcion == "4":
            eliminar_materia()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")
