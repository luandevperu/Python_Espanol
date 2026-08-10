# ==============================================================================
#                     CURSO PERSONALIZADO DE PYTHON DESDE CERO
# ==============================================================================
# CLASE 1: Mostrar información y guardar tus primeros datos
# ------------------------------------------------------------------------------
# Instrucciones:
# Copia todo este código y pégalo directamente en tu editor de Python.
# Puedes ejecutar el archivo para ver qué hace cada sección explicada.
# ==============================================================================


# ------------------------------------------------------------------------------
# 1. ¿QUÉ ES UN PROGRAMA Y CÓMO SE COMUNICA CONTIGO?
# ------------------------------------------------------------------------------
# Para lograr que la pantalla te muestre una palabra, una frase o un número, 
# usamos una instrucción llamada print(). 
# En Python, la palabra "print" significa imprimir o mostrar en pantalla.

print("¡Hola, mundo!")

# REGRA FUNDAMENTAL: 
# Todo texto que quieras mostrar tal cual debe ir encerrado entre comillas dobles
# ("...") o comillas simples ('...'). A este texto se le conoce técnicamente 
# como "cadena de texto" o "string".


# ------------------------------------------------------------------------------
# 2. NÚMEROS VERSUS TEXTO
# ------------------------------------------------------------------------------
# Python distingue claramente entre texto y números:
# - Texto: "10" (Para Python esto es una palabra o símbolo, no un valor matemático).
# - Número: 10 (Sin comillas. Python lo reconoce como valor numérico para calcular).

print(10)       # Muestra el número 10
print("10")     # Muestra el texto "10"
print(5 + 3)    # Calcula la operación matemática y muestra 8
print("5 + 3")  # Muestra literal el texto "5 + 3"


# ------------------------------------------------------------------------------
# 3. VARIABLES: CAJAS PARA GUARDAR INFORMACIÓN
# ------------------------------------------------------------------------------
# Imagina que una VARIABLE es una caja en la memoria de la computadora a la que
# le pones una etiqueta con un nombre. Dentro de esa caja guardas un dato.
# Para crear una variable usamos el símbolo de asignación (=):

nombre = "Carlos"
edad = 25

# Para mostrar el contenido de una variable, pones su nombre dentro del print()
# SIN COMILLAS:

print(nombre)  # Muestra: Carlos
print(edad)    # Muestra: 25

# Nota: Si pones print("nombre"), mostrará la palabra literal "nombre" 
# y no lo que está guardado en la caja.


# ------------------------------------------------------------------------------
# 4. COMENTARIOS: NOTAS PARA EL PROGRAMADOR
# ------------------------------------------------------------------------------
# Cualquier línea que empiece con el símbolo # es un COMENTARIO.
# Python ignora completamente los comentarios al ejecutar el programa.

# Este es un comentario. Python no ejecutará esta línea.
print("Esta línea sí se ejecutará")


# ------------------------------------------------------------------------------
# CÓDIGO PRÁCTICO DE EJEMPLO COMPLETO
# ------------------------------------------------------------------------------

# 1. Mostrar textos sencillos
print("Bienvenido al curso de Python")
print('Puedes usar comillas dobles o simples')

# 2. Mostrar números y operaciones matemáticas básicas
print(2026)
print(10 + 5)
print(20 - 4)

# 3. Mostrar varios elementos en una misma línea usando comas
print("Mi año de nacimiento es:", 2000)

# 4. Uso de variables
nombre_usuario = "Ana"
nivel = 1
puntos = 150

print("Usuario:")
print(nombre_usuario)
print("Nivel actual:")
print(nivel)
print("Puntaje acumulado:")
print(puntos)

# 5. Cambiar el valor de una variable (sobrescribir)
puntos = 200  # Ahora la caja "puntos" guarda el número 200
print("¡NUEVO PUNTAJE!")
print(puntos)


