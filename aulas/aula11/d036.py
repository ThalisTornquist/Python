vc = float(input('Digite o valor da casa: '))
s = float(input('Digite seu salário: '))
a = int(input('Em quantos anos quer pagar? '))

sp = s * 0.3
va = vc / a
vm = va / 12

if sp >= vm:
    print(f'Você pode comprar a casa, e pagara R${f'{vm:.2f}'} por mês.')
else:
    print(f'Infelizmente voce nao podera comprar essa casa, as prestaçoes ficam de R${f'{vm:.2f}'} e ultrapassam 30% de seu salario!')

