# tratando valores
num = 0
contagem = 0
soma = 0

while num != 999:
    num = int(input('Digite um número [999 para parar]:'))
    if num != 999:
        soma += num
        contagem += 1

print(f'Você digitou {contagem} números e a soma deles é igual a {soma}')
print('''Fim do programa 
  __
<(o )___
 ( ._> /
  `---'   quak

      ''')