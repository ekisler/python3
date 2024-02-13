import random

numero_random = random.randint(1, 10)

print(numero_random)

print("******************************************************")

# Si el usuario acierta el resultado, el programa lo felicitará, de lo contrario no lo hará.

mayorMenor = input("Dime si el numero será mayor o menor que 5: ") 

numero_aleatorio = random.randint(1, 10)

if numero_aleatorio < 5 and mayorMenor == "menor":
    print(f"¡Ganaste Felicitaciones, el número {numero_aleatorio} es menor a 5!")

elif numero_aleatorio > 5 and mayorMenor == "mayor":
    print(f"¡Ganaste Felicitaciones, el número {numero_aleatorio} es mayor a 5!")

else:
    print(f"¡Perdiste, el número es: {numero_aleatorio} intenta de nuevo!")

