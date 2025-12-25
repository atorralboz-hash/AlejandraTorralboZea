def clasificar_nota(nota):
    """
    Función que recibe una nota (float) y devuelve su clasificación.
    """
    # Primero verificamos que la nota sea válida
    if nota < 0 or nota > 10:
        return "Error: La nota debe estar entre 0 y 10."

    # Clasificación según la escala
    if nota < 5.0:
        return "Suspenso"
    elif nota < 7.0:
        return "Aprobado"
    elif nota < 9.0:
        return "Notable"
    else:
        return "Sobresaliente"


# Bloque principal para probar el script
try:
    entrada = float(input("Introduce la nota del estudiante: "))

    resultado = clasificar_nota(entrada)
    print(f"La calificación para {entrada} es: **{resultado}**")

except ValueError:
    print("Por favor, introduce un número válido.")