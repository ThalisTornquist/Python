

pi = 0
h = 0
m = 0
while True:
    i = int(input('Qual sua idade? '))

    s = ' '
    while s not in 'mf':
        s = input('Qual seu sexo? [M/F] ').lower().strip()[0]





    if i > 18:
        pi += 1

    if s == 'm':
        h += 1

    if s == 'f' and i < 20:
        m += 1

    e = ' '
    while e not in 'sn':
        e = input('Quer continuar? [S/N] ').lower().strip()[0]

    if e == 'n':
        break

print(f'Existem {h} homens.')
print(f'Existem {pi} pessoas com mais de 18 anos.')
print(f'Existem {m} mulheres com menos de 20 anos.')