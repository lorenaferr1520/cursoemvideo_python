# calculando descontos

produto = float(input('qual o preço do produto? R$'))
novo = produto - (produto * 5 / 100)

print(f'o produto que custava R${produto:.2f} na promoção com desconto de 5% vai custar R${novo:.2f}')