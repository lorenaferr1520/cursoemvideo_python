# classificando atletas
from datetime import date
ano_atual = date.today().year
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

mirim = 9
infantil = 14
junior = 19
senior = 25
master = 26 # acima de 25

print('-=-=-=-=-=-=-=- CLASSIFICANDO ATLETAS -=-=-=-=-=-=-=-')

ano_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nascimento

if idade <= mirim :
    print(f'O atleta tem {idade} anos. \nClassificação: {cores["amarelo"]}MIRIM{cores["limpa"]}')

elif idade <= infantil:
    print(f'O atleta tem {idade} anos. \nClassificação: {cores["ciano"]}INFANTIL{cores["limpa"]}')

elif idade <= junior:
    print(f'O atleta tem {idade} anos. \nClassificação: {cores["azul"]}JUNIOR{cores["limpa"]}')

elif idade <= senior:
    print(f'O atleta tem {idade} anos. \nClassificação: {cores["vermelho"]}SENIOR{cores["limpa"]}')

else:
    print(f'O atleta tem {idade} anos. \nClassificação: {cores["sublinhado"]}MASTER{cores["limpa"]}')
    
print('-=-' * 18)