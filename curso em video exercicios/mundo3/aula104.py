def leiaInt(msg="Digite um número", padrao=0):
    while True:
        entrada = input(f"{msg}: ").strip()

        if not entrada:
            print(f"Entrada vazia. Valor padrão definido: {padrao}")
            return padrao

        try:
            valor = int(entrada)
            return valor
        except (ValueError, TypeError):
            print("\033[31mERRO: Digite um número inteiro válido!\033[m")

n = leiaInt("Digite um número")
print(f"O número final guardado foi {n}")