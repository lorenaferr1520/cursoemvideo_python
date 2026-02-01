from random import randint
numeros = ()
contador = 10

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), 
           randint(1, 10), randint(1, 10))

print('Os valores sorteados foram: ')

for i in numeros:
    print(i, end=' ')

print(f'\nO maior número sorteado foi o {max(numeros)}')
print(f'O menor número sorteado foi o {min(numeros)}')

print('''Fim do programa 
  __
<(o )___
 ( ._> /
  `---'   quak

      ''')