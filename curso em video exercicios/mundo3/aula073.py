# tupla brasileirão
times = (
    "Palmeiras", "Grêmio", "Atlético-MG", "Flamengo", "Botafogo",
    "Red Bull Bragantino", "Fluminense", "Athletico-PR", "Internacional", "Fortaleza",
    "São Paulo", "Cuiabá", "Corinthians", "Cruzeiro", "Vasco",
    "Bahia", "Santos", "Goiás", "Coritiba", "América-MG"
)

print('-=-' * 20)
print('                         BRASILEIRÃO')

print('-=-' * 20)
print("Lista de times do Brasileirão:")
print(times)

print('-=-' * 20)
print("\nOs 5 primeiros colocados:")
print(times[:5])

print('-=-' * 20)
print("\nOs últimos 4 colocados:")
print(times[-4:])

print('-=-' * 20)
print("\nTimes em ordem alfabética:")
print(sorted(times))

print('-=-' * 20)

print("\nPosição do Corinthians:")
print(times.index("Corinthians") + 1)


print('-=-' * 20)
print('''Fim do programa 
  __
<(o )___
 ( ._> /
  `---'   quak

      ''')
