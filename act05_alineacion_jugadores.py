def registrar_jugadores():
    # 1. Creamos la LISTA vacía que contendrá a todos los jugadores
    plantilla = []

    print("--- Sistema de Gestión de Plantilla ---")
    print("Introduce los datos. Escribe 'salir' en el nombre para terminar.\n")

    while True:
        # DATOS
        nombre = input("Nombre del jugador: ").strip()

        # Condición de salida
        if nombre.lower() == 'salir':
            break

        # Pedimos las 2 características obligatorias
        # (Puedes cambiar 'Posición' y 'Dorsal' por lo que prefieras)
        posicion = input(f"Posición de {nombre}: ").strip()

        # Validación simple para que el dorsal sea un número (opcional)
        while True:
            try:
                dorsal = int(input(f"Número (Dorsal) de {nombre}: "))
                break
            except ValueError:
                print("Por favor, introduce un número válido para el dorsal.")

        # 2. Creamos un DICCIONARIO para este jugador específico
        # Aquí guardamos las claves y sus valores
        jugador_actual = {
            "nombre": nombre,
            "posicion": posicion,
            "dorsal": dorsal
        }

        # 3. Guardamos el diccionario dentro de la lista principal
        plantilla.append(jugador_actual)
        print("✅ Jugador añadido.\n")

    # Salida de datos (La Plantilla Final)
    print("\n" + "=" * 40)
    print(f"{'DORSAL':<8} {'NOMBRE':<20} {'POSICIÓN'}")
    print("=" * 40)

    # Recorremos la lista. En cada vuelta, 'j' es un diccionario.
    for j in plantilla:
        # Accedemos a los valores usando las claves del diccionario
        print(f"{j['dorsal']:<8} {j['nombre']:<20} {j['posicion']}")

    print("=" * 40)
    print(f"Total de jugadores registrados: {len(plantilla)}")


# Ejecutamos el programa
registrar_jugadores()