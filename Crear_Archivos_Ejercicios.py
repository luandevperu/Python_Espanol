import os

# Nombre de la carpeta que se creará
carpeta = "Ejercicios"

# Crear la carpeta si no existe
os.makedirs(carpeta, exist_ok=True)

# Crear los 50 archivos vacíos
for numero in range(1, 51):
    nombre_archivo = f"Ejercicio_{numero:02d}.py"
    ruta = os.path.join(carpeta, nombre_archivo)

    # Crear el archivo vacío
    open(ruta, "w", encoding="utf-8").close()

print("¡Listo! Se crearon los 50 archivos.")
print(f"Carpeta creada: {carpeta}")