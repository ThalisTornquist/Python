
l1 = []
l2 = []
l3 = []

for c in range(1, 10):
    n = int(input('Digite um numero: '))


    if c <= 3:
        l1.append(n)
    elif c <= 6:
        l2.append(n)
    elif c <= 9:
        l3.append(n)


print(f'[{l1[0]}] [{l1[1]}] [{l1[2]}]')
print(f'[{l2[0]}] [{l2[1]}] [{l2[2]}]')
print(f'[{l3[0]}] [{l3[1]}] [{l3[2]}]')