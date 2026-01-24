# gerenciador de pagamentos
cores = {
    'limpa': '\033[m',
    'branco': '\033[30m',
    'vermelho': '\033[1;31m', # Negrito + Vermelho
    'verde': '\033[1;32m',    # Negrito + Verde
    'amarelo': '\033[1;33m',   # Negrito + Amarelo
    'azul': '\033[1;34m',      # Negrito + Azul
    'roxo': '\033[1;35m',      # Negrito + Roxo
    'ciano': '\033[1;36m',     # Negrito + Ciano
    'cinza': '\033[37m',
    'sublinhado': '\033[4m'
}
print(f'{cores["verde"]}-=-=-=-=-=-=-=-=- SUPERMERCADO PYTHON -=-=-=-=-=-=-=-=-{cores["limpa"]}')
preço = float(input('Qual o preço das compras: '))

forma_de_pagamento = int(input('''Qual a forma de pagamento:
[1] À vista dinheiro/cheque 
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
--> Qual a opção? '''))

if forma_de_pagamento == 1: # 10% de desconto
    pagamento = preço - (preço * 10 / 100)
    print(f'Pagamento a vista no dinheiro/cheque com {cores["verde"]}10% de desconto{cores["limpa"]} ')
    print(f'com o total de {cores["sublinhado"]}R${pagamento:.2f}{cores["limpa"]}')
elif forma_de_pagamento == 2: # 5% de desconto
    pagamento = preço - (preço * 5 / 100)
    print(f'Pagamento a vista no cartão com {cores["verde"]}5% de desconto{cores["limpa"]}')
    print(f'com o total de {cores["sublinhado"]}R${pagamento:.2f}{cores["limpa"]}')
    
elif forma_de_pagamento == 3: # preço normal
    pagamento = preço
    parcelas = preço / 2
    print(f'A compra será parcelada em {cores["sublinhado"]}2x de R${parcelas:.2f}{cores["limpa"]} {cores["verde"]}SEM JUROS{cores["limpa"]}')
    print(f'Com o total de {cores["sublinhado"]}R${pagamento}{cores["limpa"]}')
          
elif forma_de_pagamento == 4: # 20% de juros
    num_parcelas = int(input('Qual o número de parcelas: '))
    if num_parcelas >= 3:
        pagamento = preço + (preço * 20 / 100)
        parcelas = preço / num_parcelas
        print(f'A compra será parcelada em {num_parcelas}X de R${parcelas:.2f} {cores["vermelho"]}COM 20% DE JUROS{cores["limpa"]} no cartão')
        print(f'Com o total de {cores["sublinhado"]}R${pagamento:.2f}{cores["limpa"]}')
    else:
        print(f'Apenas acima de 3X no cartão! \n{cores["vermelho"]}Porfavor Digite uma opção válida!{cores["limpa"]}')
       
else:
    print(f'{cores["vermelho"]}Porfavor digite uma opção válida!{cores["limpa"]}')

print(f'{cores["verde"]}-=-{cores["limpa"]}' * 18)