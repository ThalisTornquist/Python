
l = []

while True:

    v = int(input('Digite um numero: '))

    if v in l:
        print('Valor ja adcionado tente outro!')
    else:
        print('Valor adicionado!')
        l.append(v)


    s = ' '
    while s not in 'sn':
        s = input('Quer continuar? [S/N] ').lower()

    if s == 'n':
        break


l.sort()
print(f'Voce adicionou os valores {l}')