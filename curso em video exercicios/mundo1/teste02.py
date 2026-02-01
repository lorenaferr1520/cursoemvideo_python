''' Criando um Inventário
Crie um dicionário chamado estoque com os seguintes itens: {"monitor": 5, "teclado": 10, "mouse": 15}.
Adicione um novo item: "headset" com valor 8.
Atualize a quantidade de "teclado" para 12.
Printe apenas as chaves desse dicionário.'''

estoque = {"monitor": 5,
           "teclado": 10,
           "mouse": 15,}

print(estoque)

estoque["headset"] = 8
estoque["teclado"] = 12

print(estoque)