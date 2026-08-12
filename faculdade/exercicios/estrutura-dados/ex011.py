estoque = {
    'batata' : 50,
    'carne' : 20,
    'arroz' : 100
}

print(estoque['carne'])
estoque['feijao'] = 80
estoque['batata'] = 70

for c in estoque:
    print(f'A quanteidade de {c} é {estoque[c]}')

print(estoque.keys())
print(estoque.values())
print(estoque.items())