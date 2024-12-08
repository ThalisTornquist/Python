c = float(input('Digite uma temperatura em ºC: '))
fc = (c * 9/5) + 32
kc = c + 273,15

print('{} ºC são iguais a {:.2f} ºF e {:.2f} K'.format(c,fc,kc))
