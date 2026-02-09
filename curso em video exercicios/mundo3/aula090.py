# dicionário python
linha = '-=' * 20

print(linha)
print('            DICIONÁRIO NOTA')
print(linha)
nome = str(input('Nome: '))
média = float(input(f'Média de {nome}: '))
print(linha)
aluno = {}
aluno['nome'] = nome
aluno['média'] = média
print(aluno)

if média >= 7:
    aluno['situação'] = 'Aprovado(a)'
elif 5 <= média < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado(a)'

print(f'- nome é igual a {aluno['nome']}')
print(f'- Média é igual a {aluno['média']}')
print(f'- Situação é igual a {aluno['situação']}')

print(linha)
print('''Fim do programa 
  __
<(o )___
 ( ._> /
  `---'   quak

      ''')