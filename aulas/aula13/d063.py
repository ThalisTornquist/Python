nt = int(input('Quantos termos quer ver? '))

t1 = 0
t2 = 1
t3 = 0
c = 3
print(t1)
print(t2)
while c <= nt:
    t3 = t1 + t2

    print(t3)
    t1 = t2
    t2 = t3
    c += 1
print(f'fim!')