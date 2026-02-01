# while

tabuada = 2
contagem = 1

while contagem <= 20:
    print(f'2 X {contagem} = {contagem * 2}')
    contagem += 1
    
input()
vogais = ["a","e","i","o","u","A","E","I","O","U"]
palavra = input('digite uma palavra: ')
nova = ""

for i in palavra:
    if i not in vogais:
        nova += i

print(nova)