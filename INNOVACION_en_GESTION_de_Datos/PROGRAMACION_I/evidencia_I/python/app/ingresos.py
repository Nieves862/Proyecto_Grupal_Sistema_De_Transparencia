from datetime import datetime

def guardar_ingreso(nombre_usuario):
    fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("ingresos.txt", "a") as file:
        file.write(f"Usuario: {nombre_usuario}, Fecha de ingreso: {fecha_ingreso}\n")
    print("Ingreso registrado correctamente.")
