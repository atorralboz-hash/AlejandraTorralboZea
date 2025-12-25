def analizar_compra():
    precios = []  # Lista vacía para guardar los precios

    print("--- Calculadora de Supermercado ---")
    print("Introduce los precios de los productos uno por uno.")
    print("Escribe 'fin' o '0' cuando hayas terminado.\n")

    while True:
        entrada = input("Precio del producto ($): ")

        # Condición de salida
        if entrada.lower() in ['fin', 'salir']:
            break

        try:
            precio = float(entrada)

            # Si el usuario pone 0, también terminamos (opcional)
            if precio == 0:
                break

            if precio < 0:
                print("⚠️  El precio no puede ser negativo.")
            else:
                precios.append(precio)  # Añadimos el precio a la lista

        except ValueError:
            print("❌ Error: Por favor introduce un número válido.")

    # Resultados
    print("\n" + "-" * 30)
    if len(precios) > 0:
        # Usamos funciones nativas de Python (max, min, sum)
        maximo = max(precios)
        minimo = min(precios)
        total = sum(precios)
        promedio = total / len(precios)

        print(f"Items comprados: {len(precios)}")
        print(f"Producto más caro:  ${maximo:,.2f}")
        print(f"Producto más barato: ${minimo:,.2f}")
        print(f"Precio promedio:     ${promedio:,.2f}")
        print("-" * 30)
        print(f"TOTAL A PAGAR:       **${total:,.2f}**")
    else:
        print("No se introdujeron productos.")


# Ejecutamos la función
analizar_compra()