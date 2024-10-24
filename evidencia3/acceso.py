import pickle
from datetime import datetime
import os
from usuario import validar_usuario

class Acceso:
    def __init__(self, id, fechaIngreso, fechaSalida, usuarioLogueado):
        self.id = id
        self.fechaIngreso = fechaIngreso
        self.fechaSalida = fechaSalida
        self.usuarioLogueado = usuarioLogueado

    def __str__(self):
        return f"ID: {self.id}, Usuario: {self.usuarioLogueado}, Fecha de Ingreso: {self.fechaIngreso}, Fecha de Salida: {self.fechaSalida}"

accesos = []

def registrar_acceso(username, password):
    if validar_usuario(username, password):
        id = len(accesos) + 1
        fechaIngreso = datetime.now()
        acceso = Acceso(id, fechaIngreso, None, username)
        accesos.append(acceso)
        guardar_accesos()
        print(f"Acceso registrado para el usuario '{username}' el {fechaIngreso}.")
        print("Acceso concedido.")
    else:
        registrar_intento_fallido(username, password)
        print("Usuario no encontrado. Acceso denegado.")

def registrar_intento_fallido(username, password):
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.now()} - Intento fallido: {username}, Contraseña: {password}\n")

def guardar_accesos():
    ruta_archivo = 'accesos.ispc'
    try:
        with open(ruta_archivo, 'wb') as file:
            pickle.dump(accesos, file)
        print(f"Accesos guardados correctamente en {os.path.abspath(ruta_archivo)}.")
    except Exception as e:
        print(f"Error al guardar accesos: {str(e)}")

def cargar_accesos():
    global accesos
    ruta_archivo = 'accesos.ispc'
    try:
        with open(ruta_archivo, 'rb') as file:
            accesos = pickle.load(file)
        print("Accesos cargados correctamente.")
    except FileNotFoundError:
        accesos = []
        print(f"Archivo '{ruta_archivo}' no encontrado. Se creará un nuevo archivo al guardar.")

# Funciones adicionales para ordenamiento y búsqueda
def ordenar_accesos_burbuja():
    n = len(accesos)
    for i in range(n):
        for j in range(0, n-i-1):
            if accesos[j].usuarioLogueado > accesos[j+1].usuarioLogueado:
                accesos[j], accesos[j+1] = accesos[j+1], accesos[j]
    guardar_accesos()
    print("Accesos ordenados por burbuja y guardados correctamente.")

def ordenar_accesos_python():
    accesos.sort(key=lambda x: x.usuarioLogueado)
    guardar_accesos()
    print("Accesos ordenados por método sort() de Python y guardados correctamente.")
