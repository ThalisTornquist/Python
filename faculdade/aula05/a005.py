import random

lista = []
par = []
impar = []

for c in range(100):

    numero = random.randint(1, 1000)
    lista.append(numero)

for i in lista:

    if i % 2 == 0:
        par.append(i)

    else:
        impar.append(i)

print(lista)
print(par)
print(impar)