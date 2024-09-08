# Importamos la función 'get_db_connection' del módulo 'database' para conectarnos a la base de datos
from database import get_db_connection


 # Creamos la funcion crear estudiantes
def crear_estudiante():
    # Obtenemoss la conexión a la base de datos
    conexion = get_db_connection() #llamo variable conexion a la conexion con la base de datos
    cursor = conexion.cursor()  # Creamos el llamado cursor usado para interactuar con la base de datos

    # Solicitamos que se ingrese los datos del estudiante
    apellido = input("Ingrese el apellido del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    email = input("Ingrese el email del estudiante: ")
    dni = input("Ingrese el DNI del estudiante: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del estudiante (YYYY-MM-DD): ")
    edad = int(input("Ingrese la edad del estudiante: "))
    telefono = input("Ingrese el teléfono del estudiante: ")
    direccion = input("Ingrese la dirección del estudiante: ")
    localidad = input("Ingrese la localidad del estudiante: ")
    provincia = input("Ingrese la provincia del estudiante: ")

    #Definimos una consulta como una cadena de texto con ""
    #Luego realizamos una operacion de Insert en la tabla cuart_año y especifiamos las columnas a rellenar con los datos
    #Despus introducimos los marcadores de posicion con %s
    consulta = """
        INSERT INTO cuarto_año (Apellido, Nombre, E_mail, DNI, Fecha_De_Nacimiento, Edad, Teléfono, Direccion, Localidad, Provincia)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
    """
    # Ejecutamos la consulta con los datos proporcionados, los datos que ingresamos
    cursor.execute(consulta, (apellido, nombre, email, dni, fecha_nacimiento, edad, telefono, direccion, localidad, provincia))
    conexion.commit()  # Confirmamos los cambios en la base de datos

    print("Estudiante creado exitosamente!") #mostramos mensaje cuando finalizamos bien la ooperacion
    cursor.close()  # Cerramos el cursor creado para interactuar con la base de datos
    conexion.close()  # Cerramos la conexión a la base de datos


#Creamos una nueva funcion para consultar estudiantes
def consultar_estudiante():
    # Obtenemos la conexión a la base de datos
    conexion = get_db_connection()
    cursor = conexion.cursor()  # Llamamos nuevamente cursor a la interaccion con la base de datos

    # Solicitar el ID del estudiante que quiero conocer los datos
    id_estudiante = input("Ingrese el ID del estudiante a consultar: ") #habilito con el input el ingreso del ID del estudiante
    consulta = "SELECT * FROM cuarto_año WHERE ID_ESTUDIANTE = %s"  # Definimos la consulta para obtener de cuarto_año segun el ID del estudiante a partir del marcador ingresado %s
    cursor.execute(consulta, (id_estudiante,))  # Ejecutams la consulta con el ID ingresado por el usuario con el input
    estudiante = cursor.fetchone()  # Obtenemos el resultado de la consulta con fetchone que devuelve una sola fila si encuentra coincidencia con el ID ingresado, sino devuelve None

    # Si se encuentra el estudiante, deberia mostrar sus datos
    if estudiante:
        print(f"ID: {estudiante[0]}")
        print(f"Apellido: {estudiante[1]}")
        print(f"Nombre: {estudiante[2]}")
        print(f"Email: {estudiante[3]}")
        print(f"DNI: {estudiante[4]}")
        print(f"Fecha de Nacimiento: {estudiante[5]}")
        print(f"Edad: {estudiante[6]}")
        print(f"Teléfono: {estudiante[7]}")
        print(f"Dirección: {estudiante[8]}")
        print(f"Localidad: {estudiante[9]}")
        print(f"Provincia: {estudiante[10]}")
    else:
        print("No se encontró estudiante con ese ID.")
    
    cursor.close()  # Cerramos el cursor que sirve de interaccion con la base de datos
    conexion.close()  # Cerramos lla conexión a la base de datos


#creamos la fucion para actualizar estudiante
def actualizar_estudiante():
    # Hacemos la conexión a la base de datos
    conexion = get_db_connection()
    cursor = conexion.cursor()  # Creamos una interaccion con la base datos llamada habitualmente cursor

    # Solicitaoms el ID del estudiante al usuario
    id_estudiante = input("Ingrese el ID del estudiante a actualizar: ")

    consulta = "SELECT * FROM cuarto_año WHERE ID_ESTUDIANTE = %s"  # Definimos la consulta como obtener de cuarto_año el ID del estudiante a partir del marcador ingresado %s
    cursor.execute(consulta, (id_estudiante,))  # Ejecuta la consulta con el ID proporcionado en el input
    resultado = cursor.fetchone()  #  Obtenemos el resultado de la consulta con fetchone que devuelve una sola fila si encuentra coincidencia con el ID ingresado, sino devuelve None


    # Si se encuentra el estudiante con el id, solicitamos nuevos datos para actualizar, sino quiero actualizar le doy enter para seguir
    if resultado:
        apellido = input("Ingrese el nuevo apellido del estudiante (o presione Enter para no cambiar): ")
        nombre = input("Ingrese el nuevo nombre del estudiante (o presione Enter para no cambiar): ")
        email = input("Ingrese el nuevo email del estudiante (o presione Enter para no cambiar): ")
        dni = input("Ingrese el nuevo DNI del estudiante (o presione Enter para no cambiar): ")
        fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento del estudiante (YYYY-MM-DD) (o presione Enter para no cambiar): ")
        edad = input("Ingrese la nueva edad del estudiante (o presione Enter para no cambiar): ")
        telefono = input("Ingrese el nuevo teléfono del estudiante (o presione Enter para no cambiar): ")
        direccion = input("Ingrese la nueva dirección del estudiante (o presione Enter para no cambiar): ")
        localidad = input("Ingrese la nueva localidad del estudiante (o presione Enter para no cambiar): ")
        provincia = input("Ingrese la nueva provincia del estudiante (o presione Enter para no cambiar): ")

        #Definimos una consulta como una cadena de texto con ""
        #Luego realizamos una operacion de Update para actualizar en la tabla cuart_año y especifiamos las columnas a rellenar con los datos
        #Despus introducimos los marcadores de posicion con %s
        consulta_actualizar = """
            UPDATE cuarto_año
            SET Apellido = %s, Nombre = %s, E_mail = %s, DNI = %s, Fecha_De_Nacimiento = %s, Edad = %s, Teléfono = %s, Direccion = %s, Localidad = %s, Provincia = %s
            WHERE ID_ESTUDIANTE = %s
        """
        # Ejecuta la consulta actualizar con dos argumentos, el primero es la consulta a actualizar y el segundo una tupla
        cursor.execute(consulta_actualizar, ( # usamos una expresion condicional para determinar que valor usaremos
            apellido if apellido else resultado[1], # si ingresamos un nuevo apellido, usamos ese apellido sino, si deje el espacio vacio, se mantiene el valor que tenia en resultado, obtenido de la base de datos
            nombre if nombre else resultado[2],
            email if email else resultado[3],
            dni if dni else resultado[4],
            fecha_nacimiento if fecha_nacimiento else resultado[5],
            edad if edad else resultado[6],
            telefono if telefono else resultado[7],
            direccion if direccion else resultado[8],
            localidad if localidad else resultado[9],
            provincia if provincia else resultado[10],
            id_estudiante #ultimo valor de mi tupla que indica que alimno actualizar
        ))
        conexion.commit()  # Confirmamos los cambios en la base de datos
        print("Estudiante actualizado exitosamente!")
    else:
        print(f"No se encontró estudiante con el ID: {id_estudiante}")

    cursor.close()  # Cerramos el cursor
    conexion.close()  # Cerramos la conexión a la base de datos


#Creamos la funcion para eliminar datos del estudiante
def eliminar_estudiante():
    # Hacemos la conexión a la base de datos
    conexion = get_db_connection()
    cursor = conexion.cursor()  # Creamos una interaccion con la base datos llamada habitualmente cursor

    # Solicitamos el ID del estudiante al usuario que ingrese
    id_estudiante = input("Ingrese el ID del estudiante a eliminar: ")

    consulta = "SELECT * FROM cuarto_año WHERE ID_ESTUDIANTE = %s"  # Definimos la consulta como obtener de cuarto_año el ID del estudiante a partir del marcador ingresado %s
    cursor.execute(consulta, (id_estudiante,)) # Ejecuta la consulta con el ID proporcionado en el input anterior
    resultado = cursor.fetchone()  # Obtener el resultado de la consulta

    # Si se encuentra el estudiante, confirmar la eliminación
    if resultado: #Verificamos la variable resultado, si encuentra un id que coincida con id_estudiante, sino devolveria None
        confirmar = input(f"¿Está seguro de eliminar al estudiante {resultado[1]} {resultado[2]} (S/N): ") #preguntamos si queremos confirmar la eliminacion, usamos f  para consultar sobre resultado 1 y 2 que son el  apellido y nombre
        if confirmar.upper() == "S":  #Pedimos una S para decir Si y confirmar
            consulta_eliminar = "DELETE FROM cuarto_año WHERE ID_ESTUDIANTE = %s"  # creamos la Consulta SQL para eliminar al estudiante usando DElete en cuarto_año si en el ID elegido
            cursor.execute(consulta_eliminar, (id_estudiante,))  # Ejecutams la consulta con el ID proporcionado para eliminarlo
            conexion.commit()  # Confirmamos los cambios en la base de datos
            print("Estudiante eliminado exitosamente!")
        else:
            print("Eliminación cancelada.")
    else:
        print(f"No se encontró estudiante con el ID: {id_estudiante}")

    cursor.close()  # Cerramos el cursor
    conexion.close()  # Cerrar=mos la conexión a la base de datos

#creamos la fucion gestionar estudiantes para crear un menu de opciones
def gestionar_estudiantes():
    # Bucle infinito para gestionar las opciones del menú de estudiantes
    while True: #Se va a ejecutar el menu de opciones mientras sea True y hasta encontrarse con un break
        print("\nGestión de Estudiantes")
        print("========================")
        print("1. Registrar estudiante")
        print("2. Consultar estudiante")
        print("3. Modificar estudiante")
        print("4. Eliminar estudiante")
        print("5. Volver al menú principal")
        print("========================")

        opcion = input("Ingrese la opción deseada: ") # Pedimos ingresar una opcion

        # Ejecutar la función correspondiente según la opción seleccionada
        if opcion == "1":
            crear_estudiante()
        elif opcion == "2":
            consultar_estudiante()
        elif opcion == "3":
            actualizar_estudiante()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            break  # Salir del bucle y volver al menú principal
        else:
            print("Opción inválida. Por favor, intente nuevamente.")
