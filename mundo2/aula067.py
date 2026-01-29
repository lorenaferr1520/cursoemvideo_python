# tabuada v3.0
print('-=-' * 14)
print('               TABUADA V3.0')

while True:
    contador = 1
    print('-' * 40)
    tab = int(input('Quer ver a tabuada de qual valor: '))
    print('-' * 40)
    
    if tab < 0:
        break
    
    while contador <= 10:
        print(f'{tab} X {contador} = {tab * contador}')
        contador += 1
        
print('''Fim do programa 
  __
<(o )___
 ( ._> /
  `---'   quak

      ''')
print('-=-' * 18)