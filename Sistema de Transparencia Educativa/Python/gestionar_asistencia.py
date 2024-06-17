from database import get_db_connection  # Importamos la función para obtener la conexión a la base de datos


#Creamos la funcion registrar asistencia
def registrar_asistencia():
    conexion = get_db_connection()  # Obtenemos la conexión a la base de datos
    cursor = conexion.cursor()  # Creamos un cursor para interactuar con la base de datos

    # Solicitamos los datos de la nueva asistencia al usuario
    id_estudiante = input("Ingrese el ID del estudiante: ")
    id_materia = input("Ingrese el ID de la materia: ")
    fecha_clase = input("Ingrese la fecha de la clase (YYYY-MM-DD): ")
    asistencia = input("Ingrese la asistencia (Presente/Ausente): ")
    justificacion = input("Ingrese la justificación (si la hay): ")

    #Consultamos SQL para insertar una nueva asistencia
    #Consultamos el SQL para insertar una nueva calificación
    #Definimos una consulta como una cadena de texto con ""
    #Luego realizamos una operacion de Insert en la tabla Asistencia y especifiamos las columnas a rellenar con los datos
    #Despus introducimos los marcadores de posicion con %s
    consulta = """
        INSERT INTO Asistencia (ID_ESTUDIANTE, ID_MATERIA, Fecha_Clase, Asistencia, Justificacion)
        VALUES (%s, %s, %s, %s, %s)
    """
    # Ejecutams la consulta con los datos proporcionados por el usuario
    cursor.execute(consulta, (id_estudiante, id_materia, fecha_clase, asistencia, justificacion))
    conexion.commit()  # Confirmamos los cambios en la base de datos

    print("Asistencia registrada exitosamente!")
    cursor.close()  # Cerramos la interaccion cerrando el cursor
    conexion.close()  # Cerramos la conexión a la base de datos


#creamos una funcion para consultar la asistencia
def consultar_asistencia():
    conexion = get_db_connection()  #Obtenemos la conexión a la base de datos
    cursor = conexion.cursor()  # Creamos un cursor para interactuar con la base de datos

    # Solicitamoss el ID para consultar por asistencia
    id_asistencia = input("Ingrese el ID de la asistencia a consultar: ")
    # Consulta SQL para obtener los datos de la asistencia
    consulta = "SELECT * FROM Asistencia WHERE ID_ASISTENCIA = %s" # Definimos en la consulta para obtener de la tabla Asistencia a partir del ID de la nota ingresada con el marcador %s
    cursor.execute(consulta, (id_asistencia,))  # Ejecutamos la consulta con el ID proporcionado
    asistencia = cursor.fetchone()  # Obtenemos el resultado de la consulta

    # Mostramos los datos de la materia si se encuentra por ID, con los campos de cada materia que coincidieron en el paso anterior
    if asistencia: #si hubo coincidencia
        print(f"ID: {asistencia[0]}, ID Estudiante: {asistencia[1]}, ID Materia: {asistencia[2]}, Fecha Clase: {asistencia[3]}, Asistencia: {asistencia[4]}, Justificación: {asistencia[5]}")
    else:# de lo contrario
        print(f"No se encontró asistencia con el ID: {id_asistencia}")

    cursor.close()  # Cerramos el cursor
    conexion.close()  # Cerramos la conexión a la base de datos


#creamos la funcion actualizar asistencia
def actualizar_asistencia():
    conexion = get_db_connection()  # Obtenemos la conexión a la base de datos
    cursor = conexion.cursor()  # Creamos un cursor para interactuar con la base de datos

    # Solicitamos los nuevos datos de la asistencia al usuario
    id_asistencia = input("Ingrese el ID de la asistencia a actualizar: ")
    id_estudiante = input("Ingrese el nuevo ID del estudiante: ")
    id_materia = input("Ingrese el nuevo ID de la materia: ")
    fecha_clase = input("Ingrese la nueva fecha de la clase (YYYY-MM-DD): ")
    asistencia = input("Ingrese la nueva asistencia (Presente/Ausente): ")
    justificacion = input("Ingrese la nueva justificación (si la hay): ")

    #Definimos una consulta como una cadena de texto con ""
    #Luego realizamos una operacion de Update para actualizar en la tabla Materia y especifiamos las columnas a rellenar con los datos
    #Despus introducimos los marcadores de posicion con %s
    consulta = """
        UPDATE Asistencia
        SET ID_ESTUDIANTE = %s, ID_MATERIA = %s, Fecha_Clase = %s, Asistencia = %s, Justificacion = %s
        WHERE ID_ASISTENCIA = %s
    """
    # Ejecutamos la consulta con los nuevos datos proporcionados
    cursor.execute(consulta, (id_estudiante, id_materia, fecha_clase, asistencia, justificacion, id_asistencia))
    conexion.commit()  # Confirmamos los cambios en la base de datos

    print("Asistencia actualizada exitosamente!")
    cursor.close()  # Cerramos el cursor
    conexion.close()  # Cerramos la conexión a la base de datos

#creamos una funcin para eliminar la asistencia
def eliminar_asistencia():
    conexion = get_db_connection()  # Obtenemos la conexión a la base de datos
    cursor = conexion.cursor()  # Creamos un cursor para interactuar con la base de datos

    # Solicitamos el ID de la asistencia a eliminar
    id_asistencia = input("Ingrese el ID de la asistencia a eliminar: ")

    # Consultmos SQL para eliminar la asistencia
    consulta = "DELETE FROM Asistencia WHERE ID_ASISTENCIA = %s" #Definimos en la consulta para la tabla Asistencia a partir del ID de asistencia ingresado con el marcador %s
    cursor.execute(consulta, (id_asistencia,))  # Ejecutamos la consulta con el ID proporcionado
    conexion.commit()  # Confirmamos los cambios en la base de datos

    print("Asistencia eliminada exitosamente!")
    cursor.close()  # Cerrams el cursor
    conexion.close()  # Cerramos la conexión a la base de datos

#creamos el menu para gestionar la asistencia
def gestionar_asistencia():
    while True:  #Se va a ejecutar el menu de opciones mientras sea True y hasta encontrarse con un break
        print("\nGestión de Asistencia")
        print("========================")
        print("1. Registrar asistencia")
        print("2. Consultar asistencia")
        print("3. Modificar asistencia")
        print("4. Eliminar asistencia")
        print("5. Volver al menú principal")
        print("========================")

        opcion = input("Ingrese la opción deseada: ")  # Solicitarmos la opción al usuario

        # Ejecutamos la función correspondiente según la opción seleccionada
        if opcion == "1":
            registrar_asistencia()
        elif opcion == "2":
            consultar_asistencia()
        elif opcion == "3":
            actualizar_asistencia()
        elif opcion == "4":
            eliminar_asistencia()
        elif opcion == "5":
            break  # Salimos del bucle y volver al menú principal
        else:
            print("Opción inválida. Por favor, intente nuevamente.")
