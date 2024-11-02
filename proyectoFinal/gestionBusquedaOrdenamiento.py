import os
from datetime import datetime
import pickle
from gestionUsuario import mostrar_usuarios

# Rutas de archivos
USUARIOS_FILE = 'usuarios.ispc'
ORDENADOS_FILE = 'usuariosOrdenadosPorUsername.ispc'
BUSQUEDAS_FOLDER = 'búsquedasYordenamientos'

usuarios = []


# Función para cargar usuarios desde un archivo específico
def cargar_usuarios(archivo=USUARIOS_FILE):
    global usuarios
    try:
        with open(archivo, 'rb') as file:
            usuarios = pickle.load(file)
        print(f"Usuarios cargados correctamente desde {archivo}.")
    except FileNotFoundError:
        usuarios = []
        print(f"Archivo '{archivo}' no encontrado.")


# Verificar si la carpeta de búsquedas existe, de no ser así, crearla
if not os.path.exists(BUSQUEDAS_FOLDER):
    os.makedirs(BUSQUEDAS_FOLDER)


# Guardar usuarios en archivo ordenado
def guardar_usuarios(archivo=USUARIOS_FILE):
    with open(archivo, 'wb') as file:
        pickle.dump(usuarios, file)


# Función de ordenamiento por inserción (puedes cambiarla a burbuja, selección o quicksort)
def ordenamiento_insercion_usuarios():
    global usuarios
    cargar_usuarios()  # Asegúrate de que los usuarios estén cargados
    for i in range(1, len(usuarios)):
        key_user = usuarios[i]
        j = i - 1
        while j >= 0 and usuarios[j].get_username() > key_user.get_username():
            usuarios[j + 1] = usuarios[j]
            j -= 1
        usuarios[j + 1] = key_user
    guardar_usuarios(ORDENADOS_FILE)  # Guardar en archivo ordenado
    print("Usuarios ordenados por username y guardados correctamente en el archivo de ordenados.")


# Búsqueda secuencial
def busqueda_secuencial(campo, valor, nombre_campo=""):
    cargar_usuarios()  # Cargar usuarios desde archivo original
    intentos = 0
    print(f"Se utilizó la búsqueda por {nombre_campo} y la técnica fue la búsqueda secuencial.")
    
    for user in usuarios:
        intentos += 1
        if getattr(user, f'get_{campo}')() == valor:
            print(f"Usuario encontrado en {intentos} intentos. Datos: Username: {user.get_username()}, DNI: {user.get_dni()}, Email: {user.get_email()}")
            return user
        else:
            print(f"Intento {intentos}: {valor} es distinto a {getattr(user, f'get_{campo}')()}")
    
    print(f"Usuario con {nombre_campo} {valor} no encontrado después de {intentos} intentos.")
    return None



# Búsqueda binaria y generación de log para búsqueda por DNI
def busqueda_binaria_por_dni(dni):
    cargar_usuarios() 
    # Ordena los usuarios por DNI antes de hacer la búsqueda
    usuarios.sort(key=lambda x: x.get_dni())
    dnies = [user.get_dni() for user in usuarios]
    
    log_filename = f'buscandoUsuarioPorDNI-{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
    with open(os.path.join(BUSQUEDAS_FOLDER, log_filename), 'w') as log_file:
        print("Se utilizó la búsqueda por DNI y la técnica fue la búsqueda binaria.")
        log_file.write("Usando búsqueda binaria por DNI.\n")
        
        if dni < dnies[0]:
            print("DNI buscado es más chico que el más chico de los registrados.")
            log_file.write(f"DNI buscado {dni} es más chico que el menor registrado {dnies[0]}. No se buscará.\n")
            return
        elif dni > dnies[-1]:
            print("DNI buscado es más grande que el más grande de los registrados.")
            log_file.write(f"DNI buscado {dni} es más grande que el mayor registrado {dnies[-1]}. No se buscará.\n")
            return

        inicio, fin = 0, len(dnies) - 1
        intentos = 0
        encontrado = False

        while inicio <= fin:
            intentos += 1
            mid = (inicio + fin) // 2
            log_file.write(f"Intento {intentos}: Comparando con DNI en posición {mid}: {dnies[mid]}\n")

            if dnies[mid] == dni:
                encontrado = True
                usuario_encontrado = usuarios[mid]
                print(f"Usuario encontrado en {intentos} intentos. Datos: Username: {usuario_encontrado.get_username()}, DNI: {usuario_encontrado.get_dni()}, Email: {usuario_encontrado.get_email()}")
                log_file.write(f"Usuario encontrado: {usuario_encontrado.get_username()}, DNI: {usuario_encontrado.get_dni()}, Email: {usuario_encontrado.get_email()}\n")
                return usuario_encontrado
            elif dnies[mid] < dni:
                inicio = mid + 1
                log_file.write("Buscando en la parte derecha.\n")
            else:
                fin = mid - 1
                log_file.write("Buscando en la parte izquierda.\n")

        if not encontrado:
            print(f"No se encontró el DNI {dni} después de {intentos} intentos.")
            log_file.write(f"No se encontró el DNI {dni} después de {intentos} intentos.\n")




