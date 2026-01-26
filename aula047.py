# contagem de pares de 1 a 50
lista_de_pares = []

for i in range(1, 51):
    if i % 2 == 0:
        lista_de_pares.append(i)

print(lista_de_pares)

# ou
lista_de_pares2 = []
for i in range(2, 51, 2):
    lista_de_pares2.append(i)

print(lista_de_pares2)