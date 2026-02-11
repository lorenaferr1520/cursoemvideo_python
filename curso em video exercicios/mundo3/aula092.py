# cadastro de trabalhador em python
from datetime import datetime
ano_atual = datetime.now().year
linha = '-=' * 20
pessoa = dict()
print(linha)

pessoa['nome'] = str(input('Nome: '))
anonascimento = int(input('Ano de Nascimento: '))
pessoa['idade'] = ano_atual - anonascimento

ctps = int(input('Carteira de Trabalho (0 não tem): '))
pessoa['ctps'] = ctps
if ctps != 0:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário']= float(input('Salário: R$'))
    pessoa['aposentadoria'] = (pessoa['contratação']) - anonascimento + 35

print(linha)

for k, v in pessoa.items():
    print(f'- {k} tem o valor {v}')
print(linha)