import pickle
from datetime import datetime

# db_config.py
#usar para conectar a la base de datos. La contraseña debe ser reemplazadas :)

def get_db_connection():
    import mysql.connector
    return mysql.connector.connect(
        host="3306",
        user="root",
        password="Aasx76tcy_2791",
        database="edutareas"
    )



# Clase Usuario
class Usuario:
    def __init__(self, user_id, username, password, email):
        self.id = user_id
        self.username = username
        self.password = password
        self.email = email


    def __repr__(self):
        return f"ID: {self.id}, Username: {self.username}, Email: {self.email}"




# Clase Acceso
class Acceso:
    def __init__(self, acceso_id, usuario_logueado):
        self.id = acceso_id
        self.fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.fecha_salida = None
        self.usuario_logueado = usuario_logueado


    def registrar_salida(self):
        self.fecha_salida = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def __repr__(self):
        return f"Acceso ID: {self.id}, Usuario: {self.usuario_logueado.username}, Ingreso: {self.fecha_ingreso}, Salida: {self.fecha_salida}"




# Guardar y cargar datos usando archivos binarios
def guardar_datos(archivo, datos):
    with open(archivo, 'wb') as file:
        pickle.dump(datos, file)




def cargar_datos(archivo):
    try:
        with open(archivo, 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return []




# Registrar intentos fallidos de acceso
def registrar_intento_fallido(username, password):
    with open('logs.txt', 'a') as log_file:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{fecha} - Intento fallido con Username: {username}, Password: {password}\n")




# Cargar usuarios y accesos
usuarios = cargar_datos('usuarios.ispc')
accesos = cargar_datos('accesos.ispc')




# Agregar un nuevo usuario
def agregar_usuario():
    user_id = len(usuarios) + 1
    username = input("Ingrese username: ")
    email = input("Ingrese email: ")
    password = input("Ingrese password: ")


    # Crear y guardar el usuario
    nuevo_usuario = Usuario(user_id, username, password, email)
    usuarios.append(nuevo_usuario)
    guardar_datos('usuarios.ispc', usuarios)
    print("Usuario agregado exitosamente.")




# Modificar un usuario
def modificar_usuario():
    username = input("Ingrese el username del usuario a modificar: ")
    for usuario in usuarios:
        if usuario.username == username:
            nuevo_email = input("Nuevo email: ")
            nuevo_password = input("Nuevo password: ")
            usuario.email = nuevo_email
            usuario.password = nuevo_password
            guardar_datos('usuarios.ispc', usuarios)
            print("Usuario modificado exitosamente.")
            return
    print("Usuario no encontrado.")




# Eliminar un usuario
def eliminar_usuario():
    username = input("Ingrese el username del usuario a eliminar: ")
    for usuario in usuarios:
        if usuario.username == username:
            usuarios.remove(usuario)
            guardar_datos('usuarios.ispc', usuarios)
            print("Usuario eliminado exitosamente.")
            return
    print("Usuario no encontrado.")




# Buscar usuario
def buscar_usuario():
    username = input("Ingrese username o email a buscar: ")
    for usuario in usuarios:
        if usuario.username == username or usuario.email == username:
            print(usuario)
            return
    print("Usuario no encontrado.")




# Mostrar todos los usuarios
def mostrar_usuarios():
    if usuarios:
        for usuario in usuarios:
            print(usuario)
    else:
        print("No hay usuarios registrados.")




# Ingresar al sistema
def ingresar_sistema():
    username = input("Ingrese su username: ")
    password = input("Ingrese su password: ")


    for usuario in usuarios:
        if usuario.username == username and usuario.password == password:
            print(f"Acceso concedido. Bienvenido, {usuario.username}.")
            acceso_id = len(accesos) + 1
            nuevo_acceso = Acceso(acceso_id, usuario)
            accesos.append(nuevo_acceso)
            guardar_datos('accesos.ispc', accesos)
            return
    print("Credenciales incorrectas.")
    registrar_intento_fallido(username, password)




# Menú principal
def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar Usuario")
        print("2. Modificar Usuario")
        print("3. Eliminar Usuario")
        print("4. Buscar Usuario")
        print("5. Mostrar todos los Usuarios")
        print("6. Ingresar al Sistema")
        print("7. Salir")


        opcion = input("Seleccione una opción: ")


        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            modificar_usuario()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            buscar_usuario()
        elif opcion == "5":
            mostrar_usuarios()
        elif opcion == "6":
            ingresar_sistema()
        elif opcion == "7":
            print("Saliendo del programa.")
            guardar_datos('usuarios.ispc', usuarios)
            guardar_datos('accesos.ispc', accesos)
            break
        else:
            print("Opción no válida. Intente de nuevo.")




# Ejecutar el menú
if __name__ == "__main__":
    menu()





