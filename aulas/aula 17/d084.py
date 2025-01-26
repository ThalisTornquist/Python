l = []
dd = []

pg = 0
pp = 0
c = 0
ng = []
np = []


while True:
    dd.append(input('Digite seu nome: '))
    dd.append(int(input('Digite seu peso: ')))
    l.append(dd[:])


    if c == 0:
        pg = dd[1]
        pp = dd[1]

        ng.append(dd[0])
        np.append(dd[0])
    else:
        if pg <= dd[1]:

            if pg == dd[1]:
                ng.append(dd[0])
            else:
                ng.clear()
                ng.append(dd[0])
            pg = dd[1]

        if pp >= dd[1]:

            if pp != dd[1]:
                np.clear()
                np.append(dd[0])
            else:
                np.append(dd[0])

            pp = dd[1]



    dd.clear()
    c += 1
    s = ' '
    while s not in 'sn':
        s = input('Quer continuar? [S/N] ').lower()

    if s == 'n':
        break

print(f'Foram adicionados {len(l)} nomes.')
print(f'O mais pesado é {ng} com {pg}Kg.')
print(f'O mais leve é {np} com {pp}Kg.')