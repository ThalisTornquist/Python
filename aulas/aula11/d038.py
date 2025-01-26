n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n1 > n2:
    print(f'O numero {n1} é maior que {n2}.')
elif n2 > n1:
    print(f'O numero {n2} é maior que {n1}.')
else:
    print('Os numeros sao iguais.')