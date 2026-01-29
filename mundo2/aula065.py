# maior e menor valor
escolha = "S"
contador = 0
maior = 0
menor = 0
soma = 0

while escolha != 'N':
    num = int(input('Digite um número: '))
    soma += num
    contador += 1
    
    if contador <= 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num


    escolha = str(input('Quer continuar? [S/N]: ')).upper()

media = soma / contador
print(f'Você digitou {contador} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
