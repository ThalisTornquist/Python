p = 0
g = 0
num = 0
c = 0
res = 's'
while res == 's':
    c += 1
    n = int(input('Digite um numero: '))
    res = input('Quer continuar?  [s/n]').lower()
    num += n

    if c == 1:
        g = n
        p = n
    if n > g:
        g = n
    if p > n:
        p = n

m = num / c
print(f'Voce digitou {c} numeros, e a media deles é {m}.')
print(f'O maior numero foi {g} e o menor foi {p}.')