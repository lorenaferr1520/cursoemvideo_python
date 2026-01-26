# números primos 

numero = int(input('Digite um número: '))
tot = 0 # contador de números divisiveis

for i in range(1, numero + 1):
    if numero % i == 0:
        print('\033[33m', end= ' ')
        tot +=1
    else:
        print('\033[31m', end= ' ')
        
    print(i, end=' ')
print(f'\033[mO número {numero} foi divisível {tot} vezes')

if tot == 2:
    print('\033[32mÉ um número PRIMO!\033[m')
else:
    print('\033[31mNÃO é um número PRIMO!\033[m')

