#biblioteca estándar que proporciona funciones para generar números aleatorios y realizar otras operaciones relacionadas con la aleatoriedad.
import random
import aritmetica


usuarios = {}


def validar_clave(clave):
    if len(clave) < 8:
        return False
    condiciones = [
        any(c.islower() for c in clave),
        any(c.isupper() for c in clave),
        any(c.isdigit() for c in clave),
        any(c in '!@#$%^&*()-_+=' for c in clave)
    ]
    return sum(condiciones) >= 2


def registrar_usuario():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    if dni in [usuario['dni'] for usuario in usuarios.values()]:
        print("DNI ya registrado.")
        return
