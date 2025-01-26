l = ('aprender', 'programar')

for v in l:
    print(f'na palavra {v} temos ', end='')
    for vo in v:
        if vo in 'aeiou':
            print(f'{vo} ', end='')