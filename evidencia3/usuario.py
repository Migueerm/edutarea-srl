import pickle

class Usuario:
    def __init__(self, id, usuario, clave, email):
        self.id = id
        self.usuario = usuario
        self.clave = clave
        self.email = email

usuarios = []

def agregar_usuario(id, usuario, clave, email):
    # Verificar si el ID ya existe
    for u in usuarios:
        if u.id == id:
            print(f"No se puede agregar el usuario. El ID '{id}' ya existe.")
            return
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
            metodo_busqueda = "búsqueda secuencial" if not esta_ordenado else "búsqueda binaria"
            print(f"ID: {usuario.id}, Username: {usuario.usuario}, Email: {usuario.email} (Realizado por técnica de {metodo_busqueda})")
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

# Método de ordenamiento por burbuja
def ordenar_usuarios_burbuja():
    n = len(usuarios)
    for i in range(n):
        for j in range(0, n-i-1):
            if usuarios[j].usuario > usuarios[j+1].usuario:
                usuarios[j], usuarios[j+1] = usuarios[j+1], usuarios[j]
    global esta_ordenado
    esta_ordenado = True
    guardar_usuarios()
    print("Usuarios ordenados por burbuja y guardados correctamente.")

# Método para ordenar utilizando sort() de Python
def ordenar_usuarios_python():
    usuarios.sort(key=lambda x: x.usuario)
    global esta_ordenado
    esta_ordenado = True
    guardar_usuarios()
    print("Usuarios ordenados por método sort() de Python y guardados correctamente.")

# Variable global para controlar si los usuarios están ordenados
esta_ordenado = False

# Función para insertar usuarios rápidamente esta se elimina luego de la prueba, va a dar error al ejecutar por primera vez el codigo 
def usuarios_aleatorios() :
    usuarios_prueba = [
        {"id": 1, "usuario": "usuario1", "clave": "clave1", "email": "usuario1@example.com"},
        {"id": 2, "usuario": "usuario2", "clave": "clave2", "email": "usuario2@example.com"},
        {"id": 3, "usuario": "usuario3", "clave": "clave3", "email": "usuario3@example.com"},
        {"id": 4, "usuario": "usuario4", "clave": "clave4", "email": "usuario4@example.com"},
        {"id": 5, "usuario": "usuario5", "clave": "clave5", "email": "usuario5@example.com"},
        {"id": 6, "usuario": "usuario6", "clave": "clave6", "email": "usuario6@example.com"},
        {"id": 7, "usuario": "usuario7", "clave": "clave7", "email": "usuario7@example.com"},
        {"id": 8, "usuario": "usuario8", "clave": "clave8", "email": "usuario8@example.com"},
        {"id": 9, "usuario": "usuario9", "clave": "clave9", "email": "usuario9@example.com"},
        {"id": 10, "usuario": "usuario10", "clave": "clave10", "email": "usuario10@example.com"},
        {"id": 11, "usuario": "usuario11", "clave": "clave11", "email": "usuario11@example.com"},
        {"id": 12, "usuario": "usuario12", "clave": "clave12", "email": "usuario12@example.com"},
        {"id": 13, "usuario": "usuario13", "clave": "clave13", "email": "usuario13@example.com"},
        {"id": 14, "usuario": "usuario14", "clave": "clave14", "email": "usuario14@example.com"},
        {"id": 15, "usuario": "usuario15", "clave": "clave15", "email": "usuario15@example.com"}
    ]
    for u in usuarios_prueba:
        agregar_usuario(u["id"], u["usuario"], u["clave"], u["email"])
