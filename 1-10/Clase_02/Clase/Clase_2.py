# ==============================================================================
#                     CURSO PERSONALIZADO DE PYTHON DESDE CERO
# ==============================================================================
# CLASE 2: Interacción con el usuario y tipos de datos en Python
# ------------------------------------------------------------------------------
# Instrucciones:
# Copia todo este código y pégalo directamente en tu editor de Python.
# Ejecútalo para experimentar con el código interactivo.
# ==============================================================================


# ------------------------------------------------------------------------------
# 1. REPASO Y REFORZAMIENTO: Salto de línea vs Salida en la misma línea
# ------------------------------------------------------------------------------
# En la Clase 1 aprendimos a usar print().
# Cada print() por defecto agrega un salto de línea al final.

print("Línea 1")
print("Línea 2")

# Si usamos comas dentro de UN SOLO print(), los datos salen en LA MISMA línea:
print("Línea A", "Línea B")


# ------------------------------------------------------------------------------
# 2. ENTRADA DE DATOS: La función input()
# ------------------------------------------------------------------------------
# Hasta ahora, nosotros escribíamos los datos fijos en el código.
# Para hacer programas interactivos que le pidan información al usuario,
# usamos la función input().

# Sintaxis:
# variable = input("Mensaje de solicitud: ")

# Ejemplo (puedes ejecutarlo y escribir en la consola):
# nombre_usuario = input("¿Cómo te llamas? ")
# print("Hola,", nombre_usuario)


# ------------------------------------------------------------------------------
# 3. LOS TIPOS DE DATOS BÁSICOS EN PYTHON
# ------------------------------------------------------------------------------
# Python clasifica la información en diferentes "Tipos de Datos":
#
# 1. Texto (String / str): Cadenas entre comillas.
#    Ejemplo: "Luan", "Python", "123"
#
# 2. Números Enteros (Integer / int): Números sin decimales.
#    Ejemplo: 22, -5, 0
#
# 3. Números Decimales (Float / float): Números con punto decimal.
#    Ejemplo: 17.5, 3.1416, 0.5
#
# 4. Booleanos (Boolean / bool): Solo dos valores posibles: True (Verdadero) o False (Falso).
#    Ejemplo: activo = True, juego_terminado = False


# ------------------------------------------------------------------------------
# 4. EL GRAN TRUCO DE input() Y LA CONVERSIÓN DE TIPOS (CASTING)
# ------------------------------------------------------------------------------
# ¡ATENCIÓN! La función input() SIEMPRE lee lo que escribe el usuario como TEXTO (str).
# Incluso si el usuario escribe un número como 22, input() recibe "22".

# Si intentas sumar texto, Python pega los textos (Concatenación) en vez de sumar:
# print("20" + "20")  # Resultado: "2020", NO 40.

# Para convertir un texto a número usamos int() o float():

# edad_texto = input("¿Cuál es tu edad? ")
# edad_numero = int(edad_texto) # Convierte el texto "22" al entero 22
# edad_siguiente = edad_numero + 1
# print("El próximo año tendrás:", edad_siguiente)

# O todo en una sola línea (lo habitual en Python):
# edad = int(input("Ingresa tu edad: "))


# ------------------------------------------------------------------------------
# CÓDIGO PRÁCTICO DE EJEMPLO COMPLETO
# ------------------------------------------------------------------------------

# 1. Entrada de texto
usuario = "Luan"  # Simulación o puedes usar: input("Usuario: ")
pais = "Perú"

# 2. Entrada de números enteros y decimales con conversión (int / float)
edad = int("22")           # Simula: int(input("Edad: "))
estatura = float("1.75")   # Simula: float(input("Estatura en metros: "))

# 3. Tipos booleanos
es_mayor_de_edad = True

# 4. Operaciones con los datos leídos
ano_nacimiento = 2026 - edad

# 5. Salida de resultados
print("----------------------------------------")
print("RESUMEN DE USUARIO")
print("----------------------------------------")
print("Nombre:", usuario)
print("País:", pais)
print("Año aproximado de nacimiento:", ano_nacimiento)
print("Estatura:", estatura, "m")
print("¿Es mayor de edad?:", es_mayor_de_edad)


