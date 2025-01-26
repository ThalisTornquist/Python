lista = [1, 3, 2, 4]

lista[3] = 8

lista.append(5)
print(lista)

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

lista.remove(8)
print(lista)

lista.pop(0)
print(lista)

lista.insert(1, 10)
print(lista)


print(sum(lista))