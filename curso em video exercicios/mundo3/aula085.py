# Criando a lista principal com as duas sublistas vazias dentro
num = [[], []]

print('-' * 20)
print('  LISTA PAR E ÍMPAR  ')
print('-' * 20)

for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    

    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print('-' * 30)

num[0].sort()
num[1].sort()

print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')