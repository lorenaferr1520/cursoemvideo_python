# calcular area da parede e quanto de tinta se gasta nela
# 1 litro de tinta == 2m quadrados

altura = float(input('qual a altura da parede em metros: '))
largura = float(input('qual a largura da parede em metros: '))

litrotinta = 2 #litros
metrosquad = altura * largura
tinta = metrosquad / litrotinta

print(f'a parede possui {metrosquad} metros quadrados')
print(f'serão gastos {tinta} litros de tinta nessa parede')