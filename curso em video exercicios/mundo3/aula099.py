# função que descobre o maior
from time import sleep

def maior(* num):
    print('-=' * 20)
    print('Analisando os valores passados...')
    
    maior_valor = cont = 0
    
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        # Lógica para descobrir o maior
        if cont == 0:
            maior_valor = valor
        else:
            if valor > maior_valor:
                maior_valor = valor
        cont += 1
        
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior_valor}.')

# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior() 