import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def generar_datos_pluviales(anno):
    """
    Genera datos de lluvias aleatorios para cada día del año y los guarda en un archivo CSV.
    Cada registro incluye mes, día y cantidad de lluvia en mm.
    """
    np.random.seed(42)
    meses_dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


    datos = []
    for mes in range(1, 13):
        dias = meses_dias[mes - 1]
        for dia in range(1, dias + 1):
            lluvia = round(np.random.uniform(0, 100), 2)
            datos.append([mes, dia, lluvia])
   
    df_precipitaciones = pd.DataFrame(datos, columns=['Mes', 'Dia', 'Lluvia (mm)'])
    os.makedirs('data', exist_ok=True)
    df_precipitaciones.to_csv(f'data/registroPluvial{anno}.csv', index=False)
    print(f"Datos pluviales generados y guardados en registroPluvial{anno}.csv.")


def cargar_datos_pluviales(anno):
    """
    Carga los datos pluviales desde el archivo CSV en un DataFrame.
    Si el archivo no existe, se generan nuevos datos automáticamente.
    """
    path = f'data/registroPluvial{anno}.csv'
    if not os.path.exists(path):
        print("Archivo no encontrado. Generando datos aleatorios...")
        generar_datos_pluviales(anno)
    return pd.read_csv(path)


def analizar_datos_anuales(df):
    """
    Muestra la precipitación máxima, mínima y promedio de lluvia en el año.
    Genera gráficos de barras, dispersión y circular.
    """
    max_lluvia = df['Lluvia (mm)'].max()
    min_lluvia = df['Lluvia (mm)'].min()
    mean_lluvia = df['Lluvia (mm)'].mean()
    print(f"Precipitación Máxima: {max_lluvia} mm")
    print(f"Precipitación Mínima: {min_lluvia} mm")
    print(f"Precipitación Promedio: {mean_lluvia:.2f} mm")


    # Ruta para guardar gráficos
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datosAnalizados')
    os.makedirs(path, exist_ok=True)


    # Gráficos anuales
    df.groupby('Mes')['Lluvia (mm)'].sum().plot(kind='bar', color='skyblue')
    plt.title('Precipitación Anual por Mes')
    plt.xlabel('Mes')
    plt.ylabel('Lluvia (mm)')
    plt.savefig(f'{path}/precipitacion_anual_barras.png')
    plt.show()


    # Gráfico de dispersión
    fig, ax = plt.subplots(figsize=(12, 6))
    for mes in range(1, 13):
        dias = df[df['Mes'] == mes]['Dia']
        ax.scatter(dias, df[df['Mes'] == mes]['Lluvia (mm)'], label=f'Mes {mes}', alpha=0.5)
    ax.set_title('Dispersión de Lluvias Anuales')
    ax.set_xlabel('Día del Mes')
    ax.set_ylabel('Lluvia (mm)')
    ax.legend(title='Mes')
    plt.savefig(f'{path}/precipitacion_anual_dispersión.png')
    plt.show()


    df.groupby('Mes')['Lluvia (mm)'].sum().plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('Distribución Mensual de Precipitaciones')
    plt.ylabel('')
    plt.savefig(f'{path}/precipitacion_anual_circular.png')    
    plt.show()
   


def analizar_datos_mensuales(df, mes):
    """
    Genera gráficos de barras, dispersión y circular para el mes especificado,
    respetando el número de días del mes correspondiente.
    """
    registros_mes = df[df['Mes'] == mes].set_index('Dia')['Lluvia (mm)']
    max_lluvia = registros_mes.max()
    min_lluvia = registros_mes.min()
    mean_lluvia = registros_mes.mean()
    print(f"Datos del mes {mes}:")
    print(registros_mes)
    print(f"Precipitación Máxima: {max_lluvia} mm")
    print(f"Precipitación Mínima: {min_lluvia} mm")
    print(f"Precipitación Promedio: {mean_lluvia:.2f} mm")


    # Ruta para gráficos específicos del mes
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datosAnalizados')
    os.makedirs(path, exist_ok=True)


    # Graficar de acuerdo con el número de días en el mes
    registros_mes.plot(kind='bar', color='skyblue')
    plt.title(f'Precipitación Diaria en el Mes {mes}')
    plt.xlabel('Día')
    plt.ylabel('Lluvia (mm)')
    plt.savefig(f'{path}/precipitacion_mes_{mes}_barras.png')
    plt.show()


    plt.scatter(registros_mes.index, registros_mes, alpha=0.5)
    plt.title(f'Dispersión de Lluvias en el Mes {mes}')
    plt.xlabel('Día')
    plt.ylabel('Lluvia (mm)')
    plt.savefig(f'{path}/precipitacion_mes_{mes}_dispersión.png')
    plt.show()


    registros_mes.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title(f'Distribución de Precipitaciones en el Mes {mes}')
    plt.ylabel('')
    plt.savefig(f'{path}/precipitacion_mes_{mes}_circular.png')
    plt.show()




def menu_analisis_datos_pluviales():
    anno = input("Ingrese el año para analizar los registros pluviales: ")
    df = cargar_datos_pluviales(anno)
    while True:
        print("\n--- Menú de Análisis de Datos Pluviales ---")
        print("1. Resumen de precipitaciones anuales")
        print("2. Analizar un mes específico")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
       
        if opcion == '1':
            analizar_datos_anuales(df)
        elif opcion == '2':
            mes = int(input("Ingrese el número del mes a analizar (1 para Enero, 2 para Febrero, etc.): "))
            if 1 <= mes <= 12:
                analizar_datos_mensuales(df, mes)
            else:
                print("Mes no válido. Intente nuevamente.")
        elif opcion == '3':
            print("Saliendo del análisis de datos pluviales...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu_analisis_datos_pluviales()
