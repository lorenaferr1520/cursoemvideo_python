# Valores únicos em uma lista
valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Valor duplicado, não vou adicionar...')
    else:
        print('valor adicionado com sucesso...')
        valores.append(valor)
    
    seguimento = input('Quer continuar? [S/N]').upper()
    if seguimento == 'S':
        continue
    else:
        break
valores.sort()
print('-=-' * 20)
print(f'Você digitou os valores {valores}')
print('-=-' * 20)