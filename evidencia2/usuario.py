import pickle

class Usuario:
    def __init__(self, id, usuario, clave, email):
        self.id = id
        self.usuario = usuario
        self.clave = clave
        self.email = email

usuarios = []

def agregar_usuario(id, usuario, clave, email):
    nuevo_usuario = Usuario(id, usuario, clave, email)
    usuarios.append(nuevo_usuario)
    guardar_usuarios()
    print(f"Usuario '{usuario}' agregado correctamente.")  # Mensaje de confirmación

def modificar_usuario(nombre_usuario, nuevo_usuario, nueva_clave, nuevo_email):
    for usuario in usuarios:
        if usuario.usuario == nombre_usuario:
            usuario.usuario = nuevo_usuario
            usuario.clave = nueva_clave
            usuario.email = nuevo_email
            guardar_usuarios()
            print(f"Usuario '{nombre_usuario}' modificado correctamente.")
            return
    print("Usuario no encontrado.")

def eliminar_usuario(nombre_usuario):
    for usuario in usuarios:
        if usuario.usuario == nombre_usuario or usuario.email == nombre_usuario:
            usuarios.remove(usuario)
            guardar_usuarios()
            print(f"Usuario '{nombre_usuario}' eliminado correctamente.")
            return
    print("Usuario no encontrado.")

def buscar_usuario(nombre_usuario):
    for usuario in usuarios:
        if usuario.usuario == nombre_usuario or usuario.email == nombre_usuario:
            print(f"ID: {usuario.id}, Username: {usuario.usuario}, Email: {usuario.email}")
            return
    print("Usuario no encontrado.")

def validar_usuario(nombre_usuario, clave_usuario):
    for usuario in usuarios:
        if usuario.usuario == nombre_usuario and usuario.clave == clave_usuario:
            return True
    return False

def mostrar_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
    for usuario in usuarios:
        print(f"ID: {usuario.id}, Username: {usuario.usuario}, Email: {usuario.email}")

def guardar_usuarios():
    with open('usuarios.ispc', 'wb') as file:
        pickle.dump(usuarios, file)
    print("Usuarios guardados en 'usuarios.ispc'.")

def cargar_usuarios():
    global usuarios
    try:
        with open('usuarios.ispc', 'rb') as file:
            usuarios = pickle.load(file)
        print("Usuarios cargados correctamente.")
    except FileNotFoundError:
        usuarios = []
        print("Archivo 'usuarios.ispc' no encontrado. Se creará un nuevo archivo al guardar.")
