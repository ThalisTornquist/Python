
n = 0
num = int(input('Digite um numero: '))
for c in range(2, num, 1):
    if num % c != 0:
        n += 1




if n == num - 2:
    print('É primo!')
else:
    print('Nao é primo!')