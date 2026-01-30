# estatisticas em produtos
total_da_compra = 0
compramil = 0
contagem = 0
comprabarato = []


print('--' * 20)
print('               LOJA PYTHON')
print('--' * 20)

while True:
    nome_do_produto = str(input('Nome do produto: '))
    preço_do_produto = float(input('Preço: R$'))
    total_da_compra += preço_do_produto
    
    if preço_do_produto > 1000.00:
        compramil += 1
        
    contagem += 1    
    if contagem == 1:
        comprabarato = [nome_do_produto, preço_do_produto]
    else:
        if  comprabarato[1] >  preço_do_produto:
            comprabarato = [nome_do_produto, preço_do_produto]

    
    continuação = input('Quer continuar [S/N]:').upper()
    
    if continuação == 'S':
        continue
    else:
        break

print('--' * 20)  
print(f'O total da compra foi de R${total_da_compra:.2f}')
print(f'Temos {compramil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {comprabarato[0]} custando {comprabarato[1]:.2f}')
print('--' * 20)
print('''Fim do programa 
  __
<(o )___
 ( ._> /
  `---'   quak

      ''')