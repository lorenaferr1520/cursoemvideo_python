# sorteando uma lista
from random import choice
aluno1 = input("digite o nome do primeiro aluno: ")
aluno2 = input("digite o nome do segundo aluno: ")
aluno3 = input("digite o nome do terceiro aluno: ")
aluno4 = input("digite o nome do quarto aluno: ")

lista_alunos = [aluno1, aluno2, aluno3, aluno4]
print(lista_alunos)

sorteado = choice(lista_alunos)
print(f"o aluno(a) escolhido foi {sorteado}")