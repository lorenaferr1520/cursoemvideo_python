# jogo do par ou impar
from random import randint
from time import sleep
cores = {
    'limpa': '\033[m',
    'vermelho': '\033[1;31m', # Negrito + Vermelho
    'verde': '\033[1;32m',    # Negrito + Verde
    'amarelo': '\033[1;33m',   # Negrito + Amarelo
    'azul': '\033[1;34m',      # Negrito + Azul
    'ciano': '\033[1;36m',     # Negrito + Ciano
    'cinza': '\033[37m',

}

print(f'{cores["verde"]}-=-{cores["limpa"]}' * 14)
print('          JOGO DO PAR OU IMPAR')
print(f'{cores["verde"]}-=-{cores["limpa"]}' * 14)
vitorias = 0
 
while True:
    computador = randint(0, 10)
    usuario = int(input('Digite um valor: '))
    escolha = input('Par ou impar? [P/I]').upper()
    total = computador + usuario 
    par = total % 2 == 0
   
    if escolha != 'P' and escolha != 'I':
        print(f'{cores["vermelho"]}Escolha inválida! apenas par [P] ou impar [I]{cores["limpa"]}')
        print(f'{cores["vermelho"]}Encerrando programa...{cores["limpa"]}')
        print(f'{cores["vermelho"]}3..{cores["limpa"]}')
        sleep(1.0)
        print(f'{cores["vermelho"]}2..{cores["limpa"]}')
        sleep(1.0)
        print(f'{cores["vermelho"]}1..{cores["limpa"]}')
        sleep(1.0)
        break
    
    print(f'Você jogou {usuario} o computador jogou {computador}, total de {total}')
    
    if total == par:
        if escolha == 'P':
            print(f'{cores["verde"]}Usuário ganhou!{cores["limpa"]}')
            vitorias += 1
        else:
            print(f'{cores["vermelho"]}Computador ganhou!{cores["limpa"]}')
            break
    elif total != par:
        if escolha == 'I':
            print(f'{cores["verde"]}Usuário ganhou!{cores["limpa"]}')
            vitorias += 1
        else:
            print(f'{cores["vermelho"]}Computador ganhou!{cores["limpa"]}')
            break
        
print(f'{cores["verde"]}-=-{cores["limpa"]}' * 14)
print(f'{cores["ciano"]}Total de vitórias: {vitorias}{cores["limpa"]}')
print(f'{cores["verde"]}-=-{cores["limpa"]}' * 14)

print(f'''{cores["amarelo"]}Fim do programa 
  __
<(o )___
 ( ._> /
  `---'   quak

     {cores["limpa"]} ''')

    
    