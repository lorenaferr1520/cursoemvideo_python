print('-' * 20)
print('VALIDADOR DE EXPRESSÕES')
print('-' * 20)

expr = str(input('Digite a expressão: '))
pilha = []

for caractere in expr:
    if caractere == '(':
        pilha.append('(')
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop() 
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

