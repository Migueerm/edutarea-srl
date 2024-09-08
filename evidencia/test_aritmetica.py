import aritmetica


def test_sumar():
    assert aritmetica.sumar(1.123, 2.456) == 3.58
    assert aritmetica.sumar(-1, -2) == -3.00
    assert aritmetica.sumar(0, 0) == 0.00


def test_restar():
    assert aritmetica.restar(5.55, 2.22) == 3.33
    assert aritmetica.restar(-1, 1) == -2.00
    assert aritmetica.restar(0, 0) == 0.00

def test_dividir():
    assert aritmetica.dividir(10, 2) == 5.00
    assert aritmetica.dividir(5, 2) == 2.50
    assert aritmetica.dividir(5, 0) == "Error: División por cero"


def test_multiplicar():
    assert aritmetica.multiplicar(2.5, 4) == 10.00
    assert aritmetica.multiplicar(0, 4) == 0.00
    assert aritmetica.multiplicar(-3, 3) == -9.00

def test_sumar_n():
    assert aritmetica.sumar_n(1, 2, 3) == 6.00
    assert aritmetica.sumar_n() == 0.00
    assert aritmetica.sumar_n(-1, -2, -3) == -6.00

#FLOR
def test_promedio_n():
    assert aritmetica.promedio_n(1, 2, 3, 4) == 2.50
    assert aritmetica.promedio_n(5) == 5.00
    assert aritmetica.promedio_n() == 0.00




















































if __name__ == "__main__":
    test_sumar()
    test_restar()
    test_dividir()
    test_multiplicar()
    test_sumar_n()
    test_promedio_n()
    print("Todos los tests pasaron correctamente.")
