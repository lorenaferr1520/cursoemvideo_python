# verifica se existe silva no nome da pessoa

nome = str(input("Qual o seu nome: ").lower())
silva = "silva"

print("Seu nome tem Silva?", silva in nome)