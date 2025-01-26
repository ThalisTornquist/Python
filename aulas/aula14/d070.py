t = 0
p = 0
b = 0
c = 0
c2 = 0
while True:
    np = input('Qual o nome do produto? ')
    p = float(input('Qual o preço do produto? '))

    if p > 1000:
        c2 += 1

    t += p

    if c == 0:
        b = p
        nb = np

    elif p < b:
        b = p
        nb = np

    c += 1
    res = ' '
    while res not in 'sn':
        res = input('Quer continuar? [S/N]').lower().strip()[0]

    if res == 'n':
        break

print(f'Voce compro {c} itens e pagou R${t:.2f}')
print(f'{c2} itens custaram mais de R$1000,00')
print(f'O produto mais barato foi {nb} e custou R${b:.2f}')