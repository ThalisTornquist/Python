
l = []
p = []
ip = []
while True:

    v = int(input('Digite um numero: '))
    l.append(v)

    if v % 2 == 0:
        p.append(v)
    else:
        ip.append(v)


    s = ' '
    while s not in 'sn':
        s = input('Quer continuar? [S/N] ').lower()

    if s == 'n':
        break


l.sort()
print(f'Voce adicionou os valores {l}')
print(f'A lista de pares foi {p}')
print(f'A lista de impares foi {ip}')