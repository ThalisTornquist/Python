import random
import time
print('-'*30)
print(f"{'JOGA NA MEGA SENA':^30}")
print('-'*30)

n = int(input('Quantos jogos quer sortiar? '))

print(f'SORTEANDO {n} JOGOS')

time.sleep(.5)

for c in range(n):
    num = random.sample(range(1, 61), 6)
    num.sort()
    print(f'Jogo {c+1}: {num}')
    time.sleep(.5)
    num.clear()