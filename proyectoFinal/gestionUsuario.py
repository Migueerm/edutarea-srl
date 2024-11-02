# Definición de la Clase Usuario y Listas
import pickle


class Usuario:
    def __init__(self, id, username, dni, password, email):
        self.id = id
        self.username = username
        self.dni = dni
        self.password = password
        self.email = email


    # Getters
    def get_id(self):
        return self.id


    def get_username(self):
        return self.username


    def get_dni(self):
        return self.dni


    def get_password(self):
        return self.password


    def get_email(self):
        return self.email


    # Setters
    def set_id(self, id):
        self.id = id


    def set_username(self, username):
        self.username = username


    def set_dni(self, dni):
        if dni:
            self.dni = dni
        else:
            raise ValueError("DNI no puede ser vacío.")


    def set_password(self, password):
        self.password = password


    def set_email(self, email):
        self.email = email


    def get_usuario(self):
        return f"id: {self.id}, username: {self.username}, dni: {self.dni}, email: {self.email}"


usuarios = []


# Funciones CRUD con Ordenación Integrada


def agregar_usuario():
    id = int(input("Ingrese el ID del nuevo usuario: "))
    # Verificar si el ID o el email ya existen
    for u in usuarios:
        if u.id == id:
            print(f"No se puede agregar el usuario. El ID '{id}' ya existe.")
            return
    username = input("Ingrese el username: ")
    dni = int(input("Ingrese el DNI: "))
    password = input("Ingrese la contraseña: ")
    email = input("Ingrese el email: ")
    for u in usuarios:
        if u.email == email:
            print(f"No se puede agregar el usuario. El email '{email}' ya está en uso.")
            return
    nuevo_usuario = Usuario(id, username, dni, password, email)
    usuarios.append(nuevo_usuario)
    ordenar_usuarios_por_dni()  # Ordenar por DNI de mayor a menor después de agregar
    guardar_usuarios()
    print(f"Usuario '{username}' agregado y listado ordenado correctamente.")


def modificar_usuario():
    username = input("Ingrese el nombre de usuario a modificar: ")
    for user in usuarios:
        if user.username == username:
            nuevo_usuario = input("Nuevo nombre de Usuario: ")
            dni = int(input("Nuevo DNI: "))
            password = input("Nueva contraseña: ")
            email = input("Nuevo email: ")
            user.username = nuevo_usuario
            user.dni = dni
            user.password = password
            user.email = email
            ordenar_usuarios_por_dni()  # Ordenar por DNI de mayor a menor después de modificar
            guardar_usuarios()
            print(f"Usuario '{nuevo_usuario}' modificado y listado ordenado correctamente.")
            return
    print("Usuario no encontrado.")


def eliminar_usuario():
    usuario = input("Ingrese el nombre de usuario o email a eliminar: ")
    for user in usuarios:
        if user.username == usuario or user.email == usuario:
            usuarios.remove(user)
            ordenar_usuarios_por_dni()  # Ordenar por DNI de mayor a menor después de eliminar
            guardar_usuarios()
            print(f"Usuario '{usuario}' eliminado y listado ordenado correctamente.")
            return
    print("Usuario no encontrado.")


# Funciones de Búsqueda y Validación de Usuarios


def buscar_usuario(nombre_usuario):
    for usuario in usuarios:
        if usuario.username == nombre_usuario or usuario.email == nombre_usuario:
            metodo_busqueda = "búsqueda secuencial" if not esta_ordenado else "búsqueda binaria"
            print(f"ID: {usuario.id}, Username: {usuario.username}, Email: {usuario.email} (Realizado por técnica de {metodo_busqueda})")
            return
    print("Usuario no encontrado.")


def validar_usuario(username, password):
    for usuario in usuarios:
        if usuario.username == username and usuario.password == password:
            return True
    return False


def mostrar_usuarios(archivo=None):
    global usuarios
    if archivo:
        cargar_usuarios(archivo)  # Cargar usuarios desde el archivo especificado
    else:
        cargar_usuarios()  # Cargar usuarios desde el archivo por defecto

    # Mostrar la lista de usuarios
    for user in usuarios:
        print(f"Username: {user.get_username()}, DNI: {user.get_dni()}, Email: {user.get_email()}")



# Funciones de Guardado y Carga de Usuarios


def guardar_usuarios():
    with open('usuarios.ispc', 'wb') as file:
        pickle.dump(usuarios, file)
    print("Usuarios guardados en 'usuarios.ispc'.")


def guardar_usuarios_username():
    with open('usuariosOrdenadosPorUsername.ispc', 'wb') as file:
        pickle.dump(usuarios, file)
    print("Usuarios guardados en 'usuariosOrdenadosPorUsername.ispc'.")


def cargar_usuarios(archivo='usuarios.ispc'):
    global usuarios
    try:
        with open(archivo, 'rb') as file:
            usuarios = pickle.load(file)
        print(f"Usuarios cargados correctamente desde '{archivo}'.")
    except FileNotFoundError:
        usuarios = []
        print(f"Archivo '{archivo}' no encontrado. Se creará un nuevo archivo al guardar.")



# Función de Ordenamiento de Usuarios por DNI


# Ordenar usuarios por DNI de mayor a menor
def ordenar_usuarios_por_dni():
    usuarios.sort(key=lambda x: x.dni, reverse=True)
    print("Usuarios ordenados por DNI de mayor a menor.")


# Función para Insertar Usuarios Rápidamente y Variables Globales


# Variable global para controlar si los usuarios están ordenados
esta_ordenado = False


# Incorporar usuarios aleatorios automáticamente
def usuarios_aleatorios():
    usuarios_prueba = [
        {"id": 1, "username": "usuario1", "dni": 12345678, "password": "clave1", "email": "usuario1@example.com"},
        {"id": 2, "username": "usuario2", "dni": 87654321, "password": "clave2", "email": "usuario2@example.com"},
        # ... (otros usuarios de prueba) ...
        {"id": 20, "username": "usuario20", "dni": 10101010, "password": "clave20", "email": "usuario20@example.com"}
    ]
    for u in usuarios_prueba:
        if any(usuario.id == u["id"] or usuario.email == u["email"] for usuario in usuarios):
            print(f"El ID '{u['id']}' o el email '{u['email']}' ya existen. No se puede agregar el usuario.")
        else:
            nuevo_usuario = Usuario(u["id"], u["username"], u["dni"], u["password"], u["email"])
            usuarios.append(nuevo_usuario)
    ordenar_usuarios_por_dni()  # Ordenar por DNI de mayor a menor después de cargar usuarios aleatorios
    guardar_usuarios()


# Menú CRUD de Usuarios


def menu_crud_usuarios():
    while True:
        print("\n--- CRUD de Usuarios ---")
        print("1. Agregar un nuevo usuario")
        print("2. Modificar un usuario")
        print("3. Eliminar un usuario")
        print("4. Volver al Menú de Usuarios y Accesos")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_usuario()
        elif opcion == '2':
            modificar_usuario()
        elif opcion == '3':
            eliminar_usuario()
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente nuevamente.")


