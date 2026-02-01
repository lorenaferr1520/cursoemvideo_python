# catetos e hipotenusas
from math import hypot 

co = float(input("qual o comprimento do cateto oposto: "))
ca = float(input("qual o comprimento do cateto adjacente: "))

hi = (co ** 2 + ca ** 2) ** (1/2)

print(f"A hipotenusa vai medir {hi:.2f}")

input("proxima maneira") # import math
hi = hypot(co, ca)

print(f"A hipotenusa vai medir {hi:.2f}")