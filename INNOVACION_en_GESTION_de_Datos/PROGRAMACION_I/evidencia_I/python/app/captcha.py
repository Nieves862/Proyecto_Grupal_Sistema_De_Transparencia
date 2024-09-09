from aritmetica import sumar, restar, dividir, multiplicar, sumar_n, promedio_n
import random

def generar_captcha():
    """Genera un CAPTCHA matemático aleatorio."""
    
    # Seleccionar aleatoriamente una operación
    operaciones = [sumar, restar, multiplicar, dividir]
    signos = {0: "+", 1: "-", 2: "*", 3: "/"}
    operacion = random.choice(operaciones)
    
    # Obtener el índice de la operación y su signo correspondiente
    indice_operacion = operaciones.index(operacion)
    signo = signos[indice_operacion]

    # Generar números aleatorios
    num1 = round(random.uniform(0, 10), 2)
    num2 = round(random.uniform(0, 10), 2)
    
    # Realizar la operación
    try:
        resultado = operacion(num1, num2)
    except ValueError as e:
        # En caso de división por cero, volver a generar el CAPTCHA
        print(e)
        return generar_captcha()

    # Presentar la pregunta al usuario
    print(f"¿Cuánto es {num1} {signo} {num2}?")

    # Obtener la respuesta del usuario
    while True:
        try:
            respuesta_usuario = float(input("Respuesta: "))
            break
        except ValueError:
            print("Por favor, ingrese un número.")

    # Verificar la respuesta
    return respuesta_usuario == resultado