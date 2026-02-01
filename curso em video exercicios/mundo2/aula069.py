# cadastre uma pessoa
maiores = 0
homens = 0
mulheres = 0
mulheres20 = 0

while True:
    print('--' * 20)
    print('   CADASTRE UMA PESSOA')
    print('--' * 20)
    
    idade = int(input('Idade: '))
    genero = str(input('Sexo [M/F]: ')).upper()
    
    if idade >= 18:
        maiores += 1
        
    if genero == 'M':
        homens += 1
    if genero == 'F' and idade < 20:
        mulheres20 += 1

    
    print('--' * 20)
    escolha = input('Quer continuar? [S/N]: ').upper()
    if escolha == 'S':
        continue
    else:
        break
    

print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados' )
print(f'E temos {mulheres20} mulheres com menos de 20 anos')
print('--' * 20)
print('''Fim do programa 
  __
<(o )___
 ( ._> /
  `---'   quak

      ''')