# sorteando uma ordem na lista
from random import shuffle

aluno1 = input("digite o nome do primeiro aluno: ")
aluno2 = input("digite o nome do segundo aluno: ")
aluno3 = input("digite o nome do terceiro aluno: ")
aluno4 = input("digite o nome do quarto aluno: ")
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista_alunos)

print("A ordem de apresentação será: ")
print(lista_alunos)