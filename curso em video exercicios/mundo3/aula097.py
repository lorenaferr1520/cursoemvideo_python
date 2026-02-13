# linha de tamanho variável
def escreva(msg):
    tam = len(msg) + 4 # tamanho personalizado
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    

escreva('oi tudo bem')
escreva('curso em video python')
escreva('linhas personalizadas')