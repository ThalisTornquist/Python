n = input('Digite seu nome completo: ').strip()

print(f'Primeiro nome: {n.split()[0]}')
l = int(len(n.split())) - 1
print(f'Ultimo nome: {n.split()[l]}')

