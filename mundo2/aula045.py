# Pedra Papel e Tesoura
cores = {
    'limpa': '\033[m',
    'branco': '\033[30m',
    'vermelho': '\033[1;31m', # Negrito + Vermelho
    'verde': '\033[1;32m',    # Negrito + Verde
    'amarelo': '\033[1;33m',   # Negrito + Amarelo
    'azul': '\033[1;34m',      # Negrito + Azul
    'roxo': '\033[1;35m',      # Negrito + Roxo
    'ciano': '\033[1;36m',     # Negrito + Ciano
    'cinza': '\033[37m',
    'sublinhado': '\033[4m'
}
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
escolha_computador = itens[computador]
print('-=-=-=-=-=-=-=-=-=- PEDRA, PAPEL E TESOURA -=-=-=-=-=-=-=-=-')
usuario = int(input('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA           
'''))
escolha_usuário = itens[usuario]

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=-' * 20)
print(f'O computador jogou {escolha_computador}')
print(f'O usuário jogou {escolha_usuário}')
print('-=-' * 20)

if computador == 0:
    if usuario == 0:
        print(f'{cores["amarelo"]}DEU EMPATE!{cores["limpa"]}')
    elif usuario == 1:
        print(f'{cores["verde"]}O USUÁRIO GANHOU!{cores["limpa"]}')
    elif usuario == 2:
        print(f'{cores["vermelho"]}O COMPUTADOR GANHOU!{cores["limpa"]}')

elif computador == 1:
    if usuario == 0:
        (f'{cores["vermelho"]}O COMPUTADOR GANHOU!{cores["limpa"]}')
    elif usuario == 1:
        print(f'{cores["amarelo"]}DEU EMPATE!{cores["limpa"]}')
    elif usuario == 2:
        print(f'{cores["verde"]}O USUÁRIO GANHOU!{cores["limpa"]}')

else:
    if usuario == 0:
        print(f'{cores["verde"]}O USUÁRIO GANHOU!{cores["limpa"]}')
    elif usuario == 1:
        (f'{cores["vermelho"]}O COMPUTADOR GANHOU!{cores["limpa"]}')
    elif usuario == 2:
        print(f'{cores["amarelo"]}DEU EMPATE!{cores["limpa"]}')