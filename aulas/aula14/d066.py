n = 0
s = 0
c = 0

print('Aperte 0 para sair.')
while True:
    n = int(input('Digite um numero: '))


    if n == 0:
        break

    s += n
    c += 1
print(f'Foram digitados {c} numeros, e soma é {s}.')
