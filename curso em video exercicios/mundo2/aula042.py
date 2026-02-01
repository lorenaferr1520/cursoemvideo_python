# analisando triangulos APRIMORADO
cores = {
    'limpa': '\033[m',
    'vermelho': '\033[1;31m', # Negrito + Vermelho
    'verde': '\033[1;32m',    # Negrito + Verde
    'amarelo': '\033[1;33m',   # Negrito + Amarelo
    'azul': '\033[1;34m',      # Negrito + Azul
    'ciano': '\033[1;36m',     # Negrito + Ciano
    'sublinhado': '\033[4m'
}
'''
equilatero = todos os lados iguais
isósceles = dois lados iguais
escaleno = todos os lados diferentes
'''
print(f'{cores["amarelo"]}-=-{cores["limpa"]}' * 18)
print(f'               {cores["azul"]}ANALISADOR DE TRIÂNGULOS{cores["limpa"]}')
print(f'{cores["amarelo"]}-=-{cores["limpa"]}' * 18)
r1= float(input('Primeiro seguimento: '))
r2= float(input('Segundo seguimento: '))
r3= float(input('Terceiro seguimento: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    
    if r1 == r2 and r2 == r3:
        print(f'Os seguimentos acima {cores["verde"]}PODEM{cores["limpa"]} formar um triangulo {cores["sublinhado"]}EQUILÁTERO{cores["limpa"]}')
        
    elif (r1 == r2) and (r2 != r3) or (r1 != r2) and (r2 == r3) or (r1 == r3) and (r3 != r2):
        print(f'Os segumentos acima {cores["verde"]}PODEM{cores["limpa"]} formar um triângulo {cores["sublinhado"]}ISÓSCELES{cores["limpa"]} ')
    
    else:
        print(f'Os seguimentos acima {cores["verde"]}PODEM{cores["limpa"]} formar um triangulo {cores["sublinhado"]}ESCALENO{cores["limpa"]}')

else:
    print(f'Os seguimentos acima {cores["vermelho"]}NÃO PODEM{cores["limpa"]} formar um triangulo')

print(f'{cores["amarelo"]}-=-{cores["limpa"]}' * 18)