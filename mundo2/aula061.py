# progreção aritmética
print('-=-' * 20)
print('                 PROGREÇÃO ARTMÉTICA V2.0')
print('-=-' * 20)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
contador = 1

while contador <= 10:
    print(f'{termo} --> ', end= '')
    termo += razao
    contador += 1
    
print('FIM')
