n = 0
c = 0
num = 0
while n != 999:
    c += 1
    n = int(input('Digite um numero: '))
    num += n

print(f'Foram dogitados {c-1} numeros e a soma é {num-999}')