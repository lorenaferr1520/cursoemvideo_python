# maior e menor da sequencia

maior = 0.0
menor  =  0.0

for p in range(1, 6):
    peso = (float(input(f'qual o peso da {p}ª pessoa : ')))
    
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
            
        if peso < menor:
            menor = peso

print(f'O maior peso foi {maior}Kg \nE o menor peso foi {menor}Kg')