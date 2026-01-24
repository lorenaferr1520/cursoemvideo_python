# comparando números
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
print(f'{cores["vermelho"]}-=-{cores["limpa"]}' * 18)
print(f'                 {cores["azul"]}COMPARANDO NÚMEROS{cores["limpa"]}')
print(f'{cores["vermelho"]}-=-{cores["limpa"]}' * 18)

# input dos números
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

# verificação e print
if num1 > num2:
    print(f'O {cores["azul"]}PRIMEIRO valor é maior{cores["limpa"]}')
elif num1 == num2:
    print(f'Os dois valores são {cores["azul"]}IGUAIS{cores["limpa"]}')
else:
    print(f'O {cores["azul"]}SEGUNDO{cores["limpa"]} valor é maior')

print(f'{cores["vermelho"]}-=-{cores["limpa"]}' * 18)