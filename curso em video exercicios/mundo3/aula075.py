# analise de dados

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o ultimo número: '))
pares = 0

iguais = 0
numeros = (num1, num2, num3, num4)
print(f'Você digitou os valores {numeros}')

for i in numeros:
    if i % 2 == 0:
        pares += 1



print(f'O valor {num2} apareceu na segunda posição')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
print(f'Os valores pares foram {pares}')
