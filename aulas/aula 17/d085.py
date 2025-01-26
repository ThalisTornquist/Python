
li = []
lp = []
t = []
for c in range(7):
    n = int(input('Digite um numero: '))

    if n % 2 == 0:
        lp.append(n)
    else:
        li.append(n)

li.sort()
lp.sort()
t.append(lp[:])
t.append(li[:])
print(f'Os valores pares foram {t[0]}')
print(f'Os valores impares foram {t[1]}')