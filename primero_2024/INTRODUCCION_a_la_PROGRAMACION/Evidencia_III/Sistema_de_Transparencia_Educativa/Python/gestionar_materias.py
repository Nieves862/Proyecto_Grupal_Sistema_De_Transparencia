from database import get_db_connection  # Importar la función para obtener la conexión a la base de datos


#creamos la funcion crear_materia para crearlas
def crear_materia():
    conexion = get_db_connection()  #llamo variable conexion a la conexion con la base de datos 
    cursor = conexion.cursor()  # Creaamos el cursor para interactuar con la base de datos

    # Solicitamos los datos de la nueva materia al usuario que ingrese
    espacio = input("Ingrese el nombre del espacio: ")
    profesor = input("Ingrese el nombre del profesor: ")
    detalle = input("Ingrese los detalles de la materia: ")
    carga_horaria = int(input("Ingrese la carga horaria de la materia: "))

    #Definimos una consulta como una cadena de texto con ""
    #Luego realizamos una operacion de Insert en la tabla Materia y especifiamos las columnas a rellenar con los datos
    #Despus introducimos los marcadores de posicion con %s
    consulta = """
        INSERT INTO Materia (Espacio, Profesor, Detalle, Carga_Horaria)
        VALUES (%s, %s, %s, %s)
    """
    # Ejecutamos la consulta con los datos proporcionados por el usuario
    cursor.execute(consulta, (espacio, profesor, detalle, carga_horaria))
    conexion.commit()  # Confirmamos los cambios en la base de datos

    print("Materia creada exitosamente!")
    cursor.close()  # Cerramos el cursor
    conexion.close()  # Cerramo la conexión a la base de datos

#creamos la funcion consultar amteria
def consultar_materia():
    conexion = get_db_connection()  # Obtenemos la conexión a la base de datos
    cursor = conexion.cursor()  # Creamos la variable cursor para interactuar con la base de datos

    # Solicitamos el ID de la materia a consultar
    id_materia = input("Ingrese el ID de la materia a consultar: ")
    # Consulta SQL para obtener los datos de la materia
    consulta = "SELECT * FROM Materia WHERE ID_MATERIA = %s" # Definimos en la consulta como obtener la Materia a partir del ID de la materia ingresado con el marcador %s
    cursor.execute(consulta, (id_materia,))  # # Ejecutamos la consulta con el ID ingresado por el usuario con el input
    materia = cursor.fetchone()  # Obtenemos el resultado de la consulta con fetchone que devuelve una sola fila si encuentra coincidencia con el ID ingresado, sino devuelve None

    # Mostramos los datos de la materia si se encuentra por ID, con los campos de cada materia que coincidieron en el paso anterior
    if materia: #si hubo coincidencia
        print(f"ID: {materia[0]}, Espacio: {materia[1]}, Profesor: {materia[2]}, Detalle: {materia[3]}, Carga Horaria: {materia[4]}")
    else: #de lo contrario
        print(f"No se encontró materia con el ID: {id_materia}")

    cursor.close()  # Cerramos el cursor
    conexion.close()  # Cerramos la conexión a la base de datos

#creamos la funcion apra actializar la materia
def actualizar_materia():
    conexion = get_db_connection()  # Obtenemos la conexión a la base de datos
    cursor = conexion.cursor()  # # Creamos una interaccion con la base datos llamada habitualmente cursor

    # Solicitamos los nuevos datos de la materia al usuario
    id_materia = input("Ingrese el ID de la materia a actualizar: ")
    espacio = input("Ingrese el nuevo nombre del espacio: ")
    profesor = input("Ingrese el nuevo nombre del profesor: ")
    detalle = input("Ingrese los nuevos detalles de la materia: ")
    carga_horaria = int(input("Ingrese la nueva carga horaria de la materia: "))

    #Definimos una consulta como una cadena de texto con ""
    #Luego realizamos una operacion de Update para actualizar en la tabla Materia y especifiamos las columnas a rellenar con los datos
    #Despus introducimos los marcadores de posicion con %s
    consulta = """
        UPDATE Materia
        SET Espacio = %s, Profesor = %s, Detalle = %s, Carga_Horaria = %s
        WHERE ID_MATERIA = %s
    """
    # Ejecutams la consulta con los nuevos datos proporcionados
    cursor.execute(consulta, (espacio, profesor, detalle, carga_horaria, id_materia))
    conexion.commit()  # Confirmamos los cambios en la base de datos

    print("Materia actualizada exitosamente!")
    cursor.close()  # Cerramos el cursor
    conexion.close()  # Cerramos la conexión a la base de datos

#hacemos una funcion para eliminar la materia
def eliminar_materia():
    conexion = get_db_connection()  # Obtenemos la conexión a la base de datos
    cursor = conexion.cursor()  # Creaamos  la vriable cursor para interactuar con la base de datos

    # Solicitamos el ID de la materia a eliminar
    id_materia = input("Ingrese el ID de la materia a eliminar: ")

    # Consulta SQL para eliminar la materia
    consulta = "DELETE FROM Materia WHERE ID_MATERIA = %s" #Definimos en la consulta como eliminar de la tabla Materia a partir del ID de la materia ingresado con el marcador %s
    cursor.execute(consulta, (id_materia,))  # Ejecutamos la consulta con el ID proporcionado
    conexion.commit()  # Confirmamos los cambios en la base de datos

    print("Materia eliminada exitosamente!")
    cursor.close()  # Cerramos el cursor
    conexion.close()  # Cerramos la conexión a la base de datos


#creamos la funcion par gestionar el menu de las materias 
def gestionar_materias():
    while True:  ##Se va a ejecutar el menu de opciones mientras sea True y hasta encontrarse con un break
        print("\nGestión de Materias")
        print("========================")
        print("1. Registrar materia")
        print("2. Consultar materia")
        print("3. Modificar materia")
        print("4. Eliminar materia")
        print("5. Volver al menú principal")
        print("========================")

        opcion = input("Ingrese la opción deseada: ")  # Solicitamos la opción al usuario

        # Ejecutamos la función correspondiente según la opción seleccionada
        if opcion == "1":
            crear_materia()
        elif opcion == "2":
            consultar_materia()
        elif opcion == "3":
            actualizar_materia()
        elif opcion == "4":
            eliminar_materia()
        elif opcion == "5":
            break  # Salir del bucle y volver al menú principal
        else:
            print("Opción inválida. Por favor, intente nuevamente.")
