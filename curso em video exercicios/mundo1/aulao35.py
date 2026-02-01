# analisando o triangulo
print('-=-' * 15)
print('ANALISADOR DE TRIÂNGULO')
print('-=-' * 15)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Os seguimentos acima PODEM FORMAR um triângulo!')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triângulo!')

print('-=-' * 15)
    
