n = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        n += c

print(f'A soma de todos os multiplos de 3 entre 1 e 500 é {n}')