# ==============================================================================
#                               50 EJERCICIOS
# ==============================================================================
# Instrucciones para los ejercicios:
# Resuelve cada ejercicio escribiendo el código correspondiente debajo del número.
# No olvides entregarme tus respuestas (del 1 al 50) para corregirlas y ponerte
# tu primera calificación de 0 a 50.
# ------------------------------------------------------------------------------

# --- BLOQUE A: Sintaxis básica y texto libre (Ejercicios 1 a 10) ---
# 1. Muestra en pantalla el mensaje: Estoy aprendiendo Python.
# 2. Muestra tu primer nombre en pantalla dentro de un print().
# 3. Muestra tu país de residencia en pantalla.
# 4. Muestra en líneas separadas mediante tres print() distintos tu plato de comida favorito, tu color favorito y tu pasatiempo.
# 5. Muestra una frase entre comillas dobles.
# 6. Muestra la misma frase del ejercicio 5 usando comillas simples.
# 7. Muestra el número 100 en pantalla sin usar comillas.
# 8. Muestra la palabra "100" en pantalla usando comillas.
# 9. Escribe un programa que tenga un comentario en la primera línea que diga "# Mi primer ejercicio" y abajo muestre el mensaje "Hola".
# 10. Muestra en pantalla la palabra "Python" tres veces, cada una en una instrucción print() distinta.

# --- BLOQUE B: Distinción entre texto, números y expresiones (Ejercicios 11 a 20) ---
# 11. Muestra en pantalla el resultado directo de la suma 15 + 35 sin usar comillas.
# 12. Muestra en pantalla el texto "15 + 35" usando comillas.
# 13. Muestra la resta 100 - 42 sin comillas.
# 14. Muestra la multiplicación de 6 * 7 en pantalla.
# 15. Muestra en un solo print() el texto "Resultado:" seguido del número 50 (separados por coma).
# 16. Muestra en un solo print() tu nombre y tu edad separados por coma.
# 17. Escribe dos líneas de código que muestren la diferencia entre print(2 + 2) y print("2 + 2").
# 18. Muestra el resultado de 100 + 200 - 50.
# 19. Muestra la cadena de texto "Mensaje 1" y en la línea siguiente "Mensaje 2".
# 20. Crea una línea de código con un comentario que explique qué hace la instrucción print("Prueba") colocada justo abajo.

# --- BLOQUE C: Creación y uso de variables básicas (Ejercicios 21 a 30) ---
# 21. Crea una variable llamada "ciudad" y asígnale el nombre de tu ciudad. Muestra la variable en pantalla.
# 22. Crea una variable llamada "edad" y asígnale tu edad actual en número. Muéstrala en pantalla.
# 23. Crea una variable llamada "precio" con el valor 99 y muéstrala.
# 24. Crea dos variables: "nombre" con tu nombre y "apellido" con tu apellido. Muestra ambas variables en dos print() independientes.
# 25. Muestra las dos variables anteriores ("nombre" y "apellido") en una sola línea usando print(nombre, apellido).
# 26. Crea una variable llamada "mascota" con el valor "Perro". En la siguiente línea cambia su valor a "Gato". Muestra la variable al final.
# 27. Crea una variable "dia" con el número de hoy y una variable "mes" con el nombre del mes actual. Muestra ambos en una sola línea.
# 28. Crea una variable "x" con el valor 10 y una variable "y" con el valor 20. Muestra la suma de las variables escribiendo print(x + y).
# 29. Asigna el número 50 a una variable llamada "puntos_iniciales". Muestra el texto "Puntos:" y al lado la variable.
# 30. Crea una variable llamada "mensaje" que guarde "Sistema listo". Muestra la variable dos veces seguidas en líneas diferentes.

