# aprovando emprestimo
cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m'
}

print('-=-' * 18)
print('                CALCULANDO EMPRESTIMO')
print('-=-' * 18)

valor_da_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos_financiamento = int(input('Quantos anos de financiamento: '))

trinta = (salario * 30) / 100
prestação_mensal = (valor_da_casa / anos_financiamento) / 12


if prestação_mensal > trinta:
    print(f'{cores["vermelho"]}Emprestimo NEGADO!{cores["limpa"]}')
    print(f'JUSTIFICATIVA: \nA prestação excederia 30% de um salario de R${salario:.2f} ')
else:
    print(f'{cores["verde"]}Emprestimo APROVADO!{cores["limpa"]}')

print('-=-' * 18)