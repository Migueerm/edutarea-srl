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
    
    #FLOR
      # Registrar intento fallido
            with open('log.txt', 'a') as file:
                file.write(f"Intento fallido para el usuario {nombre_usuario} el {aritmetica.obtener_fecha_hora()}\n")
           
            if intentos == 4:
                print("Usuario bloqueado.")
                break


def olvido_contrasena():
    print("Función no implementada.")
    pass


def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Iniciar Sesión")
        print("2. Registrar Usuario")
        print("3. Salir")
        print("4. Olvidé la contraseña")

