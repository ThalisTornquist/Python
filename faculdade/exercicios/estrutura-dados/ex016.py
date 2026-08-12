import json
try:
    with open('usuarios.json', 'r') as arquivo:
        usuarios = json.load(arquivo)

except (FileNotFoundError, json.JSONDecodeError):
    usuarios = []

nome = input('Digite seu nome: ')
idade = int(input('digite sua idade: '))

usuarios.append({
    'nome': nome,
    'idade': idade
})

with open('usuarios.json', 'w') as arquivo:
    json.dump(usuarios, arquivo, indent=4)


for usuario in usuarios:
    print(f'Nome: {usuario["nome"]} \nIdade: {usuario["idade"]}')