
l = []

d = []
a = []
m = []
nada = ''
while True:
    nome = input('Digite seu nome: ')
    n1 = float(input('Qual sua nota1: '))
    n2 = float(input('Qual sua nota2: '))

    a.append(nome)
    d.append(n1)
    d.append(n2)


    a.append(d[:])

    l.append(a[:])

    mm = (n1 + n2) / 2
    m.append(mm)


    a.clear()
    d.clear()


    s = ' '
    while s not in 'sn':
        s = input('Quer continuar? [S/N] ').lower()

    if s == 'n':
        break

print('-='*30)
print(f'{'NOME':<20}{'MÉDIA':>20}')
print('-'*40)

for c in range(len(l)):
    print(f'{l[c][0]:<12}[{c+1}]{nada:5}', end='')
    print(f'{m[c]:>20}')

print('-'*40)

while True:
    num = int(input('Mostrar notas de qual aluno? ([999] para sair)'))

    if num == 999:
        break
    if num > len(l):
        print('Numero invalido!')
    else:
        print(f'O aluno {l[num-1][0]} tirou as notas {l[num-1][1]}')