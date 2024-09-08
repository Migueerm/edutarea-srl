# EduTarea SRL

**Integrantes**

| Nombre y  Apellido  |    DNI    | Correo eléctronico        | Link Git Hub |
|---------------------|-----------|---------------------------|--------------
| Melania Ligorria    | 38412646  | melanialigorria@gmail.com | https://github.com/mel-ligorria
| Miguel Rojas        | 39215582  | rojas.miguel018@gmail.com | https://github.com/Migueerm/ejercitacion-ispc
| Florencia Andrada   | 44788525  | florenciacarolina031@gmail.com | https://github.com/Flor3ncia-Andr4d4
| Carlota Olmedo      | 41711170  | carlota_olmedo@hotmail.com| https://github.com/caolmedo
| Guadalupe Mendoza   | 45934026  | despontinguadalupe@gmail.com |https://github.com/Guadamendoza/SolucionesPracticas 

**Acceso al documento**: https://docs.google.com/document/d/1HBbKnpZKu7OGHchEQCvZZ0spJUapiImHA_sHksqoFFk/edit

**Descripción del repositorio**

El repositorio de EduTarea SRL contiene una carpeta con el nombre “Evidencia” donde se encuentran los archivos sobre los cuales estuvimos trabajando.

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





