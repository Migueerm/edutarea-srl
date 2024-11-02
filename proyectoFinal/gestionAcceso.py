import pickle
from datetime import datetime
import os
from gestionUsuario import validar_usuario
from gestionarBaseDatos import gestionar_base_datos

class Acceso:
    def __init__(self, id, fechaIngreso, fechaSalida, usuarioLogueado):
        self.id = id
        self.fechaIngreso = fechaIngreso
        self.fechaSalida = fechaSalida
        self.usuarioLogueado = usuarioLogueado

    # Getters
    def get_id(self):
        return self.id
    def get_fecha_ingreso(self):
        return self.fechaIngreso
    def get_fecha_salida(self):
        return self.fechaSalida
    def get_usuario_logueado(self):
        return self.usuarioLogueado

    # Setters
    def set_id(self, id):
        self.id = id
    def set_fecha_ingreso(self, fechaIngreso):
        self.fechaIngreso = fechaIngreso
    def set_fecha_salida(self, fechaSalida):
        self.fechaSalida = fechaSalida
    def set_usuario_logueado(self, usuarioLogueado):
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
        submenu_gestion_usuario()  # Llama al submenú de gestión después de iniciar sesión
    else:
        registrar_intento_fallido(username, password)
        print("Usuario no encontrado. Acceso denegado.")

def submenu_gestion_usuario():
    while True:
        print("\n--- Gestión del Sistema ---")
        print("1. Ir a la Gestión de Base de Datos")
        print("2. Volver al Menú Principal")
        print("3. Salir de la Aplicación")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            gestionar_base_datos()
        elif opcion == '2':
            return  # Vuelve al menú principal
        elif opcion == '3':
            print("Saliendo de la aplicación...")
            exit()
        else:
            print("Opción no válida. Intente nuevamente.")

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

def mostrar_accesos():
    for acceso in accesos:
        print(f"ID: {acceso.id}, Usuario: {acceso.usuarioLogueado}, Fecha de Ingreso: {acceso.fechaIngreso}, Fecha de Salida: {acceso.fechaSalida}")

def menu_accesos():
    while True:
        print("\n--- Accesos de la Aplicación ---")
        print("a. Mostrar los Accesos")
        print("b. Mostrar los logs de intentos fallidos")
        print("c. Volver al Menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == 'a':
            mostrar_accesos()
        elif opcion == 'b':
            try:
                with open('logs.txt', 'r') as f:
                    print("\n--- Logs de Intentos Fallidos ---")
                    logs = f.readlines()
                    for log in logs:
                        print(log.strip())
            except FileNotFoundError:
                print("No se encontró el archivo de logs.")
        elif opcion == 'c':
            break
        else:
            print("Opción no válida. Intente de nuevo.")
