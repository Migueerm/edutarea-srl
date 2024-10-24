import csv
import random
import os
from datetime import datetime
import matplotlib
matplotlib.use('Qt5Agg')  # Establecer el motor de visualización
import matplotlib.pyplot as plt

# Crear una lista de listas para registros pluviales
def generar_registros_pluviales():
    registros = [[random.randint(0, 100) for _ in range(31)] for _ in range(12)]
    return registros

# Guardar registros pluviales en un archivo CSV
def guardar_registros_pluviales(registros, anio):
    nombre_archivo = f'registroPluvial{anio}.csv'
    with open(nombre_archivo, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Mes", "Día", "Lluvias (mm)"])
        for mes, dias in enumerate(registros, start=1):
            for dia, lluvia in enumerate(dias, start=1):
                writer.writerow([mes, dia, lluvia])
    print(f'Registros pluviales guardados en {nombre_archivo}')

# Cargar registros pluviales desde un archivo CSV
def cargar_registros_pluviales(anio):
    nombre_archivo = f'registroPluvial{anio}.csv'
    if not os.path.exists(nombre_archivo):
        registros = generar_registros_pluviales()
        guardar_registros_pluviales(registros, anio)
    else:
        registros = []
        with open(nombre_archivo, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar encabezado
            for row in reader:
                mes, dia, lluvia = int(row[0]), int(row[1]), int(row[2])
                while len(registros) < mes:
                    registros.append([])
                while len(registros[mes-1]) < dia:
                    registros[mes-1].append(0)
                registros[mes-1][dia-1] = lluvia
            print(f'Registros pluviales cargados desde {nombre_archivo}')
    return registros

# Mostrar registros pluviales de un mes específico
def mostrar_registros_del_mes(registros, mes):
    if 1 <= mes <= 12:
        print(f'Registros pluviales del mes {mes}:')
        for dia, lluvia in enumerate(registros[mes-1], start=1):
            print(f'Día {dia}: {lluvia} mm')
    else:
        print('Mes inválido. Por favor, ingrese un valor entre 1 y 12.')

# Graficar datos pluviales
def graficar_datos_pluviales(registros):
    # Gráfico de barras de lluvias anuales
    lluvias_totales = [sum(mes) for mes in registros]
    plt.bar(range(1, 13), lluvias_totales)
    plt.xlabel('Mes')
    plt.ylabel('Lluvias (mm)')
    plt.title('Lluvias Anuales')
    plt.show(block=True)

    # Gráfico de dispersión
    for mes, dias in enumerate(registros, start=1):
        x = [mes] * len(dias)
        y = list(range(1, len(dias) + 1))
        plt.scatter(x, y, s=dias)
    plt.xlabel('Mes')
    plt.ylabel('Día')
    plt.title('Dispersión de Lluvias')
    plt.show(block=True)

    # Gráfico circular
    plt.pie(lluvias_totales, labels=range(1, 13), autopct='%1.1f%%')
    plt.title('Distribución de Lluvias por Mes')
    plt.show(block=True)
