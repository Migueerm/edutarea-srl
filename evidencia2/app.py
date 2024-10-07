import mysql.connector
from datetime import datetime


# db_config.py
#usar para conectar a la base de datos. La contraseña y database debe ser reemplazadas por la propia :)
def conectar_base_datos():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="CONTRASEÑA",
            database="evidencia2"
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos.")
            return conexion
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
        
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



# Funciones para interactuar con la base de datos

def agregar_usuario_db(usuario):
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO usuario (username, password, email) VALUES (%s, %s, %s)"
            valores = (usuario.username, usuario.password, usuario.email)
            cursor.execute(sql, valores)
            conexion.commit()
            print("Usuario agregado exitosamente en la base de datos.")
        except mysql.connector.Error as err:
            print(f"Error al insertar usuario: {err}")
        finally:
            cursor.close()
            conexion.close()


def modificar_usuario_db(username, nuevo_email, nuevo_password):
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "UPDATE usuario SET email = %s, password = %s WHERE username = %s"
            valores = (nuevo_email, nuevo_password, username)
            cursor.execute(sql, valores)
            conexion.commit()
            print("Usuario modificado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al modificar usuario: {err}")
        finally:
            cursor.close()
            conexion.close()
#FLOR
def buscar_usuario_db(username):
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "SELECT id_usuario, username, email FROM usuario WHERE username = %s OR email = %s"
            cursor.execute(sql, (username, username))
            resultado = cursor.fetchone()
            if resultado:
                usuario = Usuario(*resultado)
                print(usuario)
            else:
                print("Usuario no encontrado.")
        except mysql.connector.Error as err:
            print(f"Error al buscar usuario: {err}")
        finally:
            cursor.close()
            conexion.close()




def mostrar_usuarios_db():
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "SELECT id_usuario, username, password, email FROM usuario"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            if resultados:
                for resultado in resultados:
                    usuario = Usuario(*resultado)
                    print(usuario)
            else:
                print("No hay usuarios registrados.")
        except mysql.connector.Error as err:
            print(f"Error al mostrar usuarios: {err}")
        finally:
            cursor.close()
            conexion.close()




def registrar_acceso_db(usuario):
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO acceso (fecha_ingreso, usuario_logueado) VALUES (%s, %s)"
            fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            valores = (fecha_ingreso, usuario.username)
            cursor.execute(sql, valores)
            conexion.commit()
            print(f"Acceso registrado para el usuario {usuario.username}.")
        except mysql.connector.Error as err:
            print(f"Error al registrar acceso: {err}")
        finally:
            cursor.close()
            conexion.close()




def registrar_intento_fallido(username, password):
    with open('logs.txt', 'a') as log_file:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{fecha} - Intento fallido con Username: {username}, Password: {password}\n")


def eliminar_usuario_db(username):
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "DELETE FROM usuario WHERE username = %s"
            cursor.execute(sql, (username,))
            conexion.commit()
            print("Usuario eliminado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al eliminar usuario: {err}")
        finally:
            cursor.close()
            conexion.close()


def buscar_usuario_db(username):
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "SELECT id_usuario, username, email FROM usuario WHERE username = %s OR email = %s"
            cursor.execute(sql, (username, username))
            resultado = cursor.fetchone()
            if resultado:
                usuario = Usuario(*resultado)
                print(usuario)
            else:
                print("Usuario no encontrado.")
        except mysql.connector.Error as err:
            print(f"Error al buscar usuario: {err}")
        finally:
            cursor.close()
            conexion.close()


def mostrar_usuarios_db():
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id_usuario, username, email FROM usuario")
            resultados = cursor.fetchall()
            if resultados:
                for resultado in resultados:
                    usuario = Usuario(*resultado)
                    print(usuario)
            else:
                print("No hay usuarios registrados.")
        except mysql.connector.Error as err:
            print(f"Error al mostrar usuarios: {err}")
        finally:
            cursor.close()
            conexion.close()


