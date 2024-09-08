from database import get_db_connection

def registrar_asistencia():
    conexion = get_db_connection()
    cursor = conexion.cursor()

    id_estudiante = input("Ingrese el ID del estudiante: ")
    id_materia = input("Ingrese el ID de la materia: ")
    fecha_clase = input("Ingrese la fecha de la clase (YYYY-MM-DD): ")
    asistencia = input("Ingrese la asistencia (Presente/Ausente): ")
    justificacion = input("Ingrese la justificación (si la hay): ")

    consulta = """
        INSERT INTO Asistencia (ID_ESTUDIANTE, ID_MATERIA, Fecha_Clase, Asistencia, Justificacion)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(consulta, (id_estudiante, id_materia, fecha_clase, asistencia, justificacion))
    conexion.commit()

    print("Asistencia registrada exitosamente!")
    cursor.close()
    conexion.close()

def consultar_asistencia():
    conexion = get_db_connection()
    cursor = conexion.cursor()

    id_asistencia = input("Ingrese el ID de la asistencia a consultar: ")
    consulta = "SELECT * FROM Asistencia WHERE ID_ASISTENCIA = %s"
    cursor.execute(consulta, (id_asistencia,))
    asistencia = cursor.fetchone()

    if asistencia:
        print(f"ID: {asistencia[0]}, ID Estudiante: {asistencia[1]}, ID Materia: {asistencia[2]}, Fecha Clase: {asistencia[3]}, Asistencia: {asistencia[4]}, Justificación: {asistencia[5]}")
    else:
        print(f"No se encontró asistencia con el ID: {id_asistencia}")

    cursor.close()
    conexion.close()

def actualizar_asistencia():
    conexion = get_db_connection()
    cursor = conexion.cursor()

    id_asistencia = input("Ingrese el ID de la asistencia a actualizar: ")
    id_estudiante = input("Ingrese el nuevo ID del estudiante: ")
    id_materia = input("Ingrese el nuevo ID de la materia: ")
    fecha_clase = input("Ingrese la nueva fecha de la clase (YYYY-MM-DD): ")
    asistencia = input("Ingrese la nueva asistencia (Presente/Ausente): ")
    justificacion = input("Ingrese la nueva justificación (si la hay): ")

    consulta = """
        UPDATE Asistencia
        SET ID_ESTUDIANTE = %s, ID_MATERIA = %s, Fecha_Clase = %s, Asistencia = %s, Justificacion = %s
        WHERE ID_ASISTENCIA = %s
    """
    cursor.execute(consulta, (id_estudiante, id_materia, fecha_clase, asistencia, justificacion, id_asistencia))
    conexion.commit()

    print("Asistencia actualizada exitosamente!")
    cursor.close()
    conexion.close()

def eliminar_asistencia():
    conexion = get_db_connection()
    cursor = conexion.cursor()

    id_asistencia = input("Ingrese el ID de la asistencia a eliminar: ")
    consulta = "DELETE FROM Asistencia WHERE ID_ASISTENCIA = %s"
    cursor.execute(consulta, (id_asistencia,))
    conexion.commit()

    print("Asistencia eliminada exitosamente!")
    cursor.close()
    conexion.close()

def gestionar_asistencia():
    while True:
        print("\nGestión de Asistencia")
        print("========================")
        print("1. Registrar asistencia")
        print("2. Consultar asistencia")
        print("3. Modificar asistencia")
        print("4. Eliminar asistencia")
        print("5. Volver al menú principal")
        print("========================")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            registrar_asistencia()
        elif opcion == "2":
            consultar_asistencia()
        elif opcion == "3":
            actualizar_asistencia()
        elif opcion == "4":
            eliminar_asistencia()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")
