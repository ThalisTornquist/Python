idades = [20, 25, 30, 35]

def trocar():

    cont = 0
    for c in idades:
        idades[cont] = c + 5
        cont += 1

trocar()
print(idades)

