# Soma ímpares múltiplos de três
# (some números impares multiplos de 3)

contador = 0
soma = 0

for i in range(1, 500, 2):
    if i % 3 == 0:
        contador += 1
        soma += i

print(f'A soma de todos os {contador} valores solicitados é igual a {soma}')