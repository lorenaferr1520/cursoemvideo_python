opcao = 0
print('=' * 28)
print('         CALCULANDO')
print('=' * 28)

while opcao != 5: # 5 seria a opção para 'Sair'
    p1 = int(input('Primeiro valor: '))
    p2 = int(input('Segundo valor: '))

    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('>>>> Qual é a sua opção? '))
    
    if opcao == 1:
        print(f'{p1} + {p2} é igual a {p1 + p2}')
        
    elif opcao == 2:
        print(f'{p1} X {p2} é igual a {p1 * p2}')
            
    elif opcao == 3:
        if p1 > p2:
            print(f'O número {p1} é maior que o {p2}!')
        else:
            print(f'O número {p2} é maior que o {p1}!')
    
    elif opcao == 4:
        print('Digite o número novamente')
        continue
        

    print('=' * 28)       
        
print('''Fim do programa 
  __
<(o )___
 ( ._> /
  `---'   quak

      ''')
    
