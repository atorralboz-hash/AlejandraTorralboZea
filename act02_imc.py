# variables para el calculo del IMC
peso = 70 # en kilogramos
altura = 1.75 # altura en metros

# calculo del IMC
# imc = peso / (altura * altura)
imc = peso / (altura ** 2)
print(imc)

# Clasificacion el resultado
if imc < 18.5:
    print("déficit de peso")
elif imc >= 18.5 and imc <= 25:
        print("peso normal")
elif imc >= 25 and imc <= 30:
    print("sobrepeso")
elif imc >= 30:
    print("obeso")


