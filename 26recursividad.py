def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
  
print(factorial(5))
# 1 x 2 x 3 x 4 x 5 = 120

print("*****************")

def suma_de_naturales(n):
  if n == 1:
    return 1
  else:
    return n + suma_de_naturales(n-1)

print(suma_de_naturales(4))  
# 1 + 2 + 3 + 4 = 10

