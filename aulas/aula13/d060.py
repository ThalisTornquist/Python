n = int(input('Digite um numero: '))
f = 1
ni = n
while n > 1:

    num = (n - 1)
    if  n == ni:
        f = n * num
    else:
        f = f * num

    n -= 1
print(f'O fatorial de {ni} é {f}.')