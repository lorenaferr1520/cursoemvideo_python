# tabuada v2
cores = {
    'limpa': '\033[m',
    'verde': '\033[1;32m',    # Negrito + Verde
    'amarelo': '\033[1;33m',   # Negrito + Amarelo
    'azul': '\033[1;34m',      # Negrito + Azul
}

print(f'{cores["verde"]}-=-{cores["limpa"]}' * 18)
print(f'{cores["verde"]}                     TABUADA 2.0 {cores["limpa"]}')
print(f'{cores["verde"]}-=-{cores["limpa"]}' * 18)

num = int(input('Digite um número para ver sua tabuada: '))

for n in range(1, 11):
    print(f'{cores["azul"]}{n} X {num} = {n * num}{cores["limpa"]}')
print(f'{cores["verde"]}-=-{cores["limpa"]}' * 18)