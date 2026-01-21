# calcular preço da passagem por distancia

distancia = float(input('Qual a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia}km')

if distancia <=  200:
    preço = distancia * 0.50

else:
    preço = distancia * 0.45

''' if e else simplicidado:
preço = distancia * 0.50 if distancia <= 200 else distacia * 0.45'''

print(f'E o preço da sua passagem será de R${preço:.2f}')