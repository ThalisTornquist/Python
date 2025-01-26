import random
import time
from time import sleep

n = random.randint(0, 10)
print('_' * 140)
print(f"\033[30;45m-|'_'|-\033[m" * 20)

print('=' * 140)
print('\033[7;40mEstou pensando em um numero de 0 a 10!\033[m')
print('=' * 140)

res = int(input('\033[1;33;40mEm que numero estou pensando? \033[m'))

print('\033[1;36mPROCESSANDO...\033[m')
sleep(1) #FAZ UM UMA ESPERA DE 1 SEGUNDO NESSE CASO
num = 1
while res != n:
    print(f'\033[1;41;30mVoce errou!\033[m')
    res = int(input('Tente novamente: '))
    num += 1

print(f'\033[1;42mPARABÉNS! Você acertou! e presisou de {num} tentativas.\033[m')
