import datetime

clt = {}

clt['nome'] = input('Qual seu nome? ')
clt['ano'] = int(input('Em que ano nasceu? '))
clt['idade'] = datetime.datetime.now().year - clt['ano']
clt['clt'] = int(input('Carteira de trabalho (0 se não tiver): '))
if clt['clt'] == 0:
    clt['clt'] = 'Não tem'
else:
    clt['contrato'] = int(input('Em que ano foi contratado? '))
    clt['aposentadoria'] = clt['contrato'] - clt['ano'] + 35
    clt['sal'] = float(input('Qual seu salario? '))

print()

print(f'O nome é {clt['nome']}')
print(f'Tem {clt['idade']} anos')
print(f'A CLT: {clt['clt']}')
if clt['clt'] != 'Não tem':
    print(f'Foi contratado em {clt['contrato']}')
    print(f'O salário é de R${clt['sal']:.2f}')
    print(f'Vai se aposentar com {clt['aposentadoria']} anos')

"""
for k, v in clt.items():
    print(f'{k} recebe {v}')
"""


