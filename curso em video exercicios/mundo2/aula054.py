# grupo da maioridade
from datetime import date
ano_atual = date.today().year
maior_idade = 18
maiores = 0
menores = 0

lista_de_nascimentos = []
for p in range(1, 8):
    lista_de_nascimentos.append(int(input(f'Em que ano a {p}ª pessoa nasceu: ')))

print(lista_de_nascimentos)

for ano_n in lista_de_nascimentos:
    
    if (ano_atual - ano_n) >= 18:
        maiores += 1
    else:
        menores += 1

print(f'Ao todo tivemos {maiores} pessoas maiores de idade \nE {menores} pessoas menores de idade')