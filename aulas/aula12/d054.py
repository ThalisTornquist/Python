pm = 0
pn = 0
for c in range(7):
    r = int(input('qual o ano de nascimento de alguem? '))
    if r <= 2006:

        pm += 1
    else:
        pn += 1

    r = 0
print(f'Existem {pm} pessoas de maior e {pn} pessoas de menor.')