
c = 0
print('Numero negativo para sair.')
while True:
    n = int(input('Digite um numero: '))
    c = 0
    if n < 0:
        break
    while c < 10:

        c += 1
        print(f'{n} x {c} = {n*c}')
