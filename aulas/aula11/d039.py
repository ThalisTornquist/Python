a = int(input('Em que ano voce nasceu? '))

i = 2024 - a

if i < 18:
    t = 18 - i
    print(f'Faltam {t} anos para o seu alistamento.')
elif i == 18:
    print('Esse ano voce presisa se alistar.')
else:
    t = i - 18
    print(f'Você se alistou a {t} anos atras.')