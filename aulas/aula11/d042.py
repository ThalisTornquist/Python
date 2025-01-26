n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print(f'As retas {n1}, {n2} e {n3} PODEM formar um triangulo!')
    if n1 == n2 and n1 == n3:
        print('Formam um triangulo Equilatero (todos os lados iguais)')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Formam um triangulo isóseles (dois lados iguais)')
    else:
        print('Formam um triangulo Escaleno (todos os lados diferentes)')
else:
    print(f'As retas {n1}, {n2} e {n3} NÃO PODEM formar um triangulo!')
