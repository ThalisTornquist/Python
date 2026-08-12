try:
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite mais um numero: '))
    res = n1 / n2
    print(f'O resultado da divisao é {res}')


except ValueError:
    print('Somente numeros')

except ZeroDivisionError:
    print('Não existe divisao por zero')
