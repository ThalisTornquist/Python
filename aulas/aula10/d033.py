n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))

if n1 - n2 > 0 and n1 - n3 > 0:
    print(f'O MAIOR numero é {n1}')
elif n2 - n3 > 0:
    print(f'O MAIOR numero é {n2}')
else:
    print(f'O MAIOR numero é {n3}')

if n1 - n2 < 0 and n1 - n3 < 0:
    print(f'O MENOR numero é {n1}')
elif n2 - n3 < 0:
    print(f'O MENOR numero é {n2}')
else:
    print(f'O MENOR numero é {n3}')
