def sumar(a, b):
    return round(a + b, 2)


def restar(a, b):
    return round(a - b, 2)

#FLOR
def obtener_fecha_hora():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
