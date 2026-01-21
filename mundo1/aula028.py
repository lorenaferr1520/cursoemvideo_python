# jogo da advinhação 
from random import randint
from time import sleep

print('-=-=-=-=-=-=- JOGO DA ADVINHAÇÃO -=-=-=-=-=-=-')
computador = randint(0,5) # computador escolhe um número
num = int(input("Advinhe qual número escolhi de 0 a 5: "))
  
print('Processando...')
sleep(3)

if num == computador:
    print(f'Você acertou!!!, o número é {computador}')
elif num > 5:
    print('opção inválida! apenas números de 0 a 5')
else:
    print(f'Resposta incorreta! meu número escolhido foi {computador}')

print('-=-' * 15)
