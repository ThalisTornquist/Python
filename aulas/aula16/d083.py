e = [input('Digite uma expreção matematica com (): ')]
v1 = e.count('(')
v2 = e.count(')')

if v1 == v2:
    print('Essa expreção esta correta!')
else:
    print('Essa expreção esta incorreta!')