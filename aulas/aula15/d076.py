l = ('Lapis', 1.75, 'borracha', 2, 'caderno', 17)
for n in range(len(l)):
    if n % 2 == 0:
        print(f'{l[n]:.<30}', end='')
    else:
        print(f'{l[n]:>}')