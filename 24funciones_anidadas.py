# Definición de la función externa
def externa():
  # Variable local dentro de la función externa
  mensaje = '¡Hola!'

  # Función interna que imprime el mensaje
  def interna():
    print(mensaje)

  # Llamada a la función interna desde la función externa
  interna()

# Llamada a la función externa
externa()

# Separador visual para diferenciar la salida de diferentes bloques de código
print("************************")

# Definición de la función anidada que calcula la suma de los elementos de una lista
def anidada():
  # Lista de números sobre la cual se calculará la suma
  lista = [1,  2,  3,  4,  5]

  # Función interna que realiza la suma de los elementos de la lista
  def suma(lista):
    suma =  0
    # Iteración sobre cada elemento de la lista para sumarlos
    for i in lista:
      suma += i
    # Retorno de la suma calculada
    return suma
   
  # Retorno del resultado de la función interna suma aplicada a la lista
  return suma(lista)

# Almacenamiento del resultado de la función anidada en una variable
resultado = anidada()
# Impresión del resultado obtenido
print(resultado)
