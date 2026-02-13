# contador
from time import sleep

def contador(inicio, fim, passo):

    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)

    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}:")
    sleep(0.5)


    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f"{cont} ", end="", flush=True)
            sleep(0.3)
            cont += passo
        print("FIM!")
    

    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont} ", end="", flush=True)
            sleep(0.3)
            cont -= passo
        print("FIM!")
    print("-=" * 20)


contador(1, 10, 1)
contador(10, 0, 2)

print("Agora é sua vez de personalizar a contagem!")
ini = int(input("Início: "))
f   = int(input("Fim:    "))
pas = int(input("Passo:  "))

contador(ini, f, pas)