# cores no terminal (básico)
''' ansi - escape sequence (código: \033[m) entre o colchete e o m add código da cor
--> [style;text;backm --> [0;33;44m

 style --> 0(nome) 1(bold) 4(underline) 7(negative)
 
 text --> 30 branco, 31 vermelho, 32 verde, 33 amarelo,
 34 zul, 35 roxo, 36 azul claro, 37 cinza
 
 backgroud --> 40 branco, 41 vermelho, 42 verde, 43 amarelo,
 44 zul, 45 roxo, 46 azul claro, 47 cinza
 
'''
# teste:
print('\033[31mOlá, Mundo!') # vermelho

print('\033[31;43mOlá, Mundo!\033[m') # fundo amarelo

print('\033[1;31mOlá, Mundo!') # negrito

print('\033[7;30mOlá, Mundo!')

# use lista de cores e coloque com format