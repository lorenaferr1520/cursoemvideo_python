from random import randint
from time import sleep

print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)

quant = int(input('Quantos jogos você quer que eu sorteie? '))
jogos = [] 
dados = [] 

print(f'-=-=-= SORTEANDO {quant} JOGOS =-=-=-')

for c in range(0, quant):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in dados:
            dados.append(num)
            cont += 1
        if cont >= 6:
            break
            
    dados.sort()
    jogos.append(dados[:]) 
    dados.clear()


for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1) 

print('-=' * 5, '< BOA SORTE! >', '=-' * 5)