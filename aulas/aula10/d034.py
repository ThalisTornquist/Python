s = float(input('Digite seu salario: '))

if s >= 1250:
    a = s * 0.1 + s
    print(f'Seu novo salario é de R${f'{a:.2f}'}')
else:
    a = s * 0.15 + s
    print(f'Seu novo salario é de R${f'{a:.2f}'}')

