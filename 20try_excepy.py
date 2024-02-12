"""
try:
  numero = int(input("Ingresa un número: "))
  print(f"El número ingresado es {numero}")
except ValueError:
  print("Por favor ingrese un número valido")
"""
"""
try:
  x = 5 / 0
except ZeroDivisionError:
  print("No puedes dividir númeeros etntre ceros, por favor intenta de nuevo...")
"""

try:
  numero1 = int(input("Ingresa el primer numero de la división: "))
  numero2 = int(input("Ingresa el segundo numero de la división: "))
  resultado = numero1 / numero2
  print(f"El resultado de la división es: {resultado}")

except ValueError:
    print("Por favor ingrese un número valido")

except ZeroDivisionError:
    print("No puedes dividir númeeros etntre ceros, por favor intenta de nuevo...") 
