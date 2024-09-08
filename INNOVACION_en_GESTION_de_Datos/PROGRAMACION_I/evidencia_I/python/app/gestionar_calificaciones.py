from database import get_db_connection

def crear_calificacion():
    conexion = get_db_connection()
    cursor = conexion.cursor()

    id_estudiante = input("Ingrese el ID del estudiante: ")
    id_materia = input("Ingrese el ID de la materia: ")
    nota = int(input("Ingrese la nota: "))
    fecha_examen = input("Ingrese la fecha del examen (YYYY-MM-DD): ")
    tipo_examen = input("Ingrese el tipo de examen (Recuperatorio/Final): ")

    consulta = """
        INSERT INTO Nota_Formativa (ID_ESTUDIANTE, ID_MATERIA, Nota, Fecha_Exámen, Tipo_Exámen)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(consulta, (id_estudiante, id_materia, nota, fecha_examen, tipo_examen))
    conexion.commit()

    print("Calificación creada exitosamente!")
    cursor.close()
    conexion.close()

def consultar_calificacion():
    conexion = get_db_connection()
    cursor = conexion.cursor()

    id_calificacion = input("Ingrese el ID de la calificación a consultar: ")
    consulta = "SELECT * FROM Nota_Formativa WHERE ID_NOTA_Formativa = %s"
    cursor.execute(consulta, (id_calificacion,))
    calificacion = cursor.fetchone()

    if calificacion:
        print(f"ID: {calificacion[0]}, ID Estudiante: {calificacion[1]}, ID Materia: {calificacion[2]}, Nota: {calificacion[3]}, Fecha Examen: {calificacion[4]}, Tipo Examen: {calificacion[5]}")
    else:
        print(f"No se encontró calificación con el ID: {id_calificacion}")

    cursor.close()
    conexion.close()

def actualizar_calificacion():
    conexion = get_db_connection()
    cursor = conexion.cursor()

    id_calificacion = input("Ingrese el ID de la calificación a actualizar: ")
    id_estudiante = input("Ingrese el nuevo ID del estudiante: ")
    id_materia = input("Ingrese el nuevo ID de la materia: ")
    nota = int(input("Ingrese la nueva nota: "))
    fecha_examen = input("Ingrese la nueva fecha del examen (YYYY-MM-DD): ")
    tipo_examen = input("Ingrese el nuevo tipo de examen (Recuperatorio/Final): ")

    consulta = """
        UPDATE Nota_Formativa
        SET ID_ESTUDIANTE = %s, ID_MATERIA = %s, Nota = %s, Fecha_Exámen = %s, Tipo_Exámen = %s
        WHERE ID_NOTA_Formativa = %s
    """
    cursor.execute(consulta, (id_estudiante, id_materia, nota, fecha_examen, tipo_examen, id_calificacion))
    conexion.commit()

    print("Calificación actualizada exitosamente!")
    cursor.close()
    conexion.close()

def eliminar_calificacion():
    conexion = get_db_connection()
    cursor = conexion.cursor()

    id_calificacion = input("Ingrese el ID de la calificación a eliminar: ")
    consulta = "DELETE FROM Nota_Formativa WHERE ID_NOTA_Formativa = %s"
    cursor.execute(consulta, (id_calificacion,))
    conexion.commit()

    print("Calificación eliminada exitosamente!")
    cursor.close()
    conexion.close()

def gestionar_calificaciones():
    while True:
        print("\nGestión de Calificaciones")
        print("========================")
        print("1. Registrar calificación")
        print("2. Consultar calificación")
        print("3. Modificar calificación")
        print("4. Eliminar calificación")
        print("5. Volver al menú principal")
        print("========================")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            crear_calificacion()
        elif opcion == "2":
            consultar_calificacion()
        elif opcion == "3":
            actualizar_calificacion()
        elif opcion == "4":
            eliminar_calificacion()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")
