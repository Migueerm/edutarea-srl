import mysql.connector
from mysql.connector import Error

# Función para conectar a la base de datos
def conectar_base_datos():
    try:
        conexion = mysql.connector.connect(
            user='root',
            password='Aasx76tcy_2791',
            host='127.0.0.1',
            port=3306,
            database='edutareas'
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos.")
            return conexion
    except Error as e:
        print(f"Error en la conexión a la base de datos: {e}")
        return None

# Funciones de consulta (JOIN) con manejo de excepciones
def consultar_inner_join():
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = """
            SELECT *
            FROM materia A
            INNER JOIN profesor B
            ON A.ID_Profesor = B.ID_Profesor
            """
            cursor.execute(query)
            resultados = cursor.fetchall()
            print("Resultado INNER JOIN entre materia y profesor:")
            for fila in resultados:
                print(fila)
        except Error as e:
            print(f"Error al ejecutar la consulta INNER JOIN: {e}")
        finally:
            cursor.close()
            conexion.close()

def consulta_left_join():
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = """
            SELECT *
            FROM inscripcion C
            LEFT JOIN estudiante D
            ON C.ID_Estudiante = D.ID_Estudiante
            """
            cursor.execute(query)
            resultados = cursor.fetchall()
            print("Resultado LEFT JOIN entre inscripcion y estudiante:")
            for fila in resultados:
                print(fila)
        except Error as e:
            print(f"Error al ejecutar la consulta LEFT JOIN: {e}")
        finally:
            cursor.close()
            conexion.close()

def consulta_right_join():
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = """
            SELECT *
            FROM curso_profesor E
            RIGHT JOIN profesor B
            ON E.ID_Profesor = B.ID_Profesor
            """
            cursor.execute(query)
            resultados = cursor.fetchall()
            print("Resultado RIGHT JOIN entre curso_profesor y profesor:")
            for fila in resultados:
                print(fila)
        except Error as e:
            print(f"Error al ejecutar la consulta RIGHT JOIN: {e}")
        finally:
            cursor.close()
            conexion.close()

def consulta_full_join():
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = """
            SELECT *
            FROM usuario F
            LEFT JOIN usuario_logueado G ON F.id_usuario = G.id_usuario
            UNION
            SELECT *
            FROM usuario F
            RIGHT JOIN usuario_logueado G ON F.id_usuario = G.id_usuario
            """
            cursor.execute(query)
            resultados = cursor.fetchall()
            print("Resultado FULL JOIN entre usuario y usuario_logueado (simulado):")
            for fila in resultados:
                print(fila)
        except Error as e:
            print(f"Error al ejecutar la consulta FULL JOIN: {e}")
        finally:
            cursor.close()
            conexion.close()

# Función de gestión de base de datos con un menú claro y completo
def gestionar_base_datos():
    while True:
        print("\n--- Gestión de Base de Datos ---")
        print("1. INNER JOIN entre materia y profesor")
        print("2. LEFT JOIN entre inscripcion y estudiante")
        print("3. RIGHT JOIN entre curso_profesor y profesor")
        print("4. FULL JOIN entre usuario y usuario_logueado")
        print("5. Volver al Menú Principal")
        option = input("Seleccione una opción: ")
        if option == '1':
            consultar_inner_join()
        elif option == '2':
            consulta_left_join()
        elif option == '3':
            consulta_right_join()
        elif option == '4':
            consulta_full_join()
        elif option == '5':
            print("Volviendo al Menú Principal...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
