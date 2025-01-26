import random

n = random.choices(range(0, 11), k=5)
print(n)
c = 0
g = 0
p = 0
for cc in range(0, len(n)):

    if c == 0:
        g = n[0]
        p = n[0]

    if g < n[c]:
        g = n[c]

    if p > n[c]:
        p = n[c]

    c += 1


print(f'O maior foi {g}')
print(f'O menor foi {p}')
