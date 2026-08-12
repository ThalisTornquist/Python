n1 = int(input("Qual sua nota? "))
n2 = int(input("Qual sua nota? "))

n1 = n1 * 4
n2 = n2 * 6
m = (n1 + n2) / 10
if m >= 5:
    print(f'Parabens! voce foi aprovado com a media de {m}.')
else:
    print(f'Voce foi reprovado com uma media de {m}')