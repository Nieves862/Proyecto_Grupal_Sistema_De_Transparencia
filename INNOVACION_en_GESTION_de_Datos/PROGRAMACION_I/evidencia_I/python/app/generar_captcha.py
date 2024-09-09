import random
from aritmetica import sumar, restar, multiplicar, dividir

def generar_captcha():
    operaciones = ['+', '-', '*', '/']
    num1 = round(random.uniform(1, 100), 2)  # Genera un número aleatorio entre 1 y 100 con 2 decimales
    num2 = round(random.uniform(1, 100), 2)
    operacion = random.choice(operaciones)
    
    if operacion == '+':
        resultado_correcto = sumar(num1, num2)
    elif operacion == '-':
        resultado_correcto = restar(num1, num2)
    elif operacion == '*':
        resultado_correcto = multiplicar(num1, num2)
    elif operacion == '/':
        if num2 != 0:  # Evitar división por cero
            resultado_correcto = dividir(num1, num2)
        else:
            return generar_captcha()  # Regenerar captcha si num2 es 0

    print(f"Captcha: {num1} {operacion} {num2} = ?")
    respuesta_usuario = input("Ingrese el resultado (con dos decimales): ")

    try:
        if round(float(respuesta_usuario), 2) == resultado_correcto:
            print("Captcha correcto.")
            return True
        else:
            print("Captcha incorrecto.")
            return False
    except ValueError:
        print("Respuesta inválida.")
        return False
