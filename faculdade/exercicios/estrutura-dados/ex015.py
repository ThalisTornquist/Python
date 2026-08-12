def entradas():
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    usuarios = {}
    usuarios = {
        'nome': nome,
        'idade': idade
    }
    cadastro(usuarios)
    return usuarios



def cadastro(usuarios):
    u_existe = False
    with open('usuarios.txt', 'r') as arquivo:
        for linha in arquivo:
            nome_arquivo, idade_arquivo = linha.strip().split(';')

            if usuarios['nome'].lower() == nome_arquivo.lower():
                u_existe = True
                break

    if u_existe:
        print('Esse usuario ja esta cadastrado! ')
    else:
        print('Novo usuario cadastrado')

        with open('usuarios.txt', 'a') as arquivo:
            arquivo.write(f'{usuarios["nome"]};{usuarios["idade"]}\n')



def remover(nome_remover):
    encontrado = False
    linhas = []

    with open('usuarios.txt', 'r') as arquivo:
        for linha in arquivo:
            nome_arquivo, idade_arquivo = linha.strip().split(';')

            if nome_arquivo.lower() == nome_remover.lower():
                encontrado = True
            else:
                linhas.append(linha)

    with open('usuarios.txt', 'w') as arquivo:
        for linha in linhas:
            arquivo.write(linha)

    if encontrado:
        print('Usuario removido! ')
    else:
        print('Usuario não encontrado')



def mostrar():
        c = 0
        with open('usuarios.txt', 'r') as arquivo:
            for linha in arquivo:
                c += 1
                nome, idade = linha.strip().split(';')
                print(f'Nome: {nome} \n Idade: {idade}')
            print(f'O total de usuarios é de {c}')

def alterar_idade(nome_idade_alterar):
    encontrado = False
    linhas = []
    nova_idade = int(input('Digite a nova idade: '))

    with open('usuarios.txt', 'r') as arquivo:
        for linha in arquivo:
            nome_arquivo, idade_arquivo = linha.strip().split(';')

            if nome_arquivo.lower() == nome_idade_alterar.lower():
                encontrado = True
                linhas.append(f'{nome_arquivo};{nova_idade}\n')

            else:
                linhas.append(linha)

    with open('usuarios.txt', 'w') as arquivo:
        for linha in linhas:
            arquivo.write(linha)

        if encontrado:
            print('Idade atualizada! ')
        else:
            print('Usuario não encontrado')



def buscar(nome_buscar):
    encontrado = False

    with open('usuarios.txt', 'r') as arquivo:
        for linha in arquivo:
            nome_arquivo, idade_arquivo = linha.strip().split(';')

            if nome_arquivo.lower() == nome_buscar.lower():
                encontrado = True
                print(f'{nome_arquivo} tem {idade_arquivo} anos de idade.')

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

