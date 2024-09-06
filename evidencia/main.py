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
  correo = input("Correo: ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")


    nombre_usuario = input("Nombre de usuario: ")
    if len(nombre_usuario) < 6 or len(nombre_usuario) > 12 or nombre_usuario in usuarios:
        print("El nombre de usuario debe tener entre 6 y 12 caracteres y ser único.")
        return


    clave = input("Clave: ")
    if not validar_clave(clave):
        print("La clave no cumple con los requisitos de seguridad. Debe poseer al menos 8 caracteres. Usar al menos una minúscula, una mayúscula, un número y un caracter especial")
        return


    # CAPTCHA
    while True:
        operacion = random.choice([aritmetica.sumar, aritmetica.restar, aritmetica.multiplicar, aritmetica.dividir])
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        resultado = operacion(a, b)
       
        if isinstance(resultado, float):
            captcha = float(input(f"Resuelve el CAPTCHA: {a} {operacion.__name__} {b} = "))
            if captcha == resultado:
                print("CAPTCHA correcto. Usuario registrado.")
                break
            else:
                print("CAPTCHA incorrecto. Inténtalo nuevamente o presiona 'q' para salir.")
                if input().lower() == 'q':
                    return
        else:
            print("Operación inválida. Inténtalo de nuevo.")

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

