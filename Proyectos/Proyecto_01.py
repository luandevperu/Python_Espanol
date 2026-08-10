decorador = "======================================"
separador = "----------------------------"
nombre = "   Ficha de Personaje de Videojuego"
usuario = "Luan"
clase = "Mago"
nivel = 10
vida_maxima = 100
vida_actual = 50
fuerza = 10
dano_base = 10
defensa = 5
arma_principal = "baston"
dano = dano_base + fuerza
vida_perdida = vida_maxima - vida_actual

print (decorador)
print (nombre)
print (decorador)
print ("            Datos generales")
print ("Usuario:", usuario)
print ("Clase:", clase)
print ("Nivel:", nivel)
print ("Vida màxima:", vida_maxima)
print ("Vida actual:", vida_actual)
print ("Vida perdida:", vida_perdida)
print ("Fuerza:", fuerza)
print ("Daño base:", dano_base)
print ("Defensa:", defensa)
print ("Arma principal:", arma_principal)
print ("Daño total:", dano)