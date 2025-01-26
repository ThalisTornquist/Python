v = int(input('Quanto quer sacar? '))
c50 = 0
c20 = 0
c10 = 0
c1 = 0
while True:
    if v >= 50:
        c50 += 1
        v -= 50

    elif v >= 20:
        c20 += 1
        v -= 20

    elif v >= 10:
        c10 += 1
        v -= 10
    elif v >= 1:
        c1 += 1
        v -= 1

    if v == 0:
        break

if c50 > 0:
    print(f'Voce vai receber {c50} notas de R$50,00')

if c20 > 0:
    print(f'Voce vai receber {c20} notas de R$20,00')

if c10 > 0:
    print(f'Voce vai receber {c10} notas de R$10,00')

if c1 > 0:
    print(f'Voce vai receber {c1} notas de R$1,00')