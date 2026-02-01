# média 
cores = {
    'limpa': '\033[m',
    'branco': '\033[30m',
    'vermelho': '\033[1;31m', # Negrito + Vermelho
    'verde': '\033[1;32m',    # Negrito + Verde
    'amarelo': '\033[1;33m',   # Negrito + Amarelo
    'azul': '\033[1;34m',      # Negrito + Azul
    'roxo': '\033[1;35m',      # Negrito + Roxo
    'ciano': '\033[1;36m',     # Negrito + Ciano
    'cinza': '\033[37m',
    'sublinhado': '\033[4m'
}
''' 
abaixo de 5.0 = reprovado
entre 5.0 e 6.9 = recuperação
acima de 7 = aprovado
'''
print(f'{cores["amarelo"]}-=- {cores["limpa"]}' * 18)
print(f'                           {cores["ciano"]} MÉDIA ESCOLAR {cores["limpa"]}')
print(f'{cores["amarelo"]}-=- {cores["limpa"]}' * 18)

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'Tirando {nota1} e {nota2} a média do aluno é {media}')
    print(f'O aluno está {cores["vermelho"]}REPROVADO{cores["limpa"]}')

elif media > 6.9:
    print(f'Tirando {nota1} e {nota2} a média do aluno é {media}')
    print(f'O aluno está {cores["verde"]}APROVADO{cores["limpa"]}')

else:
    print(f'Tirando {nota1} e {nota2} a média do aluno é {media}')
    print(f'O aluno está de {cores["vermelho"]}RECUPERAÇÃO{cores["limpa"]}')

print(f'{cores["amarelo"]}-=- {cores["limpa"]}' * 18)
