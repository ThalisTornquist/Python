import json

def entradas():
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    u_existe = False

    try:
        with open('arquivo_usuarios.json', 'r') as arquivo:
            usuarios = json.load(arquivo)
            for linha in usuarios:
                if linha['nome'].lower() == nome.lower():
                    u_existe = True
                    break
    except (FileNotFoundError, json.JSONDecodeError):
        usuarios = []

    if u_existe:
        print('Esse usuario ja esta cadastrado! ')
    else:
        print('Novo usuario cadastrado')
        usuarios.append(
            {
                'nome': nome,
                'idade': idade
            }
        )
        with open('arquivo_usuarios.json', 'w') as arquivo:
            json.dump(usuarios, arquivo, indent=4)



def remover(nome_remover):
    encontrado = False
    linhas = []

    with open('arquivo_usuarios.json', 'r') as arqui:
        arquivo = json.load(arqui)
        for linha in arquivo:

            if linha['nome'].lower() == nome_remover.lower():
                encontrado = True
            else:
                linhas.append(linha)

    with open('arquivo_usuarios.json', 'w') as arquivo:
        json.dump(linhas, arquivo, indent=4)

    if encontrado:
        print('Usuario removido! ')
    else:
        print('Usuario não encontrado')



def mostrar():
        c = 0
        with open('arquivo_usuarios.json', 'r') as arqui:
            arquivo = json.load(arqui)
            for linha in arquivo:
                c += 1
                print(f'Nome: {linha['nome']} \n Idade: {linha['idade']}')
            print(f'O total de usuarios é de {c}')


def alterar_idade(nome_idade_alterar):
    encontrado = False
    linhas = []
    nova_idade = int(input('Digite a nova idade: '))

    with open('arquivo_usuarios.json', 'r') as arqui:
        arquivo = json.load(arqui)
        for linha in arquivo:

            if linha['nome'].lower() == nome_idade_alterar.lower():
                encontrado = True
                linhas.append({
                    'nome': linha['nome'],
                    'idade': nova_idade
                })
            else:
                linhas.append(linha)

    with open('arquivo_usuarios.json', 'w') as arquivo:
        json.dump(linhas, arquivo, indent=4)

    if encontrado:
        print('Idade atualizada! ')
    else:
        print('Usuario não encontrado')



def buscar(nome_buscar):
    encontrado = False

    with open('arquivo_usuarios.json', 'r') as arqui:
        arquivo = json.load(arqui)
        for linha in arquivo:
            if linha['nome'].lower() == nome_buscar.lower():
                encontrado = True
                print(f'{linha['nome']} tem {linha['idade']} anos de idade.')

    if not encontrado:
        print('Usuario não encontrado! ')

while True:
    try:

        s = input('"s" para sair do programa \n"b" para buscar usuario\n"a" para mostrar a lista \n"t" para atualizar idade \n"r" para remover um usuario \n"c" para continuar cadastro\n ')

        if s.lower() == 's' :
            break
        elif s.lower() == 'a':
            mostrar()
        elif s.lower() == 'r':
            remover(input('Didite um nome para ser removido: '))
        elif s.lower() == 'c':
            entradas()
        elif s.lower() == 't' :
            alterar_idade(input('Digite o nome do usuario que quer atualizar a idade: '))
        elif s.lower() == 'b':
            buscar(input('Digite um nome para ser buscado: '))
        else:
            print('opcao invalida')

    except Exception as erro:
        print(f'Ocorreu um erro: {erro}')

