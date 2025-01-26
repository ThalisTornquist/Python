
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


l.sort(reverse=True)
print(f'Voce adicionou os valores {l}')
print(f'foram adcionados {len(l)} valores')

if 5 in l:
    print('Tem o numero 5')
else:
    print('nao tem 5')