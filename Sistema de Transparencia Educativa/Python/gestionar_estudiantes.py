from database import get_db_connection

def crear_estudiante():
    conexion = get_db_connection()
    cursor = conexion.cursor()

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

    consulta = """
        INSERT INTO cuarto_año (Apellido, Nombre, E_mail, DNI, Fecha_De_Nacimiento, Edad, Teléfono, Direccion, Localidad, Provincia)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(consulta, (apellido, nombre, email, dni, fecha_nacimiento, edad, telefono, direccion, localidad, provincia))
    conexion.commit()

    print("Estudiante creado exitosamente!")
    cursor.close()
    conexion.close()

def consultar_estudiante():
    conexion = get_db_connection()
    cursor = conexion.cursor()

    id_estudiante = input("Ingrese el ID del estudiante a consultar: ")
    consulta = "SELECT * FROM cuarto_año WHERE ID_ESTUDIANTE = %s"
    cursor.execute(consulta, (id_estudiante,))
    estudiante = cursor.fetchone()

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
    
    cursor.close()
    conexion.close()

def actualizar_estudiante():
    conexion = get_db_connection()
    cursor = conexion.cursor()

    id_estudiante = input("Ingrese el ID del estudiante a actualizar: ")

    consulta = "SELECT * FROM cuarto_año WHERE ID_ESTUDIANTE = %s"
    cursor.execute(consulta, (id_estudiante,))
    resultado = cursor.fetchone()

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

        consulta_actualizar = """
            UPDATE cuarto_año
            SET Apellido = %s, Nombre = %s, E_mail = %s, DNI = %s, Fecha_De_Nacimiento = %s, Edad = %s, Teléfono = %s, Direccion = %s, Localidad = %s, Provincia = %s
            WHERE ID_ESTUDIANTE = %s
        """
        cursor.execute(consulta_actualizar, (
            apellido if apellido else resultado[1],
            nombre if nombre else resultado[2],
            email if email else resultado[3],
            dni if dni else resultado[4],
            fecha_nacimiento if fecha_nacimiento else resultado[5],
            edad if edad else resultado[6],
            telefono if telefono else resultado[7],
            direccion if direccion else resultado[8],
            localidad if localidad else resultado[9],
            provincia if provincia else resultado[10],
            id_estudiante
        ))
        conexion.commit()
        print("Estudiante actualizado exitosamente!")
    else:
        print(f"No se encontró estudiante con el ID: {id_estudiante}")

    cursor.close()
    conexion.close()

def eliminar_estudiante():
    conexion = get_db_connection()
    cursor = conexion.cursor()

    id_estudiante = input("Ingrese el ID del estudiante a eliminar: ")

    consulta = "SELECT * FROM cuarto_año WHERE ID_ESTUDIANTE = %s"
    cursor.execute(consulta, (id_estudiante,))
    resultado = cursor.fetchone()

    if resultado:
        confirmar = input(f"¿Está seguro de eliminar al estudiante {resultado[1]} {resultado[2]} (S/N): ")
        if confirmar.upper() == "S":
            consulta_eliminar = "DELETE FROM cuarto_año WHERE ID_ESTUDIANTE = %s"
            cursor.execute(consulta_eliminar, (id_estudiante,))
            conexion.commit()
            print("Estudiante eliminado exitosamente!")
        else:
            print("Eliminación cancelada.")
    else:
        print(f"No se encontró estudiante con el ID: {id_estudiante}")

    cursor.close()
    conexion.close()

def gestionar_estudiantes():
    while True:
        print("\nGestión de Estudiantes")
        print("========================")
        print("1. Registrar estudiante")
        print("2. Consultar estudiante")
        print("3. Modificar estudiante")
        print("4. Eliminar estudiante")
        print("5. Volver al menú principal")
        print("========================")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            crear_estudiante()
        elif opcion == "2":
            consultar_estudiante()
        elif opcion == "3":
            actualizar_estudiante()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")
