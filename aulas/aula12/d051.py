a1 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão dessa PA: '))

#pa = [a1 + (i * r) for i in range(10)]
#print(pa)
t =  a1 + (10 - 1) * r + r
for i in range(a1, t, r):
    print(i)