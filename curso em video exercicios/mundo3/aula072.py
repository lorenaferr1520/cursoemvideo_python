# numeros por extenso
extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis",
    "sete", "oito", "nove", "dez", "onze", "doze", "treze",
    "quatorze", "quinze", "dezesseis", "dezessete",
    "dezoito", "dezenove", "vinte"
)

num = int(input('Digite um número entre 0 e 20: '))

if num > 20 or num < 0:
    while num > 20 or num < 0 :
        num = int(input('ERRO! Digite um número APENAS entre 0 e 20: '))

print(f'Você digitou o número {extenso[num]}')

print('''Fim do programa 
  __
<(o )___
 ( ._> /
  `---'   quak

      ''')