def ficha(nome="<desconhecido>", gols=0):
    print('-' * 30)
    nome = input('Nome do Jogador: ')
    if nome == '':
        nome = '<desconhecido>'

    while True:

        gols = (input('Numeros de gols: '))
        
        if gols == "":
            gols = 0
            break
        elif gols.isdigit():
            break
        else:
            print('Apenas números inteiros')
            continue
      
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')

ficha()