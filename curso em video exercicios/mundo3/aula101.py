from datetime import date

def voto(ano):
    ano_atual = date.today().year
    idade = ano_atual - ano
    
    if 18 <= idade < 70:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif 16 <= idade < 18 or idade >= 70:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: NÃO VOTA.'

print('-' * 25)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))