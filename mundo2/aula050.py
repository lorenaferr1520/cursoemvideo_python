# soma de pares

lista_pares = []

for n in range(1,7):
    num  = int(input("Digite um número: "))
    if num % 2 == 0:
        lista_pares.append(num)

soma = sum(lista_pares)
print(f'Você digitou {len(lista_pares)} números pares e a soma foi {soma}.')