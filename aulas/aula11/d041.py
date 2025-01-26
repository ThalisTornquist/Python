a = int(input('Em que ano voce nasceu? '))

i = 2024 - a

if i <= 9:
    print('Sua categoria é mirim')
elif i <= 14:
    print('Sua categoria é Infantil')
elif i <= 19:
    print('Sua categoria é Junior')
elif i == 20:
    print('Sua categoria é Senior')
elif i > 20:
    print('Sua categoria é Master')
else:
    print('Sua idade é invalida.')

