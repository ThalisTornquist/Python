import math

l = int(input('digite uma largura de um triangulo: '))
c = int(input('digite um comprimernto de um triangulo: '))

h = (l ** 2 + c ** 2) ** (1/2)

print(f'A hipotenusa desse triângulo é de {f"{h:g}" if h.is_integer() else f"{h:.2f}"}')
