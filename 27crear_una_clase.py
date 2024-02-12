class Persona: 
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def saludar(self):
    print(f"Mi nombre es {self.nombre} y tengo {self.edad} años.")

persona = Persona("Juan", 20)
persona.saludar()

persona2 = Persona("Maria", 25)
persona2.saludar()

"""
Crear una clase llamada libro con los atributos titulo, autor; agrega un 
metodo llamado mostrar informacion que imprima el titulo y el autor del libro.
"""
print("***********************************************")

class Libro:
  def __init__(self, titulo, autor):
    self.titulo = titulo
    self.autor = autor
  def mostrar(self):
    print(f"El libro {self.titulo} fue escrito por {self.autor}.")

libro = Libro("La Busqueda", "Alfonzo Lara Castilla") 
libro.mostrar()

libro1 = Libro("La Odisea", "Homero")
libro1.mostrar()
