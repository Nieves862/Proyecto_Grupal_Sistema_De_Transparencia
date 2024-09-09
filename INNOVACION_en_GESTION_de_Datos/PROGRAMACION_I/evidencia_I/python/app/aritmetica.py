def sumar(a: float, b: float) -> float:
    return round(a + b, 2)

def restar(a: float, b: float) -> float:
    return round(a - b, 2)

def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return round(a / b, 2)

def multiplicar(a: float, b: float) -> float:
    return round(a * b, 2)

def sumar_n(*numeros: float) -> float:
    return round(sum(numeros), 2)

def promedio_n(*numeros: float) -> float:
    if not numeros:
        raise ValueError("No se pueden calcular promedios de una lista vacía.")
    return round(sum(numeros) / len(numeros), 2)
