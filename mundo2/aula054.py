# grupo da maioridade
from datetime import date
ano_atual = date.today().year
maior_idade = 18
maiores = 0
menores = 0

p1 = int(input('Em que ano a primeira pessoa nasceu: '))
p2 = int(input('Em que ano a segunda pessoa nasceu: '))
p3 = int(input('Em que ano a terceira pessoa nasceu: '))
p4 = int(input('Em que ano a quarta pessoa nasceu: '))
p5 = int(input('Em que ano a quinta pessoa nasceu: '))
p6 = int(input('Em que ano a sexta pessoa nasceu: '))
p7 = int(input('Em que ano a sétima pessoa nasceu: '))

lista_de_nascimentos = [p1, p2, p3, p4, p5, p6, p7 ]

print(lista_de_nascimentos)

for ano_n in lista_de_nascimentos:
    
    if (ano_atual - ano_n) >= 18:
        maiores += 1
    else:
        menores += 1

print(f'Ao todo tivemos {maiores} pessoas maiores de idade \nE {menores} pessoas menores de idade')