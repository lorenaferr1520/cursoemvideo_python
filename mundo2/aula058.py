# jogo da advinhação V2.0
from random import randint
numero_da_maquina = randint(0, 10)
cores = {
    'verde': '\033[1;32m',
    'limpa': '\033[m', 
}
tentativas = 1

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
    if usuario < numero_da_maquina:
        print('Mais... Tente novamente!')
    else:
        print('Menos... Tente novamente!')
    usuario = int(input('Seu Palpite: '))
    tentativas += 1

if tentativas == 1:
    print(f'Parabens! Você acertou na PRIMEIRA tentativa, o número era o {numero_da_maquina}')
else:
    print(f'Você acertou em {tentativas} tentativas! o número era o {numero_da_maquina}')
print(print('''Fim do programa 
  __
<(o )___
 ( ._> /
  `---'   quak

      '''))
print(f'{cores["verde"]}-=-{cores["limpa"]}' * 18)