p = 0
pp = 0
for c in range(5):
    r = float(input('qual o peso de alguem? '))
    if pp == 0:
        pp = r
        p = r
    else:
        if r > p:
            p = r

        if pp > r:
            pp = r

    r = 0
print(f'O maior peso foi {p}kg, e o menor foi {pp}kg.')