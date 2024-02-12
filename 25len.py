# 'cadena' es una variable de tipo string (cadena de texto).
cadena_string = "¡Hola!, esta es una cadena de texto hecha para medir su longitud con el método len()"
# La función len() retorna la longitud de la cadena de texto.
print(len(cadena_string))  # Salida: número de caracteres en 'cadena'

# 'frutas' es una lista (array ordenado de elementos).
frutas_lista = ["pera", "mango", "fresa"]
# La función len() retorna el número de elementos en la lista.
print(len(frutas_lista))  # Salida: número de elementos en 'frutas'

# 'frutas1' es un conjunto (un conjunto no ordenado de elementos únicos).
frutas1_conjunto = {"pera", "mango", "fresa"}
# La función len() retorna el número de elementos en el conjunto.
print(len(frutas1_conjunto))  # Salida: número de elementos en 'frutas1'

# 'frutas2' es una tupla (una colección ordenada e inmutable de elementos).
frutas2_tupla = ("pera", "mango", "fresa")
# La función len() retorna el número de elementos en la tupla.
print(len(frutas2_tupla))  # Salida: número de elementos en 'frutas2'

# 'fruta3' es un diccionario (una colección de pares clave-valor).
fruta3_diccionario = {
  "fruta": "pera",
  "fruta1": "mango",
  "fruta2": "fresa"
}
# La función len() retorna el número de pares clave-valor en el diccionario.
print(len(fruta3_diccionario))  # Salida: número de pares clave-valor en 'fruta3'

numeros = range(1, 6)
print(len(numeros))  # Salida: número de elementos en 'numeros'