#Dicionario
d = {'star wars': {'titulo': 'Star Wars', 'ano': 1977}, 'game of thrones': {'titulo': 'Game of Thrones', 'ano': 2003}}

print(d['star wars'])
print(d['game of thrones'])

d['game of thrones']['diretor'] = 'Irmaos Russuel'

print(f'A serie {d['game of thrones']['titulo']} que surgiu em {d['game of thrones']['ano']} foi dirigida pelos {d['game of thrones']['diretor']}.')

print()

print(d.keys())
print(d.values())
print(d.items())

print()

p = ''
l = {p: 'jose'}
print(l[p])

print()

for k, v in d.items():
    print(f'{k} = {v}')

print()
"""
for i in d:
    for k, v in i:
        print(f'O campo {i} tem {k}')   
"""


