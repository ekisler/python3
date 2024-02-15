import time
"""
print("Dime lo que sea...")
anything = input()
print("Hmm...", anything, "... ¿en serio?")

# Podemos usar el input() directamente sin el print()
anything = input("Dime lo que sea...")
print("Humm...", anything, "... ¿en serio?")

introduceDatos = input("Escribe lo que quieras y veraz la respuesta de la computadora:")
print(f"De acuerdo, has escrito: {introduceDatos}, gracias por colaborar!")

print("+" + 30 * "-" + "+")
print(("|" + " " * 30 + "|\n") * 5, end="")
print("+" + 30 * "-" + "+")

# Fracción continua o infinita
x = float(input("Ingresa el valor para x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)


# Calcular duracion de eventos en horas
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aquí.

# Sumamos la duración a la hora de inicio para obtener los minutos totales
total_minutes = mins + dura
print(f"total_minutes {total_minutes}")

# Convertimos los minutos totales a horas y minutos
final_hour = total_minutes // 60 # División entera para obtener las horas
print(f"final_hour {final_hour}")

remaining_mins = total_minutes % 60 # Módulo para obtener los minutos restantes
print(f"remaining_mins {remaining_mins}")

# Sumamos las horas de inicio al calculo de horas finales y calculamos el módulo de 24 para obtener la hora correcta
final_hour = (hour + final_hour) % 24
print(f"final_hour {final_hour}")

# Imprimimos la hora y los minutos finales
print("El evento termina a las ", final_hour, ":", remaining_mins, sep="")

x = int(input("Ingresa un número: ")) # El usuario ingresa un 2
print(x * "5")

x = input("Ingresa un número: ") # El usuario ingresa un 2
print(type(x))

n = int(input("Ingresa un número: "))

print(n > 100)

number1 = float(input("Ingresa el primer número: "))
number2 = float(input("Ingresa el segundo número:"))

# Elegimos el n{umero más grande

if number1 > number2:
  large_number = number1
else:
  large_number = number2

print("El número más grande es: ", large_number)

number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

largest_number = number1

if number2 > largest_number:
  largest_number = number2

if number3 > largest_number:
    largest_number = number3

print("El número más grande es: ", largest_number)

largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Ir a la línea 02

number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))
 
# Verifica cuál de los números es el mayor
# y pásalo a la variable largest_number.
 
largest_number = max(number1, number2, number3)
 
# Imprime el resultado.
print("El número más grande es:", largest_number)

planta = input("Ingresa el nombre de tu planta preferida: ")

if planta == "Espatifilo":
  print("Si - ¡El Espatifilo es la mejor planta de todos los tiempos!")
elif planta == "ESPATIFILO":
  print("No, ¡quiero un gran Espatifilo!")
elif planta == "espatifilo":
    print(f"¡Espatifilo!, ¡No {planta}!")
else:
   print(f"¡Espatifilo! ¡No {planta}!")


income = float(input("Introduce el ingreso anual: "))

if income < 85528:
	tax = income * 0.18 - 556.02
# Escribe tu código aquí.

elif income > 85528:
    exceso = income - 85528
    tax = 18839.02 + exceso * 0.32
    
if tax < 0:
    tax = 0

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")

year = int(input("Introduce un año: "))

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
	if year % 4 != 0:
		print("Año Común")
	elif year % 100 != 0:
		print("Año Bisiesto")
	elif year % 400 != 0:
		print("Año Común")
	else:
		print("Año Bisiesto")
 
x = 5
y = 10
z = 8

print(x > y)
print(y > z)

x, y, z = 5, 10, 8
x, y, z = y, z, x

print(x > z)
print((y - 5) == x)

# Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande.
print("El número más grande es:", largest_number)

counter = 5
while counter != 0:
  print(f"Dentro del bucle {counter}")
  counter -= 1
print(f"Fuera del bucle {counter}")

print("******************************")

contador = 1
while contador != 5:
  print(f"Dentro del bulce {contador}")
  contador +=1
print(f"Fuera del bucle {contador}")

for i in range(1,11):
  print("El valor de i es:", i)
  
class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')

q.party()
m.party()
q.party()

import time

for i in range(1, 6):
    print(f"{i} Mississippi")
    time.sleep(1)
    
# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# Ingresa la palabra secreta para salir del bucle
while True:
    palabra = input("Ingresa una palabra: ")
    if palabra == "chupacabra":
        break
    else:
        print("Volvamos")
print("Has dejado el bucle con éxito.")

# Indicar al usuario que ingrese una palabra
palabra = input("Ingresa una palabra: ")
# y asignarlo a la variable user_word.
user_word = palabra
# Ingresa la palabra secreta para salir del bucle

for letter in user_word:
    # Completa el cuerpo del bucle for.

    if letter == "a":
        continue
    elif letter == "e":
        continue
    elif letter == "i":
        continue
    elif letter == "o":
        continue
    elif letter == "u":
        continue
    else:
        print(letter.upper())
  

# Calculo de bloques de una piramide
blocks = int(input("Ingresa el número de bloques: "))

#
# Escribe tu código aquí.
#	
height = 0

while blocks > 0:
# Calculamos cuantos bloques necesitamos para el proximo tramo
    cargando_bloques = height + 1
# Verificamos si tenemos bloques para el proximo tramo    
    if blocks >= cargando_bloques:
# Si es así, incrementamos la altura y restamos los bloques utilizados
        height += 1
        blocks -= cargando_bloques
    else:
# Si no hay suficientes bloques, salimos del bucle
        break
    
print("La altura de la pirámide:", height)

def collatz(c0):
    steps =  0
    while c0 !=  1:
        print(c0)
        if c0 %  2 ==  0:
            c0 = c0 //  2
        else:
            c0 =  3 * c0 +  1
        steps +=  1
    print(1)
    return steps

# Solicita al usuario que ingrese un número
c0 = int(input("Ingresa el número inicial: "))
steps = collatz(c0)
print(f"pasos = {steps}.")

# Imprimir solo numeros pares e impares con un bucle for
for i in range(0, 11):
  if i % 2 != 0:
    print(i)

print("******************************")

for j in range(0, 11):
  if j % 2 == 0:
    print(j)

x = 1
while x < 11:
  if x % 2 != 0:    
    print(x)
  x += 1  
  
flag_register = 0x1234
print(f"flag_register = {flag_register}")


x = 1
y = 0
z = ((x == y) and (x == y) or not(x == y))
print(not(z))

x = 4
y = 1
 
a = x & y
b = x | y
c = ~x  # ¡difícil!
d = x ^ 5
e = x >> 2
f = x << 2
 
print(a, b, c, d, e, f)


numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista: ", numeros)

numeros [0] = 111
print("Nuevo contenido de la lista con cambio: ", numeros)

numeros[1] = numeros[4]
print("Contenido de la lista con intercambio: ", numeros)

print("\nLongitud de la lista: ", len(numeros))

del numeros[1]
print("Longitud de la mueva lista", len(numeros))
print("Nuevo contenido de la lista: ", numeros)

hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
numero = int(input("Ingresa un número: "))
hat_list[2] = numero

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[-1]

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.

print("\n", hat_list, len(hat_list))

my_list = [10, 1, 8, 3, 5]
total = 0
for i in my_list:
  total += i

print(total)
"""
