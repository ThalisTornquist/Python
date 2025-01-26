a1 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão dessa PA: '))
pa = a1
nt = 0

tf = int(input('Quer ver quantos termos dessa PA? '))
while nt < tf:
    print(pa)

    nt += 1
    pa += r




'''t =  a1 + (10 - 1) * r + r
for i in range(a1, t, r):
    print(i)'''