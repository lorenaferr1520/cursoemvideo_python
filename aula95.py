# aprimorando dicionarios python
linha = '-=' * 20
time = list() 
jogador = dict()
listagols = list()

while True:
    jogador.clear()
    listagols.clear() 
    
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    
    for c in range(0, partidas):
        listagols.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
    
    jogador['gols'] = listagols[:] 
    jogador['total'] = sum(listagols)
    time.append(jogador.copy()) 
    
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print(linha)
print(f'{"cod":<3} {"nome":<15} {"gols":<15} {"total":<5}')
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} {v["nome"]:<15} {str(v["gols"]):<15} {v["total"]:<5}')
print(linha)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 40)

print('''Fim do programa 
  __
<(o )___
 ( ._> /
  `---'   quak''')
    


