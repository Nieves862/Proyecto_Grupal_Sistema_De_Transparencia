from database import get_db_connection  # Importamos la función para obtener la conexión a la base de datos

#Creamos la funcion para crear calificaciones

def crear_calificacion():
    conexion = get_db_connection()  #llamo variable conexion a la conexion con la base de datos 
    cursor = conexion.cursor()  #Creaamos el cursor para interactuar con la base de datos


    # Solicitamos los datos de la nueva calificación al usuario para su ID, materia, nota, fecha y tipo de examen
    id_estudiante = input("Ingrese el ID del estudiante: ")
    id_materia = input("Ingrese el ID de la materia: ")
    nota = int(input("Ingrese la nota: "))
    fecha_examen = input("Ingrese la fecha del examen (YYYY-MM-DD): ")
    tipo_examen = input("Ingrese el tipo de examen (Recuperatorio/Final): ")

    #Consultamos el SQL para insertar una nueva calificación
    #Definimos una consulta como una cadena de texto con ""
    #Luego realizamos una operacion de Insert en la tabla Nota_formtiva y especifiamos las columnas a rellenar con los datos
    #Despus introducimos los marcadores de posicion con %s
    consulta = """
        INSERT INTO Nota_Formativa (ID_ESTUDIANTE, ID_MATERIA, Nota, Fecha_Exámen, Tipo_Exámen)
        VALUES (%s, %s, %s, %s, %s)
    """
    # Ejecutamos la consulta con los datos proporcionados por el usuario
    cursor.execute(consulta, (id_estudiante, id_materia, nota, fecha_examen, tipo_examen))
    conexion.commit()  # Confirmams los cambios en la base de datos

    print("Calificación creada exitosamente!")
    cursor.close()  # Cerramos el cursor
    conexion.close()  # Cerrams la conexión a la base de datos


#Creamos una funcion para consltar por calificaciones
def consultar_calificacion():
    conexion = get_db_connection()  #llamo a la variable conexion, para la conexion con la base de datos 
    cursor = conexion.cursor()   #Creaamos la variable cursor para interactuar con la base de datos

    # Solicitamos el ID de la calificación buscada
    id_calificacion = input("Ingrese el ID de la calificación a consultar: ")
    # Consulta SQL para obtener los datos de la calificación
    consulta = "SELECT * FROM Nota_Formativa WHERE ID_NOTA_Formativa = %s" # Definimos en la consulta para obtener de la tabla Nota_formatica a partir del ID de la nota ingresada con el marcador %s
    cursor.execute(consulta, (id_calificacion,))  # Ejecutamos la consulta con el ID proporcionado
    calificacion = cursor.fetchone()  # Obtenemos el resultado de la consulta

    # Mostramos los datos de la calificación si se encuentra coincidencia con la busqueda de arriba
    if calificacion:
        print(f"ID: {calificacion[0]}, ID Estudiante: {calificacion[1]}, ID Materia: {calificacion[2]}, Nota: {calificacion[3]}, Fecha Examen: {calificacion[4]}, Tipo Examen: {calificacion[5]}")
    else:
        print(f"No se encontró calificación con el ID: {id_calificacion}")

    cursor.close()  # Cerramos el cursor
    conexion.close()  # Cerramos la conexión a la base de datos


#Creamos una funcion para actualizar las notas
def actualizar_calificacion():
    conexion = get_db_connection()  # Obtenemos la conexión a la base de datos con esta variable
    cursor = conexion.cursor()  # Creamos una variable cursor para interactuar con la base de datos

    # Solicitamos los nuevos datos de la calificación al usuario
    id_calificacion = input("Ingrese el ID de la calificación a actualizar: ")
    id_estudiante = input("Ingrese el nuevo ID del estudiante: ")
    id_materia = input("Ingrese el nuevo ID de la materia: ")
    nota = int(input("Ingrese la nueva nota: "))
    fecha_examen = input("Ingrese la nueva fecha del examen (YYYY-MM-DD): ")
    tipo_examen = input("Ingrese el nuevo tipo de examen (Recuperatorio/Final): ")

    # Consultamos SQL para actualizar los datos de la calificación
    # Consultamos el SQL para insertar una nueva calificación
    #Definimos una consulta como una cadena de texto con ""
    #Luego realizamos una operacion de Insert en la tabla Nota_formtiva y especifiamos las columnas a rellenar con los datos
    #Despus introducimos los marcadores de posicion con %s
    consulta = """
        UPDATE Nota_Formativa
        SET ID_ESTUDIANTE = %s, ID_MATERIA = %s, Nota = %s, Fecha_Exámen = %s, Tipo_Exámen = %s
        WHERE ID_NOTA_Formativa = %s
    """
    # Ejecutamos la consulta con los nuevos datos proporcionados
    cursor.execute(consulta, (id_estudiante, id_materia, nota, fecha_examen, tipo_examen, id_calificacion))
    conexion.commit()  # Confirmamos los cambios en la base de datos

    print("Calificación actualizada exitosamente!")
    cursor.close()  # Cerramos el cursor
    conexion.close()  # Cerramos la conexión a la base de datos


#Creamos una funcion para eliminar las calificaciones
def eliminar_calificacion():
    conexion = get_db_connection()  # Obtenemos la conexión a la base de datos
    cursor = conexion.cursor()  # Creamos una variable cursor para interactuar con la base de datos

    # Solicitamos el ID de la calificación a eliminar
    id_calificacion = input("Ingrese el ID de la calificación a eliminar: ")
    # Consultamos SQL para eliminar la calificación
    consulta = "DELETE FROM Nota_Formativa WHERE ID_NOTA_Formativa = %s" # Definimos en la consulta para obtener de la tabla Nota_formatica a partir del ID de la nota ingresada con el marcador %s
    cursor.execute(consulta, (id_calificacion,))  # Ejecutar la consulta con el ID proporcionado
    conexion.commit()  # Confirmar los cambios en la base de datos

    print("Calificación eliminada exitosamente!")
    cursor.close()  # Cerramos el cursor
    conexion.close()  # Cerramos la conexión a la base de datos


#Creamos una funcion para gestionar con un menu las califiaciones
def gestionar_calificaciones():
    while True:  #Se va a ejecutar el menu de opciones mientras sea True y hasta encontrarse con un break
        print("\nGestión de Calificaciones")
        print("========================")
        print("1. Registrar calificación")
        print("2. Consultar calificación")
        print("3. Modificar calificación")
        print("4. Eliminar calificación")
        print("5. Volver al menú principal")
        print("========================")

        opcion = input("Ingrese la opción deseada: ")  # Solicitamos la opción al usuario

        # Ejecutams la función correspondiente según la opción seleccionada
        if opcion == "1":
            crear_calificacion()
        elif opcion == "2":
            consultar_calificacion()
        elif opcion == "3":
            actualizar_calificacion()
        elif opcion == "4":
            eliminar_calificacion()
        elif opcion == "5":
            break  # Salir del bucle y volver al menú principal
        else:
            print("Opción inválida. Por favor, intente nuevamente.")
