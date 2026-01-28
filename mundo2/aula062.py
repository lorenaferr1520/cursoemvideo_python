# super progreção artmética

print('-=-' * 20)
print('              SUPER PROGREÇÃO ARTMÉTICA V3.0')
print('-=-' * 20)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
contador = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo} --> ', end= '')
        termo += razao
        contador += 1
        
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print('FIM')
