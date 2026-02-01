# vários números com flag
num = 0
contador = 0
soma = 0

while True:
    num = int(input('Digite um valor [999 para sair]:'))
    
    if num == 999:
        break
    soma += num
    contador += 1
    
print(f'Você digitou {contador} números \n e a soma deles é igual a {soma}')