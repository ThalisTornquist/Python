import random

v = 0

while True:
    n = int(input('Digite um valor: '))
    r = input('Par ou Impar? ').lower()

    l = ['par', 'impar']
    e = random.choice(l)
    e2 = random.randint(1,10)
    s = e2 + n


    if s % 2 == 0:
        res = 'par'
        if r == res:
            print(f'GANHOU! escolheu {n} e o computador escolheu {e2}.')
            v += 1
        else:
            print(f'PERDEU! escolheu {n} e o computador escolheu {e2}. ')
            break
    else:
        res = 'impar'
        if r == res:
            print(f'GANHOU! escolheu {n} e o computador escolheu {e2}.')
            v += 1
        else:
            print(f'PERDEU! escolheu {n} e o computador escolheu {e2}. ')
            break


print(f'Voce ganhou {v} vezes seguidas!')