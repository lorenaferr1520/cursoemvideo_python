# conversor de bases númericas 
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
print(f'             {cores["azul"]}CONVERSOR DE BASES NÚMERICAS{cores["limpa"]}')
print(f'{cores["vermelho"]}-=-{cores["limpa"]}' * 18)

num = int(input('Digite um número inteiro: '))
opção = int(input('Escolha uma das bases para conversão:\n[1] converter para BINÁRIO\n[2] converter para OCTAL\n[3] converter para HEXADECIMAL\nResposta: '))

if opção == 1:
    print(f'{num} convertido para BINÁRIO é igual a {cores["verde"]}{bin(num)[2:]}{cores["limpa"]}')
    
elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a {cores["verde"]}{oct(num)[2:]}{cores["limpa"]}')
    
elif opção == 3:
    print(f'o {num} convertido para HEXADECIMAL é igual a {cores["verde"]}{hex(num)[2:]}{cores["limpa"]}')

else:
    print(f'{cores["vermelho"]}Opção inválida. Tente novamente.{cores["verde"]}{cores["limpa"]}{cores["limpa"]}')

print(f'{cores["vermelho"]}-=-{cores["limpa"]}' * 18)