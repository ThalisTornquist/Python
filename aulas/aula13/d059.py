n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))


print('[1] Para SOMAR')
print('[2] Para MULTIPLICAR')
print('[3] Para MAIOR')
print('[4] Para NOVOS NUMEROS')
print('[5] Para SAIR')

res = 10

while res != 5:
    res = int(input('oque voce deseja fazer com os numeros? '))

    if res == 1:
        print(f'A soma entre {n1} e {n2} é {n1+n2}')
    elif res == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1*n2}')
    elif res == 3:
        if n1 > n2:
            m = n1
        else:
            m = n2
        print(f'O maior entre {n1} e {n2} é {m}.')
    elif res == 4:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite um numero: '))
    else:
        print('Tente novamente, apenas valores entre 1 e 5.')

print('Obigado por nos usar!')