# Búsqueda binaria por username
def busqueda_binaria_username(username):
    cargar_usuarios(ORDENADOS_FILE) 
    usernames = [user.get_username() for user in usuarios]  
    if not usernames: 
        print("No hay usuarios en la lista.")
        return None

    inicio, fin = 0, len(usernames) - 1
    intentos = 0

    log_filename = f'buscandoUsuarioPorUsername-{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
    with open(os.path.join(BUSQUEDAS_FOLDER, log_filename), 'w') as log_file:
        while inicio <= fin:
            intentos += 1
            mid = (inicio + fin) // 2
            log_file.write(f"Intento {intentos}: Comparando con username en posición {mid}: {usernames[mid]}\n")

            if usernames[mid] == username:
                usuario_encontrado = usuarios[mid]
                print(f"Usuario encontrado en {intentos} intentos. Datos: Username: {usuario_encontrado.get_username()}, DNI: {usuario_encontrado.get_dni()}, Email: {usuario_encontrado.get_email()}")
                log_file.write(f"Usuario encontrado: {usuario_encontrado.get_username()}, DNI: {usuario_encontrado.get_dni()}, Email: {usuario_encontrado.get_email()}\n")
                return usuario_encontrado
            elif usernames[mid] < username:
                inicio = mid + 1
                log_file.write("Buscando en la parte derecha.\n")
            else:
                fin = mid - 1
                log_file.write("Buscando en la parte izquierda.\n")

        print(f"No se encontró el username '{username}' después de {intentos} intentos.")
        log_file.write(f"No se encontró el username '{username}' después de {intentos} intentos.\n")
        return None

# Buscar usuario por username, decide si usar secuencial o binaria
def buscar_usuario_por_username(username):
    if not os.path.exists(ORDENADOS_FILE):  # Ordena y guarda si el archivo ordenado no existe
        print("Archivo ordenado no encontrado. Ordenando usuarios y creando archivo.")
        ordenamiento_insercion_usuarios()
    else:
        cargar_usuarios(ORDENADOS_FILE)  # Cargar el archivo ordenado antes de la búsqueda
    print("Usando búsqueda binaria por username.")
    return busqueda_binaria_username(username)



# Función principal de gestión
def gestionar_busqueda_y_ordenamiento():
    while True:
        print("\n--- Ordenamiento y Búsqueda de Usuarios ---")
        print("1. Ordenar usuarios por username (Inserción)")
        print("2. Buscar usuario por DNI")
        print("3. Buscar usuario por Username")
        print("4. Buscar usuario por Email")
        print("5. Mostrar todos los usuarios (archivo original)")
        print("6. Mostrar usuarios ordenados por Username (si existe)")
        print("7. Volver al menú anterior")

        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            ordenamiento_insercion_usuarios()
        elif opcion == '2':
            dni = input("Ingrese el DNI del usuario a buscar: ")
            busqueda_binaria_por_dni(int(dni))
        elif opcion == '3':
            username = input("Ingrese el username del usuario a buscar: ")
            buscar_usuario_por_username(username)
        elif opcion == '4':
            email = input("Ingrese el email del usuario a buscar: ")
            busqueda_secuencial("email", email, "Email")
        elif opcion == '5':
            mostrar_usuarios()
        elif opcion == '6':
            mostrar_usuarios(ORDENADOS_FILE)
        elif opcion == '7':
            break
