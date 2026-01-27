# jogo da advinhação V2.0
import random
numero_da_maquina = random.randint(0, 10)
cores = {
    'verde': '\033[1;32m',
    'limpa': '\033[m', 
}

print(f'{cores["verde"]}-=-{cores["limpa"]}' * 18)
print(f'             {cores["verde"]}JOGO DA ADVINHAÇÃO V2.0{cores["limpa"]}')
print(f'{cores["verde"]}-=-{cores["limpa"]}' * 18)

print('Sou seu computador...')
print( f'''{cores["verde"]}
     _________________
    |  _____________  |
    | | Python      | |
    | |    Rules!   | |
    | |_____________| |
    |_________________|
           |___|       
          /_____\\      {cores["limpa"]}
''')
print('Acabei de pensar em um número aleatório entre 0 a 10')
print('Será que você consegue advinhar qual foi?')
usuario = int(input('Seu Palpite: '))

while usuario != numero_da_maquina:
    print('Resposta errada! Tente novamente')
    usuario = int(input('Seu Palpite: '))
    
print(f'Você acertou! o número era o {numero_da_maquina}')
print('FIM')
print(f'{cores["verde"]}-=-{cores["limpa"]}' * 18)