num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

# verificando menor
if num1 < num2 and num1 < num3:
    menor = num1
if num2 < num3 and num2 < num1:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
# verificando maior
if num1 > num2 and num1 > num3:
    maior = num1
if num2 > num3 and num2 > num1:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f'O menor número digitado é o {menor}')
print(f'O maior número digitado é o {maior} ')