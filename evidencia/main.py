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
            
  usuarios[nombre_usuario] = {
        'nombre': nombre,
        'apellido': apellido,
        'dni': dni,
        'correo': correo,
        'fecha_nacimiento': fecha_nacimiento,
        'clave': clave
    }
   
    print(f"Usuario {nombre_usuario} registrado exitosamente.")
   
    # Guardar en archivo de texto
    with open('usuariosCreados.txt', 'a') as file:
        file.write(f"Usuario creado: {nombre_usuario}, DNI: {dni}, Fecha de creación: {aritmetica.obtener_fecha_hora()}\n")


def iniciar_sesion():
    nombre_usuario = input("Nombre de usuario: ")
    if nombre_usuario not in usuarios:
        print("Usuario no encontrado.")
        return
   
    intentos = 0
    while intentos < 4:
        clave = input("Clave: ")
        if usuarios[nombre_usuario]['clave'] == clave:
            print(f"Bienvenido {usuarios[nombre_usuario]['nombre']}.")
           
            # Guardar en archivo de texto
            with open('ingresos.txt', 'a') as file:
                file.write(f"Usuario: {nombre_usuario} ingresó el {aritmetica.obtener_fecha_hora()}\n")
            return
       
        else:
            intentos += 1
            print(f"Clave incorrecta. Intento {intentos} de 4.")

            
            
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
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            print("Saliendo...")
            break
        elif opcion == "4":
            olvido_contrasena()
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu_principal()


