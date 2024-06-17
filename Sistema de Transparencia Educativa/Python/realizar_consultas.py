import mysql.connector  # Importamos el conector de MySQL
from database import get_db_connection  # Importamos la función para obtener la conexión a la base de datos

# Creamos la Funcion para consultar todos los estudiantes
def consultar_estudiantes():
    conexion = get_db_connection()  # Obtenemos la conexión a la base de datos
    cursor = conexion.cursor()  # Creamos un cursor para interactuar con la base de datos

    # Hacemos la Consulta 1: Una sola tabla mostrando todos los datos
    consulta = "SELECT * FROM cuarto_año"  # Definir la consulta SQL desde la tabla Cuarto_año
    cursor.execute(consulta)  # Ejecutamos la consulta
    estudiantes = cursor.fetchall()  # Obtener todos los resultados de la consulta en una fila si lo datos coinciden con algun dato existente

    if estudiantes: # si estudiantes no esta vacio ejecutamos lo siguiente
        print("\nListado de estudiantes:")
        for estudiante in estudiantes: #iteramos con un bucle for sobe cada tupla de la lista estudiante, es decir cada tupla estudiante con varios datos que pedimos imprimir luego
            #se que mi tupla tiene 4 elementos , ID, Nombre, Apellido, DNI por eso indico la posicion del 0 al 3
            print(f"- ID: {estudiante[0]}, Nombre: {estudiante[1]} {estudiante[2]}, DNI: {estudiante[3]}") #imprimimos con formato
    else: #si estudiantes esta vacio imprimimos lo siguiente
        print("No hay estudiantes registrados.")

    cursor.close()  # Cerramos el cursor
    conexion.close()  # Cerramos la conexión a la base de datos

# Creamos la función para consultar todas las materias
def consultar_materias():
    conexion = get_db_connection()  # Obtenemos la conexión a la base de datos
    cursor = conexion.cursor()  # Creaoms un cursor para interactuar con la base de datos

    # Consulta 1: Una sola tabla mostrando todos los datos
    consulta = "SELECT * FROM Materia"  # Definir la consulta SQL desde la tabla Materia
    cursor.execute(consulta)  # Ejecutarmos la consulta  la tabla
    materias = cursor.fetchall()  # Obtenemos todos los resultados de la consulta que den positivo, 

    if materias: #si la Materias no esta vacio ejecuto lo siguiente
        print("\nListado de materias:")
        for materia in materias: # CON UN bucle for recorro las materias con los elementos que se que contine mi tabla
            print(f"- ID: {materia[0]}, Espacio: {materia[1]}, Profesor: {materia[2]}")
    else: # de lo contrario muestro el sguiente mensaje
        print("No hay materias registradas.")

    cursor.close()  # Cerramos el cursor
    conexion.close()  # Cerramos la conexión a la base de datos

# Creamos la funcion para consultar estudiantes por nombre
def consultar_estudiantes_por_nombre():
    nombre = input("Ingrese el nombre del estudiante a buscar: ")  # Solicitamos el nombre del estudiante

    conexion = get_db_connection()  # Obtenemos la conexión a la base de datos
    cursor = conexion.cursor()  # Creamos un cursor para interactuar con la base de datos

    # Creamos una consulta 2: usando una sola tabla con WHERE
    consulta = "SELECT * FROM cuarto_año WHERE Nombre = %s"  # Definimos la consulta SQL con un parámetro %s
    cursor.execute(consulta, (nombre,))  # Ejecutamos la consulta con el parámetro proporcionado
    estudiantes = cursor.fetchall()  # Obtenemos todos los resultados de la consulta

    if estudiantes: #si estudiantes no esta vacio ejecutamos
        print(f"\nEstudiantes encontrados con el nombre {nombre}:")
        #con un ciclo for recorremos los elementos que conozco que posee mi tabla estudiante
        for estudiante in estudiantes:
            print(f"- ID: {estudiante[0]}, Nombre: {estudiante[1]} {estudiante[2]}, DNI: {estudiante[3]}")

            # Consulta adicional para obtener las notas del estudiante
            #Seleccionamos dos columnas Espacio de Materia y Nota de Nota_formativa
            #obtenemos los datos desde Nota_formativa
            #Dentro unimos las tablas Nota_formativa y Materia donde ambas deben coincidir el ID_MATERIA
            #filtramos con where indicando que solo los ID_ESTUDIANTE de Nota_formativa que coincidan con el dato que ingrese con %s
            consulta_notas = """
            SELECT Materia.Espacio, Nota_Formativa.Nota 
            FROM Nota_Formativa
            INNER JOIN Materia ON Nota_Formativa.ID_MATERIA = Materia.ID_MATERIA
            WHERE Nota_Formativa.ID_ESTUDIANTE = %s
            """
            cursor.execute(consulta_notas, (estudiante[0],))  # Ejecutamos la consulta de notas con el ID del estudiante
            notas = cursor.fetchall()  # Obtenemos todos los resultados de la consulta

            if notas: #Si notas tiene algun valor ejecutamos
                print("  Notas:")
                for nota in notas: #COn un ciclo for recorro la nota de notas asignando el valor a los campos que quiero ver, de Materia y Nota
                    print(f"  - Materia: {nota[0]}, Nota: {nota[1]}")
            else: # de lo contrario muestro un mensaje
                print("  No se encontraron notas para este estudiante.")
    else: # de otro modo muestro el siguiente mensaje
        print(f"No se encontraron estudiantes con el nombre {nombre}.")

    cursor.close()  # Cerramos el cursor
    conexion.close()  # Cerramos la conexión a la base de datos

