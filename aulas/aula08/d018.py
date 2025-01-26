import math

a = float(input('Digite um angulo: '))

# Converte o ângulo para radianos
arad = math.radians(a)

seno = math.sin(arad)
cosseno = math.cos(arad)
tangente = math.tan(arad)

print(f"Seno: {f'{seno:.2f}'} "
      f"Cosseno: {f'{cosseno:.2f}'} "
      f"Tangente: {f'{tangente:.2f}'} ")
