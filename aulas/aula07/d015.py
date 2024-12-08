d = int(input('Quantos dias você ficou com o carro? '))
km = int(input('Quantos km você andou? '))

pd = d * 60
pkm = km * 0.15
tp = pd + pkm

print('O total a ser pago é de {:.2f} Reais.'.format(tp))