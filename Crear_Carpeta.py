from pathlib import Path

# Carpeta donde está este programa
carpeta = Path(__file__).parent

# Buscar los 50 ejercicios
ejercicios = sorted(
    carpeta.glob("Ejercicio_*.py"),
    key=lambda archivo: int(archivo.stem.split("_")[1])
)

# Archivo de entrega
archivo_entrega = carpeta / "ENTREGA_CLASE.txt"

with open(archivo_entrega, "w", encoding="utf-8") as entrega:

    entrega.write("=" * 60 + "\n")
    entrega.write("ENTREGA DE EJERCICIOS DE PYTHON\n")
    entrega.write("=" * 60 + "\n\n")

    # Copiar el contenido de cada ejercicio
    for ejercicio in ejercicios:

        numero = ejercicio.stem.split("_")[1]

        entrega.write("\n")
        entrega.write("=" * 60 + "\n")
        entrega.write(f"EJERCICIO {numero}\n")
        entrega.write("=" * 60 + "\n\n")

        contenido = ejercicio.read_text(encoding="utf-8")

        if contenido.strip():
            entrega.write(contenido)
        else:
            entrega.write("[EJERCICIO VACÍO]\n")

        entrega.write("\n\n")

print("✅ Entrega creada correctamente.")
print(f"📄 Archivo: {archivo_entrega.name}")
print(f"📚 Ejercicios encontrados: {len(ejercicios)}")