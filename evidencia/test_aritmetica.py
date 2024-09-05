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
