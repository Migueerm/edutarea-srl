from gestionUsuario import cargar_usuarios, menu_crud_usuarios, usuarios_aleatorios
from gestionAcceso import cargar_accesos, registrar_acceso, menu_accesos
from gestionBusquedaOrdenamiento import gestionar_busqueda_y_ordenamiento
from gestionPluviales import menu_analisis_datos_pluviales

# Menú principal de la aplicación
def main_menu():
    print("Bienvenido a la Aplicación")
    cargar_usuarios()
    cargar_accesos()
    usuarios_aleatorios()  # Generar usuarios aleatorios al inicio
    while True:
        print("\n--- Menú Principal ---")
        print("1. Usuarios y Accesos de la Aplicación")
        print("2. Ingresar al sistema con los datos de usuario")
        print("3. Análisis de Datos Pluviales")
        print("4. Salir de la aplicación")

        option = input("Seleccione una opción: ")
        if option == '1':
            submenu_usuarios_y_accesos()
        elif option == '2':
            login_usuario()
        elif option == '3':
            menu_analisis_datos_pluviales()
        elif option == '4':
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Función de inicio de sesión para la opción 2 del menú principal
def login_usuario():
    usuario = input("Ingrese el nombre de usuario para ingresar al sistema: ")
    password = input("Ingrese la contraseña: ")
    registrar_acceso(usuario, password)

# Menú Usuarios y Accesos
def submenu_usuarios_y_accesos():
    while True:
        print("\n--- Usuarios y Accesos de la Aplicación ---")
        print("a. CRUD de Usuarios")
        print("b. Mostrar datos de Accesos")
        print("c. Ordenamiento y Búsqueda de Usuarios")
        print("d. Volver al Menú principal")

        option = input("Seleccione una opción: ")
        if option == 'a':
            menu_crud_usuarios()
        elif option == 'b':
            menu_accesos()
        elif option == 'c':
            gestionar_busqueda_y_ordenamiento()
        elif option == 'd':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main_menu()
