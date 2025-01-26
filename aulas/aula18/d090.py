

d = {}

d['nome'] = input('Nome: ')
d['media'] = int(input(f'Média de {d['nome']}: '))

if d['media'] >= 7:
    d['res'] = 'Aprovado'
else:
    d['res'] = 'Reprovado'

print(f'O nome é {d['nome']}, sua media é {d['media']} e esta {d['res']}!')

