# dissecando uma variável

variavel = input('digite algo: ')
print(f'o tipo primitido desse valor é {type(variavel)}')
print('só tem espaços', variavel.isspace())
print('é um número:', variavel.isnumeric())
print('é alfabético:', variavel.isalpha())
print('é alfanumérico:', variavel.isalnum())
print('está em maiúsculas?', variavel.isupper())
print('está em minusculas?', variavel.islower())
print('está capitalizada?', variavel.istitle())

''' variavel nesse caso é um objeto, todo objeto tem caracteristicas
e realizam funcionalidades '''