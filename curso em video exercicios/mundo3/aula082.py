# dividindo valores em listas
lista = []
pares = []
impares = []
print('-=-' * 20)
print('                LISTA DE PARES E IMPARES')
print('-=-' * 20)
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    
    resposta = input('Quer continuar? [S/N]: ').upper()
    if resposta == 'S':
        continue
    else:
        break

print('-=-' * 20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
print('-=-' * 20)