# aluguel de carros
# diarias = R$60,00   km = R$0,15

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

pago = (dias * 60) + (km * 0.15) #aluguel das diárias e km gastos

print(f'o total a pagar é de R${pago:.2f}')