from usuario import agregar_usuario, modificar_usuario, eliminar_usuario, buscar_usuario, mostrar_usuarios, cargar_usuarios
from acceso import registrar_acceso, cargar_accesos

def menu():
    cargar_usuarios()
    cargar_accesos()
    while True:
        print("\nMenú:")
        print("1. Agregar usuario")
        print("2. Modificar usuario")
        print("3. Eliminar usuario")
        print("4. Buscar usuario")
        print("5. Mostrar todos los usuarios")
        print("6. Ingresar al sistema")
        print("7. Salir")

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
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    menu()



