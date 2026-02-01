salario = float(input('Digite o salário do funcionário: '))

if salario >= 1250.00:
    aumento = (salario * 10) / 100
else:
    aumento = (salario * 15) / 100

print(f'O funcionário que ganhava R${salario:.2f} agora ganha {salario + aumento:.2f}')