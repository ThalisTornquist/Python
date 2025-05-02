l = []
d = {}
gol = []
while True:
    d.clear()

    d['nome'] = input('Qual o nome do jogador? ')

    # CORREÇÃO 1: Corrigido o f-string aninhado (troca de aspas)
    p = int(input(f"Quantas partidas {d['nome']} jogou? "))

    gol.clear()

    for c in range(p):
        gol.append(int(input(f'   Quantos gols ele fez na partida {c + 1}? ')))

    d['total'] = sum(gol)  # CORREÇÃO 2: Substituí o loop manual por sum()

    d['gols'] = gol[:]  # CORREÇÃO 3: Adicionado a lista de gols corretamente no dicionário

    l.append(d.copy())  # CORREÇÃO 4: Removida a linha que adicionava `gol.copy()` separadamente

    s = ' '
    while s not in 'sn':
        s = input('Quer continuar? [S/N] ').lower()

    if s == 'n':
        break

print()

print(f"{'N°'}  {'Nome':<13}{'Gols':^12}{'Total':^12}")
print('-' * 38)

for c in range(len(l)):
    # CORREÇÃO 5: Acessando corretamente `l[c]['gols']` ao invés de `l[c][gol]`
    print(f'{c+1} - {l[c]["nome"]:<13}{str(l[c]["gols"]):^12}{l[c]["total"]:^12}')

print('-' * 38)

# Falta o loop final mostrando os dados

while True:
    dado = int(input('Mostrar os dados de qual jogador? [999 - PARAR]')) - 1

    print(f'-- LEVANTAMENTO DO JOGADOR {l[dado]['nome']}:')

    cont = 0
    for c in l[dado]['gols']:
        cont += 1
        print(f'    => Na partida {cont} fez {c} gols.')

    if dado == 999:
        break


