# calculo do fatorial
from math import factorial

num = int(input("digite um número para \ncalcular seu fatorial:"))
f= factorial(num)
c = num

while c >= 1:
    
    print(c, end = ' X ')
    if c == 1:
        print(end= ' ')
    c -= 1


print(f'O fatorial de {num} é {f}')