d = int(input('Digite a distancia de viajem: '))

if d <= 200:
    p = d * 0.5
    print(f'O valor da passagem é de {f'{p:.2f}'} Reais.')
else:
    p = d * 0.45
    print(f'O valor da passagem é de {f'{p:.2f}'} Reais.')