# --- BLOQUE D: Combinación de conceptos y razonamiento (Ejercicios 31 a 40) ---
# 31. Crea una variable "producto" con valor "Lapicero" y otra "cantidad" con valor 5. Muestra: "Producto:", producto, "Cantidad:", cantidad en un solo print().
# 32. Crea una variable "a" con el valor 5 y una variable "b" con el valor "a". Muestra "b" en pantalla. ¿Qué valor imprime?
# 33. Escribe corregido el siguiente código que tiene un error de comillas: print(Hola mundo)
# 34. Escribe corregido el siguiente código que tiene un error de nombre de variable:
#     mi_variable = "Python"
#     print(mivariable)
# 35. Crea una variable "saldo" con el valor 100. En la siguiente línea sobrescribe "saldo" asignándole 150. Muestra "saldo".
# 36. Escribe un programa que cree tres variables: "paso1", "paso2" y "paso3" con los textos "Encender", "Cargar", "Ejecutar". Muestra cada una en orden.
# 37. Crea una variable num1 = 12 y num2 = 8. Crea una tercera variable resultado = num1 + num2. Muestra resultado.
# 38. Modifica el ejercicio anterior para que la variable resultado guarde la resta num1 - num2. Muestra resultado.
# 39. Escribe código que muestre en pantalla una figura simple de 3 líneas hecha con asteriscos * usando tres print().
# 40. Crea una variable separador que guarde el texto "--------------------". Muestra el separador, luego el mensaje "INICIO", y luego el separador de nuevo.

# --- BLOQUE E: Desafíos de lógica y memoria de sintaxis (Ejercicios 41 a 50) ---
# 41. Crea una ficha personal en código usando las variables: nombre_completo, profesion, anos_experiencia. Muestra cada dato formateado con texto explicativo previo.
# 42. Escribe un programa que declare precio_base = 100 e impuesto = 21. Crea una variable precio_total = precio_base + impuesto y muéstrala junto a un texto descriptivo.
# 43. Escribe el código e indica qué valor mostrará la variable x al final:
#     x = 10
#     x = 5
#     print(x)
# 44. Crea una variable "titulo" con el nombre de tu película favorita y "ano" con su año de estreno. Muestra ambas en una sola línea separadas por comas.
# 45. Escribe un programa que muestre el encabezado de un recibo de compra en 4 líneas utilizando comillas, números y guiones decorativos.
# 46. Tienes las variables viento = "Fuerte" y temperatura = 18. Muestra el reporte meteorológico combinando texto con ambas variables en un solo print().
# 47. Guarda el número 7 en la variable base y 3 en altura. Muestra el resultado de base * altura.
# 48. Declara tres variables con los nombres de tres frutas distintas. Muestra el texto "Lista de compras:" y luego las tres frutas numeradas del 1 al 3 en líneas separadas.
# 49. Simula el marcador de un partido de fútbol: crea variables equipo_local, equipo_visitante, goles_local, goles_visitante. Muestra una línea con el estado actual del partido.
# 50. DESAFÍO FINAL:
#     Diseña el reporte completo de estado de un servidor de videojuegos.
#     Define al menos 6 variables (nombre_servidor, estado_linea, jugadores_activos, capacidad_maxima, ping_promedio, version_game).
#     Muestra en pantalla un reporte estructurado utilizando barras decorativas, títulos, las variables y operaciones simples para calcular cuántos cupos libres quedan (capacidad_maxima - jugadores_activos).


# ==============================================================================
#                         PROYECTO PRÁCTICO: CLASE 1
# ==============================================================================
# NOMBRE: Ficha de Personaje de Videojuego (RPG Console Card)
# ------------------------------------------------------------------------------
# Requisitos mínimos:
# 1. Variables obligatorias:
#    - nombre_personaje (texto)
#    - clase_rol (texto)
#    - nivel (número)
#    - vida_maxima (número)
#    - vida_actual (número)
#    - fuerza (número)
#    - defensa (número)
#    - arma_principal (texto)
#
# 2. Cálculos automáticos:
#    - dano_estimado = fuerza + 10
#    - vida_perdida = vida_maxima - vida_actual
#
# 3. Presentación:
#    - Usar marcas o líneas decorativas con =, - o *.
#    - Mostrar cada dato etiquetado claramente en español.
#
# Restricciones:
# - Usa únicamente lo enseñado hasta ahora (print, variables, cadenas, números y comentarios).
# ==============================================================================