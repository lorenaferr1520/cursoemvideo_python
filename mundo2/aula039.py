# alistamento militar
from datetime import date
ano_atual = date.today().year
cores = {
    'limpa': '\033[m',
    'branco': '\033[30m',
    'verde': '\033[1;32m',    # Negrito + Verde
    'vermelho': '\033[1;31m',
}

print(f'{cores['verde']}-=-{cores["limpa"]}' * 18)
print(f'                 {cores["verde"]}ALISTAMENTO MILITAR{cores["limpa"]}')
print(f'{cores['verde']}-=-{cores["limpa"]}' * 18)


ano_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nascimento
idade_alistamento = 18

if idade < idade_alistamento:
    print(f'Quem nasceu em {ano_nascimento} tem {idade} anos de idade em {ano_atual}')
    print(f'{cores["vermelho"]}Seu alistamento será em {(18 - idade) + (ano_atual)} {cores["limpa"]}')

elif idade == 18:
    print(f'Quem nasceu em {ano_nascimento} tem ou completará 18 anos de idade em {ano_atual}')
    print(f'{cores["verde"]}Já está permitido, segundo a lei, realizar seu alistamento{cores["limpa"]}')
    
else:
    print(f'Quem nasceu em {ano_nascimento} tem {idade} anos de idade em {ano_atual}')
    print(f'{cores["vermelho"]}Você já deveria ter se alistado há {idade - 18} anos{cores["limpa"]}')
    print(f'Seu alistamento foi em {ano_atual - (idade - 18)}')
    
print(f'{cores['verde']}-=-{cores["limpa"]}' * 18)