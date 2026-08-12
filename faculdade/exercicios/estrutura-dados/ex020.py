import sqlite3



class Sistema_Usuario:

    def __init__(self):
        self.conexao = sqlite3.connect('usuarios_arquivo_sql.db')
        self.cursor = self.conexao.cursor()

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS usuarios_arquivo_sql(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome TEXT NOT NULL UNIQUE,
                idade INTEGER NOT NULL CHECK(idade >= 0)
                )  
            '''
        )
        self.conexao.commit()



    def cadastro(self):
        nome = input('Digite seu nome: ')
        idade = int(input('Digite sua idade: '))

        try:
            self.cursor.execute("""
                INSERT INTO usuarios_arquivo_sql(nome, idade)
                VALUES(?, ?)
            """, (nome, idade))

            self.conexao.commit()
        except sqlite3.IntegrityError:
            print('Valores invalidos! ')


    def mostrar(self):

        while True:

            nres = input(
                '''
                Como voce gostaria de visuarisar?
                [A] - PARA ORDEM ALFABETICA
                [B] - PARA ORDEM DO MAIS NOVO
                [C] - PARA ORDEM DO MAIS VELHO
                [D] - PARA ORDEM DE IMPLEMENTAÇÃO
                ''' )

            if nres.lower() == 'a':
                self.mostrar_alfabetica()
                break
            elif nres.lower() == 'b':
                self.mostrar_cresente()
                break
            elif nres.lower() == 'c':
                self.mostrar_decresente()
                break
            elif nres.lower() == 'd':
                self.mostrar_implementacao()
                break
            else:
                print('opcao invalidade')

    def mostrar_implementacao(self):
        self.cursor.execute("""
        SELECT * FROM  usuarios_arquivo_sql
        """)

        usuarios_arquivo = self.cursor.fetchall()
        self.loop(usuarios_arquivo)

    def mostrar_alfabetica(self):

        self.cursor.execute("""
        SELECT * FROM  usuarios_arquivo_sql
        ORDER BY nome
        """)

        usuarios_arquivo = self.cursor.fetchall()
        self.loop(usuarios_arquivo)

    def mostrar_cresente(self):
        self.cursor.execute("""
        SELECT * FROM  usuarios_arquivo_sql
        ORDER BY idade
        """)

        usuarios_arquivo = self.cursor.fetchall()
        self.loop(usuarios_arquivo)

    def mostrar_decresente(self):
        self.cursor.execute("""
        SELECT * FROM  usuarios_arquivo_sql
        ORDER BY idade DESC
        """)

        usuarios_arquivo = self.cursor.fetchall()
        self.loop(usuarios_arquivo)



    def loop(self, usuarios_arquivo):
        for usuarios in usuarios_arquivo:
            print(f'Nome: {usuarios[1]}')
            print(f'Idade: {usuarios[2]}')
            print(f'Id: {usuarios[0]}')
        print(f'Existem {len(usuarios_arquivo)} usuarios.')

    def buscar(self):

        id = input('digite o ID a ser buscado: ')

        self.cursor.execute("""
        SELECT * FROM  usuarios_arquivo_sql
        WHERE id = ?
        """, (id, ))

        usuario_arquivo = self.cursor.fetchone()
        if usuario_arquivo:
            print(f'O usuario {usuario_arquivo[1]} tem {usuario_arquivo[2]} anos. Seu ID é : {usuario_arquivo[0]}')
        else:
            print('Usuario não encontrado! ')

    def buscar_parte(self):
        nome = input('Digite a parte do nome a ser buscado: ')

        self.cursor.execute(
            '''
        SELECT * FROM  usuarios_arquivo_sql
        WHERE nome LIKE ?
        ORDER BY nome
            ''', (f"%{nome}%",)
        )
        usuario_arquivo = self.cursor.fetchall()

        if usuario_arquivo:
            self.loop(usuario_arquivo)
        else:
            print('Nenhum usuario encontrado! ')

    def alterar_idade(self):
        id = input('Digite o ID do usuario a ser atualizado: ')
        idade_nova = int(input('Digite a nova idade: '))

        self.cursor.execute(
            """
            UPDATE usuarios_arquivo_sql
            SET idade = ?
            WHERE id = ?""", (idade_nova, id)
        )

        self.conexao.commit()

        if self.cursor.rowcount == 0:
            print('Usuario nao encontrado')
        else:
            print('Idade atualizada! ')


    def remover(self):
        id = input('Digite o ID do usuario a ser removido: ')

        self.cursor.execute(
            '''
            DELETE FROM usuarios_arquivo_sql
            WHERE id = ?
            ''', (id, )
        )

        self.conexao.commit()

        if self.cursor.rowcount == 0:
            print('Usuario nao encontrado')
        else:
            print('Usuario removido! ')

    def fechar(self):
        self.conexao.close()


sistema = Sistema_Usuario()

while True:
    try:

        res = input(
            '"s" para sair do programa\n'
            '"b" para buscar usuario\n'
            '"a" para mostrar a lista\n'
            '"t" para atualizar idade\n'
            '"r" para remover um usuario\n'
            '"c" para continuar cadastro\n'
            '"p" para buscar por parte do nome\n'
        )

        if res.lower() == 's':
            sistema.fechar()
            break

        elif res.lower() == 'a':
            sistema.mostrar()

        elif res.lower() == 'r':
            sistema.remover()

        elif res.lower() == 'c':
            sistema.cadastro()

        elif res.lower() == 't':
            sistema.alterar_idade()

        elif res.lower() == 'b':
            sistema.buscar()

        elif res.lower() == 'p':
            sistema.buscar_parte()

        else:
            print('Opcao invalida')

    except Exception as erro:
        print(f'Ocorreu um erro: {erro}')