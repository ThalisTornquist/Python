

l = []
h = {}
it = 0
mu = []


while True:



    h['nome'] = input('Nome: ')
    h['sexo'] = ' '
    #falta a parte de media,  minha ideia é pra cada item em l no lugar media ai teste logico.
    while h['sexo'] not in 'mf':
        h['sexo'] = input('Sexo: [M/F] ').lower()
    if h['sexo'] == 'f':
        mu.append(h['nome'])

    h['idade'] = int(input('Idade: '))


    it += h['idade']




    l.append(h.copy())
    h.clear()

    s = ' '
    while s not in 'sn':
        s = input('Quer continuar? [S/N] ').lower()

    if s == 'n':
        break
m = it / len(l)


print(f'A) Ao todo temos {len(l)} pessoas.')
print(f'B) A idade média é {m:.0f} anos.')
print(f'C) As mulheres cadastradas sao {mu} .')
print('D) Lista de pessoas acima da media de idades:')
for c in range(len(l)):
    if l[c]['idade'] >= m:
        print(f'     Nome = {l[c]['nome']}; Sexo = {l[c]['sexo']}; Idade = {l[c]['idade']}; ')

