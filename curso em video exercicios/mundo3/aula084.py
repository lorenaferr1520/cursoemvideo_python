# Lista composta e análise de dados
temp = []
principal = []
maior = 0
menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temp[1]
    if temp[1] > maior:
        maior = temp[1]
    if temp[1] < menor:
        menor = temp[1]
    
    principal.append(temp[:]) # Cópia do temporario
    temp.clear()
    
    resposta = str(input('Quer continuar? [S/N]: ')).upper()
    if resposta == 'N':
        break

print('-=-' * 20)   
print(f'Ao todo você cadrastou {len(principal)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]}', end='')
print()
print('-=-' * 20)