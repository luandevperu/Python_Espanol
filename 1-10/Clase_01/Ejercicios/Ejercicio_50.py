# 50. DESAFÍO FINAL:
#     Diseña el reporte completo de estado de un servidor de videojuegos.
#     Define al menos 6 variables (nombre_servidor, estado_linea, jugadores_activos, capacidad_maxima, ping_promedio, version_game).
#     Muestra en pantalla un reporte estructurado utilizando barras decorativas, títulos, las variables y operaciones simples para calcular cuántos cupos libres quedan (capacidad_maxima - jugadores_activos).
barra = "------------------------"
nombre_servidor = "Crafting"
estado_linea = "Activo"
jugadores_activos = 20
capacidad_maxima = 25
ping_promedio = 30
version_game = 1.0
print (barra, "Reporte diario de", nombre_servidor, barra)
print ("Estado:", estado_linea)
print ("Jugadores activos:", jugadores_activos)
print ("Espacios disponibles:", capacidad_maxima - jugadores_activos)
print ("Versiòn del juego:", version_game)
