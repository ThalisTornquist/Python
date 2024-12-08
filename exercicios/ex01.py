# NÃO É O EX01 MAS DA NADA
import math


n = int(input('Digite um numero: '))
raiz = math.sqrt(n)

r = str(raiz)

if raiz.is_integer():
    print('A raiz quadrade do numero {} é {:g}'.format(n, raiz))

else:
    print('A raiz quadrade do numero {} é {:.2f}'.format(n, raiz))





