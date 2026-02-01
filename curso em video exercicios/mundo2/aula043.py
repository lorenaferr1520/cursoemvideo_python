# IMC
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
Abaixo de 18.5	Abaixo do Peso
Entre 18.5 e 25	Peso Ideal
25 até 30	Sobrepeso
30 até 40	Obesidade
Acima de 40	Obesidade Mórbid
'''
print(f'{cores["amarelo"]}-=-{cores["limpa"]}' * 18) 
print(f'                   {cores["azul"]}CALCULANDO IMC{cores["limpa"]}')
print(f'{cores["amarelo"]}-=-{cores["limpa"]}' * 18) 

peso = float(input('Qual é o seu peso em KG: '))
altura = float(input('Qual a sua altura em metros: '))
imc = peso / (altura ** 2)
print(f'Seu IMC é de {imc:.2f}')

if imc <= 18.5:
    print(f'Cuidado! Você está {cores["amarelo"]}ABAIXO DO PESO{cores["limpa"]}')
    ganhar = (18.5 * (altura ** 2)) - peso # calculando quanto falta
    print(f'Você precisa ganhar pelo menos {ganhar:.1f}kg para chegar ao peso ideal.')

elif imc > 18.5 and imc <= 25:
    print(f'Você está no seu {cores["verde"]}PESO IDEAL{cores["limpa"]}')

elif imc > 25 and imc <= 30:
    peso_alvo = 25 * (altura ** 2)
    print(f'Você está com {cores["amarelo"]}SOBREPESO{cores["limpa"]}')
    print(f'Para chegar ao peso ideal, você deveria pesar {peso_alvo:.1f}kg.') # calculo de perda de peso

elif imc > 30 and imc <= 40:
    print(f'Cuidado! Você está com {cores["vermelho"]}OBESSIDADE{cores["limpa"]}')
    peso_alvo = 25 * (altura ** 2)
    print(f'Para chegar ao peso ideal, você deveria pesar {peso_alvo:.1f}kg.') # calculo de perda de peso

else:
    print(f'Cuidado! Você está com {cores["vermelho"]}OBESIDADE MORBIDA{cores["limpa"]}')
    peso_alvo = 25 * (altura ** 2)
    print(f'Para chegar ao peso ideal, você deveria pesar {peso_alvo:.1f}kg.') # calculo de perda de peso

print(f'{cores["amarelo"]}-=-{cores["limpa"]}' * 18)