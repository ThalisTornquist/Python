
n = (int(input('Dgite um numero: ')), int(input('Dgite um numero: ')), int(input('Dgite um numero: ')), int(input('Dgite um numero: ')))
p = 0

for c in range(4):
    if n[c] % 2 == 0:
        p += 1

nove = n.count(9)
t = n.index(3)

print(n)
print(f'Existem {nove} numeros 9')
if t != -1:
    print(f'O numero 3 esta na posisao {t}')
else:
    print('Nao tem 3')
print(f'Existem {p} numeros pares')