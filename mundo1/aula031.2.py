# calcular preço da passagem por distancia SIMPLIFICADO

distancia = float(input('Qual a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia}km')

# if e else simplicidado:
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print(f'E o preço da sua passagem será de R${preço:.2f}')