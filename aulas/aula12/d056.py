im = 0
nome = ''
p = 0
m = 0
for c in range(4):
    n = input('Digite um nome: ')
    i = int(input('Digite uma idade: '))
    s = input('Digite "M" para Masculino e "F" para Femenino: ').lower()

    m += i
    if s == 'm':
        if i > im:
            im = i
            nome = n
    elif s == 'f':
        if i < 20:
            p += 1
    else:
        print('sexo invalido!')


print('-'*50)
print(f'O homem mais velho é {nome} com {im} anos.')
if p != 0:
    print(f'Existem {p} mulheres com menos de 20 anos.')
print(f'A media das idades é de {m/(c+1)} anos.')