# ==============================================================================
#                               50 EJERCICIOS
# ==============================================================================
# Instrucciones: Resuelve cada ejercicio agregando tu código debajo de la instrucción.
# Recuerda responder todos los ejercicios utilizando variables cuando se te solicite.
# ------------------------------------------------------------------------------

# --- BLOQUE A: Repaso activo y fijación de base (Ejercicios 1 a 10) ---
# 1. Muestra en 3 líneas separadas (usando 3 print) los números 1, 2 y 3.
# 2. Muestra los números 1, 2 y 3 en una sola línea separados por comas usando 1 solo print.
# 3. Declara una variable llamada costo = 50 y muestra el resultado de multiplicarla por 4 utilizando LA VARIABLE dentro del print.
# 4. Declara num = 10. En la siguiente línea súmale 5 guardando el resultado en la misma variable num. Muestra num.
# 5. Muestra en un solo print tu nombre y la palabra "Presente", separados por un guion usando coma y texto.
# 6. Muestra el resultado de dividir 20 entre 4 utilizando el operador /.
# 7. Crea una variable con un valor booleano True que indique si un sistema está encendido (sistema_encendido).
# 8. Crea una variable booleana False para indicar que un juego ha terminado (game_over).
# 9. Asigna el número decimal 9.99 a la variable precio_dolar y muéstrala.
# 10. Escribe un comentario explicando qué tipo de dato es "100" frente a 100.

# --- BLOQUE B: Uso de input() para texto (Ejercicios 11 a 20) ---
# 11. Pide al usuario su nombre mediante input() y guárdalo en la variable nombre.
# 12. Pide al usuario su comida favorita mediante input() y muéstrala con el mensaje "Tu comida favorita es:".
# 13. Pide al usuario el nombre de su mascota y muestralo en pantalla.
# 14. Pide la ciudad donde vive el usuario y muestra "Bienvenido a" seguido del nombre de la ciudad.
# 15. Pide al usuario su color favorito y muestra el color dos veces en líneas consecutivas.
# 16. Solicita el nombre de una canción y el artista en dos input() separados. Muestra ambos en una sola línea.
# 17. Solicita una palabra al usuario y muestra la palabra precedida y seguida por la variable separador = "***".
# 18. Pide al usuario un adjetivo (ej: "rápido") y un sustantivo (ej: "auto"). Muestra ambos combinados.
# 19. Solicita al usuario su profesión y muéstrala formateada dentro de un reporte simple.
# 20. Simula un login: pide el nombre de usuario mediante input() y muestra "Acceso concedido a: [nombre]".

# --- BLOQUE C: Conversión de tipos (int() y float()) (Ejercicios 21 a 30) ---
# 21. Pide la edad al usuario usando input(), conviértela a int() y muéstrala.
# 22. Pide un número al usuario, conviértelo a int() y muestra el doble de ese número (número * 2).
# 23. Pide el precio de un producto (usa float(input(...))) y muestra el precio.
# 24. Pide un número entero al usuario y muestra el número anterior (número - 1) y el posterior (número + 1).
# 25. Pide al usuario su año de nacimiento como entero y calcula su edad en el año 2026.
# 26. Solicita una cantidad de dinero (float) y calcula cuánto dinero queda si se gasta 12.50.
# 27. Pide un número decimal al usuario y muestra el resultado de multiplicarlo por 10.
# 28. Pide la nota de un examen (decimal) y muestra "Nota ingresada:" junto con el valor.
# 29. Solicita la cantidad de horas trabajadas (entero) y calcula el pago total si la hora vale 15.
# 30. Pide al usuario la cantidad de días de vacaciones y calcula cuántas horas equivalen (días * 24).

