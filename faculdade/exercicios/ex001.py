a = float(input('Qual é sua altura? '))
sexo = input('Qual é seu sexo? "m" para masculino e "f" para femenino ').lower()

if sexo == 'm':
    peso = (a * 72.7) - 58

else:
    peso = (a * 62.1) - 44.7

print(f'Seu peso ideal é {peso}kg.') 