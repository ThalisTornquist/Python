n = int(input('Digite um numero: '))

print('Digite 1 para converter em binario.')
print('Digite 2 para converter em octal.')
print('Digite 3 para converter em hexadecal.')

r = int(input('digite o numero da base que voce quer converter: '))

if r == 1:

    bn = bin(n)[2:]

    print(f'O numero {n} convertido para binario fica {bn}.')

elif r == 2:

    on = oct(n)[2:]

    print(f'O numero {n} convertido para binario fica {on}.')

elif r == 3:

    hn = hex(n)[2:]

    print(f'O numero {n} convertido para binario fica {hn}.')

else:
    print('escolha uma das três bases para funcionar.')
