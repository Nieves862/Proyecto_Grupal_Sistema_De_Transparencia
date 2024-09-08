def sumar_n(*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return round(suma,2)

def promedio_n(*numeros):

    if not numeros:
        return 0  
    return round(sumar_n(*numeros) / len(numeros),2)

def calculadora():
    while True:
        print("Seleccione la operación:") 
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sumar n números")
        print("6. Promedio de n números")
        print("7. Salir")

        opcion = input("Ingrese su opción (1/2/3/4/5/6/7): ")

        if opcion in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                if opcion == '1':
                    suma = round(num1 + num2,2)
                    print(suma)
                elif opcion == '2':
                    print(num1, "-", num2, "=", num1 - num2)
                elif opcion == '3':
                    print(num1, "*", num2, "=", num1 * num2)
                elif opcion == '4':
                    if num2 == 0:
                        print("No se puede dividir por cero.")
                    else:
                        print(num1, "/", num2, "=", num1 / num2)
            except ValueError:
                print("Por favor, ingrese solo números.")
        elif opcion == '5':
            cantidad = int(input("Ingrese la cantidad de números a sumar: "))
            numeros = []
            for _ in range(cantidad):
                numeros.append(float(input("Ingrese un número: ")))
            print("La suma es:", sumar_n(*numeros))
        elif opcion == '6':
            cantidad = int(input("Ingrese la cantidad de números: "))
            numeros = []
            for _ in range(cantidad):
                numeros.append(float(input("Ingrese un número: ")))
            print("El promedio es:", promedio_n(*numeros))
        elif opcion == '7':
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    calculadora()