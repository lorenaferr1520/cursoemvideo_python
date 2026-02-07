# maior e menor valores da lista

n1= int(input('Digite o valor da posição 0: '))
n2= int(input('Digite o valor da posição 1: '))
n3= int(input('Digite o valor da posição 2: '))
n4= int(input('Digite o valor da posição 3: '))
n5= int(input('Digite o valor da posição 4: '))
valores = [n1, n2, n3, n4, n5]
contagem = 0
maiorvalor = 0
menorvalor = 0
print('-=-'  * 20)
for i in valores:
    contagem += 1
    if contagem == 1:
        maiorvalor = i
        menorvalor = i
    else:
        if i > maiorvalor:
            maiorvalor = i
        if i < menorvalor:
            menorvalor = i

print(f'Você digitou os valores {valores}')
print(f'O maior valor da lista é {maiorvalor} nas posições')
print(f'O menor valor da lista é {menorvalor}')
print('-=-'  * 20)