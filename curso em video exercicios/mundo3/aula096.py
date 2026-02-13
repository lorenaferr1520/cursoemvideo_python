# função que calcula a area
def area(largura, comprimento):
    a = largura * comprimento
    print(f'A area de um terrenp {comprimento} X {largura} é igual a {a:.2f} metros quadrados')

print('      Controle de Terreno')
print('-=' * 15)
l = float(input('Largura em metros: '))
c = float(input('comprimento em metros: '))
area(l, c)