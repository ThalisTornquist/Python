v = int(input('Digite uma velocidade: '))

if v > 80:
    print('Voce foi multado!')
    m = (v - 80) * 7
    print(f'Sua multa foi de {m} Reais.')
else:
    print('voce esta abaixo do limite, continue assim!')