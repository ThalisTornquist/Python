

d = {}

d['nome'] = input('Qual o nome do jogador? ')
p = int(input(f'Quantas partidas {d['nome']} Jogou? '))
d['gol'] = []

for c in range(p):
    d['gol'].append(int(input(f'   Quantos gols ele fez na partida {c+1}? ')))

d['total'] = 0
for g in d['gol']:
    d['total'] += g
# poderia fazer com 'sum' mas esqueci
print()

print(d)
print()

for k, v in d.items():
    print(f'O campo {k} recebe {v}.')

print(f'O jogador {d['nome']} jogou {p} partidas')

print()

for c in range(p):
    print(f'   => Na partida {c+1}, fez {d['gol'][c]} gols')
print(f'O total foi {d['total']} gols.')