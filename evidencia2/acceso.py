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



