# Analisador completo
soma_idade = 0
maior_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''

for p in range(1, 5):
    print(f'---- {p}ª PESSOA ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M / F]: ')).strip().upper()
    
    soma_idade += idade
    
    if p == 1 and sexo == 'M':
        maior_idade_homem = idade
        nome_mais_velho = nome
    
    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    
media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade} anos')
print(f'O homem mais velho tem {maior_idade_homem} e se chama {nome_mais_velho}')
    