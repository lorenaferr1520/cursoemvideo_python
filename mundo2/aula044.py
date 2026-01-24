# gerenciador de pagamentos
print('-=-=-=-=-=-=- SUPERMERCADO PYTHON -=-=-=-=-=-=-')
preço = float(input('Qual o preço das compras: '))

forma_de_pagamento = int(input('''Qual a forma de pagamento:
[1] À vista dinheiro/cheque 
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
--> Qual a opção? '''))

if forma_de_pagamento == 1: # 10% de desconto
    pagamento = preço - (preço * 10 / 100)
    print(pagamento)

elif forma_de_pagamento == 2: # 5% de desconto
    pagamento = preço - (preço * 5 / 100)
    print(pagamento)

elif forma_de_pagamento == 3: # preço normal
    pagamento = preço
    print(pagamento)

elif forma_de_pagamento == 4: # 20% de juros
    pagamento = preço + (preço * 20 / 100)
    print(pagamento)

else:
    print('Porfavor digite uma opção válida!')