# Creamos la función para consultar un estudiante y sus notas
def consultar_estudiante_y_notas():
    id_estudiante = input("Ingrese el ID del estudiante: ")  # Solicitamos el ID del estudiante

    conexion = get_db_connection()  # Obtenemos la conexión a la base de datos
    cursor = conexion.cursor()  # Creamos un cursor para interactuar con la base de datos

    # Hacemos la Consulta 3: consultando mas de 1 tabla con INNER JOIN
    #Selecciono las columnas y tablas de mi interes
    #unimos a partir de Nota_formativa buscando que coincida ID_ESTUDIANTE
    #Unimos a partir de nota_formatia buscando que coincidan en ID_MATERIA
    #filtramos con where con el dato que ingrese por ID_ESTUDIANTE con %s

    consulta = """
    SELECT cuarto_año.Nombre, cuarto_año.Apellido, Materia.Espacio, Nota_Formativa.Nota
    FROM cuarto_año
    INNER JOIN Nota_Formativa ON cuarto_año.ID_ESTUDIANTE = Nota_Formativa.ID_ESTUDIANTE
    INNER JOIN Materia ON Nota_Formativa.ID_MATERIA = Materia.ID_MATERIA
    WHERE cuarto_año.ID_ESTUDIANTE = %s
    """
    cursor.execute(consulta, (id_estudiante,))  # Ejecutamos la consulta con el parámetro proporcionado
    resultados = cursor.fetchall()  # Obtenemos todos los resultados de la consulta

    if resultados: # Si estudiantes tiene algun valor ejecuto lo siguiente
        print(f"\nNotas del estudiante con ID {id_estudiante}:")
        for resultado in resultados: #recorro el resultados con un ciclo for buscando completar los campos de interes
            print(f"- Nombre: {resultado[0]} {resultado[1]}, Materia: {resultado[2]}, Nota: {resultado[3]}")
    else: # de lo contrario muestro el siguiente mensaje
        print(f"No se encontraron notas para el estudiante con ID {id_estudiante}.")

    cursor.close()  # Cerramos el cursor
    conexion.close()  # Cerramos la conexión a la base de datos

#Creamos la función para consultar notas por materia
def consultar_notas_por_materia():
    id_materia = input("Ingrese el ID de la materia: ")  # Solicitamos el ID de la materia

    conexion = get_db_connection()  # Obtenemos la conexión a la base de datos
    cursor = conexion.cursor()  # Creamos un cursor para interactuar con la base de datos

    # Consulta 4: para más de 1 tabla con INNER JOIN y con filtros
    #Seleccionamos las columnas de las tablas de interes
    #desde cuarto_año
    #Uniendo desde Nota_formativa con cuarto_año buscando coincidir ID_ESTUDIANTE
    #luego uniendo desde Materia con Nota_formativa buscando coincidir ID_MATERIA
    #filtrando con where donde coincida con mi busqueda del ID_MATERIA %s
    consulta = """
    SELECT cuarto_año.Nombre, cuarto_año.Apellido, Materia.Espacio, Nota_Formativa.Nota
    FROM cuarto_año
    INNER JOIN Nota_Formativa ON cuarto_año.ID_ESTUDIANTE = Nota_Formativa.ID_ESTUDIANTE
    INNER JOIN Materia ON Nota_Formativa.ID_MATERIA = Materia.ID_MATERIA
    WHERE Materia.ID_MATERIA = %s
    """
    cursor.execute(consulta, (id_materia,))  # Ejecutamos la consulta con el parámetro proporcionado
    resultados = cursor.fetchall()  # Obtenemos todos los resultados de la consulta

    if resultados: #si resultados tiene algun valor ejecuto lo siguiente
        print(f"\nNotas de la materia con ID {id_materia}:")
        for resultado in resultados: #con un ciclo for recorro resultados mostrando con formato los campos de interes
            print(f"- Nombre: {resultado[0]} {resultado[1]}, Materia: {resultado[2]}, Nota: {resultado[3]}")
    else: # de lo contrario muestro el mensaje
        print(f"No se encontraron notas para la materia con ID {id_materia}.")

    cursor.close()  # Cerramos el cursor
    conexion.close()  # Cerramos la conexión a la base de datos

#Creaos la función para gestionar el menú de consultas
def realizar_consultas():
    while True:  # Genero el bucle infinito para gestionar las opciones del menú de consultas mientras sea TRUE hasta encontrar un break
        print("\nRealización de Consultas")
        print("========================")
        print("1. Consultar estudiantes")
        print("2. Consultar materias")
        print("3. Consultar estudiante y notas")
        print("4. Consultar estudiantes por nombre")
        print("5. Consultar notas por materia")
        print("6. Volver al menú principal")
        print("========================")

        opcion = input("Ingrese la opción deseada: ")  # Solicitamos la opción al usuario

        # Ejecutamos la función correspondiente según la opción seleccionada
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
            break  # Salimos del bucle y volver al menú principal
        else:
            print("Opción inválida. Por favor, intente nuevamente.")
