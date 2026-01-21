# seno, cosseno e tangente
import math
ang = float(input("Digite o angulo que você deseja: "))

seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))

print(f"No angulo de {ang}° tem o seno de {seno:.2f}")
print(f"No angulo de {ang}° tem o cosseno de {cosseno:.2f}")
print(f"No angulo de {ang}° tem a tangente de {tangente:.2f} ")