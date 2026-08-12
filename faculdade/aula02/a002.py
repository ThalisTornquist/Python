def combustivel_gasto(distancia, consumo):
    res = distancia / consumo
    return res

tempo = int(input())
vm = int(input())
consumo = int(input())

distancia = tempo * vm

combustivel = combustivel_gasto(distancia, consumo)

print(float(combustivel))
