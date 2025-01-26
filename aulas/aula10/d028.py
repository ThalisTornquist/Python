import random
import time
from time import sleep

n = random.randint(0, 5)
print('_' * 140)
print(f"\033[30;45m-|'_'|-\033[m" * 20)

print('=' * 140)
print('\033[7;40mEstou pensando em um numero de 0 a 5!\033[m')
print('=' * 140)

res = int(input('\033[1;33;40mEm que numero estou pensando? \033[m'))

print('\033[1;36mPROCESSANDO...\033[m')
sleep(1) #FAZ UM UMA ESPERA DE 1 SEGUNDO NESSE CASO

if res == n:
    print('\033[1;42mPARABÉNS! Você acertou!\033[m')
else:
    print(f'\033[1;41;30mVoce errou! Eu pensei no numero {n}, não no {res}.\033[m')
