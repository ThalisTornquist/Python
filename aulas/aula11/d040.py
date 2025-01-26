n1 = float(input('Digite sua nota do 1 trimestre: '))
n2 = float(input('Digite sua nota do 2 trimestre: '))

m = (n1 + n2) / 2

if m < 5:
    print('REPROVADO!')
elif m >= 5 and m < 7:
    print('REUPERAÇÃO!')
else:
    print('PASSOU!')

print(f'Sua media foi de {f'{m:.1f}'}')