# --- BLOQUE D: Combinación de texto y matemáticas interactivas (Ejercicios 31 a 40) ---
# 31. Pide la base y la altura de un rectángulo (ambos enteros) y muestra el área (base * altura).
# 32. Modifica el programa anterior para calcular el perímetro del rectángulo (2 * base + 2 * altura).
# 33. Pide al usuario el precio de 3 productos distintos (float) y muestra el total acumulado de la compra.
# 34. Pide la distancia en kilómetros (float) y calcula la distancia en metros (kilómetros * 1000).
# 35. Solicita al usuario 2 números enteros y muestra la suma, la resta y la multiplicación entre ellos.
# 36. Pide la cantidad de personas en una mesa y la cuenta total de la cena (float). Muestra cuánto debe pagar cada uno (cuenta / personas).
# 37. Solicita al usuario su peso en kg (float) y muestra su peso estimado si aumentara 2.5 kg.
# 38. Pide al usuario su nombre y su año de nacimiento. Muestra: "[nombre] tendrá [X] años en el año 2030".
# 39. Pide la velocidad de un auto en km/h (float) y calcula el tiempo en horas para recorrer 500 km (500 / velocidad).
# 40. Pide una cantidad de minutos (entero) y calcula cuántos segundos representa (minutos * 60).

# --- BLOQUE E: Desafíos integradores de razonamiento (Ejercicios 41 a 50) ---
# 41. Escribe un programa que pida el nombre del cliente, producto comprado, cantidad (int) y precio unitario (float). Muestra el total a pagar.
# 42. Pide la temperatura actual en grados Celsius (float) y conviértela a Fahrenheit usando la fórmula: (celsius * 9/5) + 32.
# 43. Pide al usuario la nota de 3 evaluaciones (float) y muestra la nota promedio (suma de las 3 / 3).
# 44. Crea una calculadora de propinas: Pide el total de la cuenta (float) y el porcentaje de propina que desea dejar (ej: 10, 15). Calcula y muestra el monto exacto de la propina.
# 45. Simula un conversor de moneda: Pide la cantidad en soles/pesos (float) y la tasa de cambio a dólares (float). Muestra el equivalente en dólares.
# 46. Pide al usuario el número de respuestas correctas (int) e incorrectas (int) en un examen de 20 preguntas. Muestra el puntaje final si cada correcta vale 5 puntos y cada incorrecta resta 2.
# 47. Solicita la edad actual del usuario y calcula en qué año cumplirá 100 años.
# 48. Un cine cobra 12.00 por entrada de adulto y 7.00 por niño. Pide la cantidad de adultos y de niños y calcula el total a pagar.
# 49. Pide un tiempo en horas (int) y muestra a cuántos minutos y a cuántos segundos equivale en dos líneas separadas.
# 50. DESAFÍO FINAL DE LA CLASE:
#     Diseña un "Generador de Factura Simplificada Interactiva".
#     El programa debe solicitar interactiva mediante input():
#     - Nombre del cliente
#     - Nombre del producto A y su precio (float)
#     - Nombre del producto B y su precio (float)
#     - Porcentaje de impuesto IGV/IVA a aplicar (ej: 18)
#     El programa debe calcular:
#     - Subtotal (Suma de precios)
#     - Monto del impuesto (Subtotal * (porcentaje / 100))
#     - Total general (Subtotal + Monto del impuesto)
#     Muestra una factura visualmente ordenada con bordes decorativos, con todas las etiquetas claras y los valores formateados.


# ==============================================================================
#                         PROYECTO PRÁCTICO: CLASE 2
# ==============================================================================
# NOMBRE: Calculadora Interactiva de Presupuesto Mensual Personal
# ------------------------------------------------------------------------------
# Requisitos mínimos:
# 1. Solicitar mediante input() los siguientes datos al usuario:
#    - Nombre del usuario.
#    - Mes presupuestado.
#    - Ingreso mensual total (float).
#    - Gasto estimado en Vivienda/Alquiler (float).
#    - Gasto estimado en Alimentación (float).
#    - Gasto estimado en Servicios/Transporte (float).
#    - Gasto estimado en Entretenimiento (float).
#
# 2. Realizar los siguientes cálculos automáticos:
#    - Total de Gastos = Vivienda + Alimentación + Servicios + Entretenimiento
#    - Saldo Disponible = Ingreso Total - Total de Gastos
#    - Porcentaje de Ingreso Gastado = (Total de Gastos / Ingreso Total) * 100
#
# 3. Presentación:
#    - Un reporte limpio en consola decorado con marcos de caracteres (ej: `=`, `-`, `*`).
#    - Etiquetas claras en español para cada dato leído y cada resultado calculado.
#
# Restricciones:
# - No utilices condicionales `if` ni bucles `for`/`while` todavía.
# ==============================================================================