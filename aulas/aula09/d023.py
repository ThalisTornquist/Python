num = int(input('Digite um numero de 0 a 9999: '))
n = str(num)
l = len(n)


print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')