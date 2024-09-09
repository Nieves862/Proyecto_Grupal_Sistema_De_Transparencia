from aritmetica import sumar, restar, dividir, multiplicar, sumar_n, promedio_n

def test_sumar():
    assert sumar(2, 3) == 5.00
    assert sumar(-2, 3) == 1.00
    assert sumar(0.1, 0.2) == 0.30

def test_restar():
    assert restar(5, 3) == 2.00
    assert restar(-1, -2) == 1.00
    assert restar(0.5, 0.2) == 0.30

def test_dividir():
    assert dividir(10, 2) == 5.00
    assert dividir(0.1, 0.2) == 0.50
    try:
        dividir(1, 0)
    except ValueError as e:
        assert str(e) == "No se puede dividir por cero."

def test_multiplicar():
    assert multiplicar(2, 3) == 6.00
    assert multiplicar(-1, 3) == -3.00
    assert multiplicar(0.1, 0.2) == 0.02

def test_sumar_n():
    assert sumar_n(1, 2, 3) == 6.00
    assert sumar_n(0.1, 0.2, 0.3) == 0.60
    assert sumar_n(-1, -2, -3) == -6.00

def test_promedio_n():
    assert promedio_n(1, 2, 3) == 2.00
    assert promedio_n(0.1, 0.2, 0.3) == 0.20
    assert promedio_n(10, 20, 30) == 20.00
    try:
        promedio_n()
    except ValueError as e:
        assert str(e) == "No se pueden calcular promedios de una lista vacía."

if __name__ == "__main__":
    test_sumar()
    test_restar()
    test_dividir()
    test_multiplicar()
    test_sumar_n()
    test_promedio_n()