def registrar_acceso_db(usuario):
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO acceso (fecha_ingreso, usuario_logueado) VALUES (%s, %s)"
            fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            valores = (fecha_ingreso, usuario.username)
            cursor.execute(sql, valores)
            conexion.commit()
            print(f"Acceso registrado para el usuario {usuario.username}.")
        except mysql.connector.Error as err:
            print(f"Error al registrar acceso: {err}")
        finally:
            cursor.close()
            conexion.close()


def registrar_intento_fallido(username, password):
    with open('logs.txt', 'a') as log_file:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{fecha} - Intento fallido con Username: {username}, Password: {password}\n")


# Funciones del menú
def agregar_usuario():
    username = input("Ingrese username: ")
    email = input("Ingrese email: ")
    password = input("Ingrese password: ")
    nuevo_usuario = Usuario(None, username, password, email)
    agregar_usuario_db(nuevo_usuario)


def modificar_usuario():
    username = input("Ingrese el username del usuario a modificar: ")
    nuevo_email = input("Nuevo email: ")
    nuevo_password = input("Nuevo password: ")
    modificar_usuario_db(username, nuevo_email, nuevo_password)


def eliminar_usuario():
    username = input("Ingrese el username del usuario a eliminar: ")
    eliminar_usuario_db(username)


def buscar_usuario():
    username = input("Ingrese username o email a buscar: ")
    buscar_usuario_db(username)


def mostrar_usuarios():
    mostrar_usuarios_db()


def ingresar_sistema():
    username = input("Ingrese su username: ")
    password = input("Ingrese su password: ")

    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "SELECT id_usuario, username, password FROM usuario WHERE username = %s AND password = %s"
            cursor.execute(sql, (username, password))
            resultado = cursor.fetchone()

            if resultado:
                usuario = Usuario(*resultado)
                print(f"Acceso concedido. Bienvenido, {usuario.username}.")
                registrar_acceso_db(usuario)
            else:
                print("Credenciales incorrectas.")
                registrar_intento_fallido(username, password)
        except mysql.connector.Error as err:
            print(f"Error al ingresar: {err}")
        finally:
            cursor.close()
            conexion.close()


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
            break
        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecutar el menú
if __name__ == "__main__":
    menu()

# Funciones del menú
def agregar_usuario():
    username = input("Ingrese username: ")
    email = input("Ingrese email: ")
    password = input("Ingrese password: ")
    nuevo_usuario = Usuario(None, username, password, email)
    agregar_usuario_db(nuevo_usuario)




def modificar_usuario():
    username = input("Ingrese el username del usuario a modificar: ")
    nuevo_email = input("Nuevo email: ")
    nuevo_password = input("Nuevo password: ")
    modificar_usuario_db(username, nuevo_email, nuevo_password)




def eliminar_usuario():
    username = input("Ingrese el username del usuario a eliminar: ")
    eliminar_usuario_db(username)




def buscar_usuario():
    username = input("Ingrese username o email a buscar: ")
    buscar_usuario_db(username)




def mostrar_usuarios():
    mostrar_usuarios_db()




def ingresar_sistema():
    username = input("Ingrese su username: ")
    password = input("Ingrese su password: ")


    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "SELECT id_usuario, username, password FROM usuario WHERE username = %s AND password = %s"
            cursor.execute(sql, (username, password))
            resultado = cursor.fetchone()


            if resultado:
                usuario = Usuario(*resultado)
                print(f"Acceso concedido. Bienvenido, {usuario.username}.")
                registrar_acceso_db(usuario)
            else:
                print("Credenciales incorrectas.")
                registrar_intento_fallido(username, password)
        except mysql.connector.Error as err:
            print(f"Error al ingresar: {err}")
        finally:
            cursor.close()
            conexion.close()




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
            break
        else:
            print("Opción no válida. Intente de nuevo.")




# Ejecutar el menú
if __name__ == "__main__":
    menu()




