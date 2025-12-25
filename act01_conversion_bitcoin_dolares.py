import requests


def obtener_precio_bitcoin():
    try:
        # Usamos la API pública de Coindesk
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        respuesta = requests.get(url)
        datos = respuesta.json()
        # Extraemos el precio en flotante (float)
        precio = datos['bpi']['USD']['rate_float']
        return precio
    except:
        return None


# Bloque Principal 1
print("Consultando precio del Bitcoin en tiempo real...")
precio_actual = obtener_precio_bitcoin()

if precio_actual:
    try:
        cantidad = float(input("Introduce la cantidad de Bitcoins: "))
        total = cantidad * precio_actual

        print(f"\nEl precio actual del Bitcoin es: ${precio_actual:,.2f}")
        print(f"{cantidad} BTC equivalen a: **${total:,.2f} USD**")

    except ValueError:
        print("Error: Introduce un número válido.")
else:
    print("Error: No se pudo conectar a internet para obtener el precio.")