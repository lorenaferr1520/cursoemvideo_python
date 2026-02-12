# cadrastro do jogador
linha = '-=' * 20
jogador = dict()
listagols = list()

jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
num = 1

for gol in range(partidas):
    golsemcada = int(input(f'Quantos gols ele fez na partida {num}°: '))
    num += 1
    listagols.append(golsemcada)

print(linha)
jogador['gols'] = listagols
jogador['total'] = sum(listagols)
print(jogador)
print(linha)

num = 1
print(f'O jogador {jogador["nome"]} jogou em {partidas} partidas: ')
for i in range(partidas):
    print(f'   => Na partida {num}, fez {listagols[i]}')
    num += 1

print(linha)
print('''Fim do programa 
  __
<(o )___
 ( ._> /
  `---'   quak

      ''')