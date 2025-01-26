p = float(input('Qual o preço do produto?'))
print('digite 1 para comprar com dinheiro')
print('digite 2 para comprar com cartao a vista')
print('digite 3 para comprar com cartao em 2 vezes')
print('digite 4 para comprar com cartao em 3 ou mais vezes')
cp = int(input('qual  aforma de pagamento? '))


if cp == 1:
    p = p - p * 0.1
    print(f'O preço final fica R${f'{p:.2f}'}')
elif cp == 2:
    p = p - p * 0.05
    print(f'O preço final fica R${f'{p:.2f}'}')
elif cp == 3:
    print(f'O preço final fica R${f'{p:.2f}'}')
else:
    p = p + p * 0.2
    pm = int(input('Em quantas parcelas ira pagar? '))
    pp = p / pm
    print(f'O preço final fica R${f'{p:.2f}'}, e cada parcela custara R${f'{pp:.2f}'}')
