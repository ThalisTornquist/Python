import random
import time
from operator import itemgetter

j = {}
n = 0

for c in range(4):
    n += 1
    j[f'jogador{n}'] = random.randint(1,    6)

    print(f'Jogador{n} = {j[f'jogador{n}']}')
    time.sleep(.5)

rank = sorted(j.items(), key=itemgetter(1))


print()
print('-'*30)
print()
time.sleep(.5)


print(f'{'--<RANKING>--':^23}')
num = 1
for con in range(3, -1, -1):
    print(f'{num} lugar: {rank[con][0]} com {rank[con][1]}')
    num += 1






