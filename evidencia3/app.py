from usuario import agregar_usuario, modificar_usuario, eliminar_usuario, buscar_usuario, mostrar_usuarios, cargar_usuarios, ordenar_usuarios_burbuja, ordenar_usuarios_python,usuarios_aleatorios
from acceso import registrar_acceso, cargar_accesos
from registros_pluviales import cargar_registros_pluviales, mostrar_registros_del_mes, graficar_datos_pluviales

def menu():
    cargar_usuarios()
    cargar_accesos()
    usuarios_aleatorios()
    while True:
        print("\nMenú:")
        print("1. Agregar usuario")
        print("2. Modificar usuario")
        print("3. Eliminar usuario")
        print("4. Buscar usuario")
        print("5. Mostrar todos los usuarios")
        print("6. Ingresar al sistema")
        print("7. Ordenar usuarios por burbuja")
        print("8. Ordenar usuarios por método sort() de Python")
        print("9. Cargar registros pluviales")
        print("10. Mostrar gráfico de lluvias")
        print("11. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            id = input("ID: ")
            usuario = input("Nombre de Usuario: ")
            clave = input("Contraseña: ")
            email = input("Email: ")
            agregar_usuario(id, usuario, clave, email)
        elif opcion == "2":
            usuario = input("Ingrese el nombre de usuario a modificar: ")
            nuevo_usuario = input("Nuevo nombre de Usuario: ")
            nueva_clave = input("Nueva contraseña: ")
            nuevo_email = input("Nuevo email: ")
            modificar_usuario(usuario, nuevo_usuario, nueva_clave, nuevo_email)
        elif opcion == "3":
            usuario = input("Ingrese el nombre de usuario o email a eliminar: ")
            eliminar_usuario(usuario)
        elif opcion == "4":
            usuario = input("Ingrese el nombre de usuario o email a buscar: ")
            buscar_usuario(usuario)
        elif opcion == "5":
            mostrar_usuarios()
        elif opcion == "6":
            usuario = input("Ingrese el nombre de usuario para ingresar al sistema: ")
            password = input("Ingrese la contraseña: ")
            registrar_acceso(usuario, password)
        elif opcion == "7":
            print("Iniciando ordenamiento por burbuja...")
            ordenar_usuarios_burbuja()
            mostrar_usuarios()
        elif opcion == "8":
            print("Iniciando ordenamiento por método sort() de Python...")
            ordenar_usuarios_python()
            mostrar_usuarios()
        elif opcion == "9":
            anio = input("Ingrese el año para cargar los registros pluviales: ")
            registros = cargar_registros_pluviales(anio)
            mes = int(input("Ingrese el mes (1-12) para mostrar los registros: "))
            mostrar_registros_del_mes(registros, mes)
        elif opcion == "10":
            anio = input("Ingrese el año para cargar los registros pluviales: ")
            registros = cargar_registros_pluviales(anio)
            graficar_datos_pluviales(registros)
        elif opcion == "11":
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    menu()
