n1 = float(input('DIgite sua nota do primeiro trimestre: '))
n2 = float(input('DIgite sua nota do segundo trimestre: '))
n3 = float(input('DIgite sua nota do terceiro trimestre: '))

m = (n1+n2+n3)/3

if m >= 6:
    print(f'Parabens! voce tirou {f'{m:.1f}'} de média e passou!')
else:
    print(f'Voce tirou {f'{m:.1f}'} de média e rodou!')