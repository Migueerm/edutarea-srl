def sumar(a, b):
    return round(a + b, 2)


def restar(a, b):
    return round(a - b, 2)

def dividir(a, b):
    try:
        return round(a / b, 2)
    except ZeroDivisionError:
        return "Error: División por cero"


def multiplicar(a, b):
    return round(a * b, 2)
    
def sumar_n(*args):
    return round(sum(args), 2)

#FLOR
def obtener_fecha_hora():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
