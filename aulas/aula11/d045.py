import random
import time

ops = ['pedra', 'papel', 'tesoura']
r = input('pedra, papel ou tesoura? ').lower()
e = random.choice(ops)

time.sleep(.5)
print('PEDRA!')
time.sleep(.8)
print('PAPEL!')
time.sleep(.8)
print('TESOURA!')


if e == r.lower():
    print(f'empatou ambos escolhemos {e}')
elif e == 'pedra' and r == 'tesoura':
    print(f'Voce perdeu, eu escolhi {e}.')
elif e == 'pedra' and r == 'papel':
    print(f'Voce Ganhou! parabens! escolhi {e}')
elif e == 'papel' and r == 'tesoura':
    print(f'Voce Ganhou! parabens! escolhi {e}')
elif e == 'papel' and r == 'pedra':
    print(f'Voce perdeu, eu escolhi {e}.')
elif e == 'tesoura' and r == 'papel':
    print(f'Voce perdeu, eu escolhi {e}.')
elif e == 'tesoura' and r == 'pedra':
    print(f'Voce Ganhou! parabens! escolhi {e}')

