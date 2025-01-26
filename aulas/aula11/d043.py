a = float(input('Digite sua altura: '))
p = float(input('Digite seu peso: '))

imc = p / a ** 2

if imc < 18.5:
    print('Voce esta abixo do peso.')
elif imc < 25:
    print('Voce esta no peso ideal.')
elif imc <= 30:
    print('Voce esta em sobrepeso.')
elif imc <= 40:
    print('voce esta obeso')
else:
    print('voce esta em obesidade morbida.')

print(f'seu imc é de {f'{imc:.1f}'}')
