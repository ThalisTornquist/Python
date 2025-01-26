s = 'x'
r = 'r'
while r != 'v':
    s = input('Digite seu sexo: [m/f] ').lower()
    if s == 'm' or s == 'f':
        r = 'v'
print('ok!')