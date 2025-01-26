n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print(f'As retas {n1}, {n2} e {n3} PODEM formar um triangulo!')
else:
    print(f'As retas {n1}, {n2} e {n3} NÃO PODEM formar um triangulo!')
