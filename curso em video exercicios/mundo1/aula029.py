# radar eletronico

limite = 80.0
multa = 7.00
vel = float(input('Qual a velocidade atual do carro? '))


if vel > limite:
    print(f"MULTADO! você excedeu o limite permitido de {limite}km/h")
    cal_multa = (vel - 80) * multa
    print(f"Você deve pagar uma multa de R${cal_multa:.2f}")
else:
    print('Tenha um bom dia e diriga com segurança!')