# EduTarea SRL

**Integrantes**

| Nombre y  Apellido  |    DNI    | Correo eléctronico        | Link Git Hub |
|---------------------|-----------|---------------------------|--------------
| Melania Ligorria    | 38412646  | melanialigorria@gmail.com | https://github.com/mel-ligorria
| Miguel Rojas        | 39215582  | rojas.miguel018@gmail.com | https://github.com/Migueerm/ejercitacion-ispc
| Florencia Andrada   | 44788525  | florenciacarolina031@gmail.com | https://github.com/Flor3ncia-Andr4d4
| Carlota Olmedo      | 41711170  | carlota_olmedo@hotmail.com| https://github.com/caolmedo
| Guadalupe Mendoza   | 45934026  | despontinguadalupe@gmail.com |https://github.com/Guadamendoza/SolucionesPracticas 

**Acceso al documento**: https://docs.google.com/document/d/1Fw-lIJrUs7D48Jj7ESrykbT-LgaB_OP8/edit?usp=sharing&ouid=105815117545153336322&rtpof=true&sd=true 

**Descripción del repositorio**

El repositorio de EduTarea SRL contiene una carpeta con el nombre “Evidencia1” donde se encuentran los archivos sobre los cuales estuvimos trabajando.

***main.py:***
 
Este código permite registrar nuevos usuarios, iniciar sesión, y verificar contraseñas. Las funciones principales son:

**validar_clave():**  Verifica que la contraseña tenga al menos 8 caracteres y cumpla los criterios de seguridad.

**registrar_usuario():** Permite registrar un nuevo usuario, asegurándose de que el nombre de usuario y la contraseña sean válidos, e incluye un CAPTCHA de verificación.

**iniciar_sesion():** Permite a los usuarios iniciar sesión con su nombre de usuario y contraseña. Después de cuatro intentos fallidos, el usuario es bloqueado.

**menu_principal():** Muestra el menú principal con opciones para iniciar sesión, registrar usuario, salir o recuperar la contraseña.

***aritmetica.py***

Este código contiene funciones  para operaciones matemáticas y manejo de fecha y hora. Las funciones son:

**sumar(a, b):** Suma dos números y devuelve el resultado redondeado a dos decimales.

**restar(a, b):** Resta dos números y devuelve el resultado redondeado a dos decimales.

**dividir(a, b):** Divide dos números, manejando la excepción de división por cero y devolviendo un mensaje de error en ese caso. El resultado se redondea a dos decimales.

**multiplicar(a, b):** Multiplica dos números y devuelve el resultado redondeado a dos decimales.

**sumar_n(args:**)Suma un número variable de argumentos y devuelve el resultado redondeado a dos decimales.

**promedio_n(args):** Calcula el promedio de un número variable de argumentos. Devuelve 0 si no se proporcionan argumentos.

**obtener_fecha_hora():** Devuelve la fecha y hora actual en formato "YYYY-MM-DD HH:MM:SS".

***test_aritmética.py***

Este código lo utilizamos para comprobar que las funciones del módulo aritmética funcionan correctamente.

**test_sumar():** Prueba la función sumar(a,b) para casos de suma (números positivos, negativos y ceros).

**test_restar():** Prueba la función restar(a,b) con diferentes casos (restas con números positivos, negativos y ceros).

**test_dividir():** Prueba la función dividir(a,b)con divisiones normales y devuelve un mensaje de error si se divide por 0.

**test_multiplicar():** Comprueba que la función multiplicar(a,b) funcione con números positivos, negativos y ceros.

**test_sumar_n():** Prueba que la función sumar_n(*args)  sumen correctamente varios números, números negativos y que cuando no haya argumentos devuelva 0.

**test_promedio_n():** Comprueba que la función promedio_n(*args) calcule correctamente el promedio de diferentes números y que devuelva 0 cuando no haya argumentos.


Se creó una aplicación en Python que implementa un sistema de gestión de usuarios y accesos, cumpliendo con la consigna de crear las clases Usuario y Acceso, donde un usuario puede tener múltiples accesos registrados, y cada acceso está asociado a un usuario.

**Funcionalidades del sistema:**
**Clases Usuario y Acceso:**

La clase Usuario tiene atributos como id, username, password, y email.
La clase Acceso incluye atributos como id, fechaIngreso, fechaSalida, y usuarioLogueado.

**Menú Principal:** El programa ofrece un menú interactivo que permite realizar las siguientes acciones:

         1- CRUD de Usuarios:
Agregar usuario: permite crear nuevos usuarios y almacenarlos.
Modificar usuario: permite actualizar el correo electrónico o la contraseña de un usuario existente.
Eliminar usuario: elimina usuarios de la base de datos, ya sea mediante username o email.
Buscar usuario: permite buscar usuarios por su username o email y mostrar sus detalles. Si no se encuentra, se muestra un mensaje informando que el usuario no existe.
Mostrar todos los usuarios: muestra una lista de todos los usuarios registrados.

        2- Salir del programa.
        3- Ingresar al sistema: el usuario puede acceder proporcionando su username y password. Si las credenciales son correctas, el sistema permite al usuario ingresar y registrar un acceso, además de ofrecer la opción de volver al menú principal o salir de la aplicación.

**Gestión de Archivos:**
Los usuarios se almacenan en un archivo binario llamado usuarios.ispc.
Cada vez que un usuario accede al sistema, se registra en un archivo binario accesos.ispc el objeto Acceso correspondiente, incluyendo el usuarioLogueado y las fechas de ingreso y salida.
Si un intento de acceso falla (por credenciales incorrectas), se deja un registro detallado en un archivo de texto llamado logs.txt, que incluye la fecha y hora del intento fallido, junto con el username y la password ingresados.

La aplicación sigue el paradigma de Programación Orientada a Objetos (POO) para gestionar los usuarios y accesos, y permite mantener un control adecuado sobre los datos mediante la lectura y escritura en archivos binarios y de texto.


Para ejecutar y probar el programa hay que hacerlo desde alguna app que corra el código Python, como puede ser Visual Studio Code, y una vez ahí se desarrolla el menú inicial en donde podemos hacer las distintas acciones del menú.
Es necesario instalar algunos componentes adicionales para ejecutar correctamente el programa:
Python 3.x
MySQL
Paquete mysql-connector-python


**Problemas e inconvenientes**
Algunos problemas que encontramos:
Conexión a la base de datos: Tuvimos problemas iniciales al configurar la conexión con MySQL debido a permisos y errores de autenticación. Solucionamos esto ajustando las credenciales y asegurando que el servidor MySQL estuviera corriendo.
Dependencias: Al instalar mysql-connector-python, nos encontramos con algunas incompatibilidades de versiones de Python, que fueron resueltas actualizando el entorno virtual.








