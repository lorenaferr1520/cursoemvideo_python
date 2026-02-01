# Validação de dados

informação = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]

while informação not in 'MmFf':
    informação = str(input('Dados inválidos! por favor informe seu sexo: [M/F] ')).upper().strip()[0]
    

print(f'Sexo {informação} registrado com sucesso!')
print("FIM")
