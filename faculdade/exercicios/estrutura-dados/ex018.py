import json

class SistemaUsuario():

    def __init__(self):
        self.arquivo = 'arquivo_usuarios.json'

    def carregar(self):
        try:
            with open(self.arquivo, 'r') as arquivo:
                return json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def salvar(self, usuarios):
        with open(self.arquivo, 'w') as arquivo:
            json.dump(usuarios, arquivo, indent=4)

    def entradas(self):
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        u_existe = False

        usuarios_arquivo = self.carregar()

        for usuario in usuarios_arquivo:
            if usuario['nome'].lower() == nome.lower():
                u_existe = True
                break

        if u_existe:
            print('Esse usuario ja esta cadastrado!')
        else:
            print('Novo usuario cadastrado')
            usuarios_arquivo.append(
                {
                    'nome': nome,
                    'idade': idade
                }
            )
            self.salvar(usuarios_arquivo)

    def remover(self, nome_remover):
        encontrado = False
        lista_linhas = []

        usuarios_arquivo = self.carregar()

        for usuario in usuarios_arquivo:

            if usuario['nome'].lower() == nome_remover.lower():
                encontrado = True
            else:
                lista_linhas.append(usuario)

        self.salvar(lista_linhas)

        if encontrado:
            print('Usuario removido!')
        else:
            print('Usuario não encontrado')

    def mostrar(self):
        c = 0
        usuarios_arquivo = self.carregar()

        for usuario in usuarios_arquivo:
            c += 1
            print(f"Nome: {usuario['nome']}\nIdade: {usuario['idade']}")

        print(f'O total de usuarios é de {c}')

    def alterar_idade(self, nome_idade_alterar):
        encontrado = False
        lista_linhas = []
        nova_idade = int(input('Digite a nova idade: '))

        usuarios_arquivo = self.carregar()

        for usuario in usuarios_arquivo:

            if usuario['nome'].lower() == nome_idade_alterar.lower():
                encontrado = True
                lista_linhas.append({
                    'nome': usuario['nome'],
                    'idade': nova_idade
                })
            else:
                lista_linhas.append(usuario)

        self.salvar(lista_linhas)

        if encontrado:
            print('Idade atualizada!')
        else:
            print('Usuario não encontrado')

    def buscar(self, nome_buscar):
        encontrado = False

        usuarios_arquivo = self.carregar()

        for usuario in usuarios_arquivo:
            if usuario['nome'].lower() == nome_buscar.lower():
                encontrado = True
                print(f"{usuario['nome']} tem {usuario['idade']} anos de idade.")

        if not encontrado:
            print('Usuario não encontrado!')


sistema = SistemaUsuario()

while True:
    try:

        s = input(
            '"s" para sair do programa\n'
            '"b" para buscar usuario\n'
            '"a" para mostrar a lista\n'
            '"t" para atualizar idade\n'
            '"r" para remover um usuario\n'
            '"c" para continuar cadastro\n'
        )

        if s.lower() == 's':
            break
        elif s.lower() == 'a':
            sistema.mostrar()
        elif s.lower() == 'r':
            sistema.remover(input('Digite um nome para ser removido: '))
        elif s.lower() == 'c':
            sistema.entradas()
        elif s.lower() == 't':
            sistema.alterar_idade(input('Digite o nome do usuario que quer atualizar a idade: '))
        elif s.lower() == 'b':
            sistema.buscar(input('Digite um nome para ser buscado: '))
        else:
            print('Opcao invalida')

    except Exception as erro:
        print(f'Ocorreu um erro: {erro}')