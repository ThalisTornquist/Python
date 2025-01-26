l = []
for c in range(0, 5):
    l.append(int(input('Digite um número: ')))


m = l[0]
p = l[0]
pos = 0
posp = 0


for i in range(len(l)):

    if l[i] > m:
        m = l[i]
        pos = i
    if l[i] < p:
        p = l[i]
        posp = i




print(f'O maior valor foi {m} na posição {pos}.')
print(f'O menor valor foi {p} na posição {posp}.')
