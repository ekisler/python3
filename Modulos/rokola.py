import random
class Rocola:
  def __init__(self):
    self.temas = [
      "Escaleras al Cielo",
      "Un ladrillo en la pared",
      "No ha parado de llover",
      "En el muelle de San Blas",
      "Amor y control",
      "Desapariciones",
      "Maestra vida",
      "Paula C"
    ]
    self.queue = []

  def play(self, k):
    if len(self.queue) >= k:
      primero = self.queue.pop(0)
      self.temas.append(primero)
    indiceRandom = random.randint(0, len(self.temas) - 1)
    tema = self.temas.pop(indiceRandom)
    self.queue.append(tema)
    return tema
  
rocola = Rocola()
print(rocola.play(4), rocola.queue)
print(rocola.play(4), rocola.queue)
print(rocola.play(4), rocola.queue)
print(rocola.play(4), rocola.queue)
print(rocola.play(4), rocola.queue)
print(rocola.play(4), rocola.queue)
print(rocola.play(4), rocola.queue)
print(rocola.play(4), rocola.queue)