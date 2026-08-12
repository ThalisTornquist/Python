class Livro:
    def __init__(self, nome, autor, paginas):
        self.nome = nome
        self.autor = autor
        self.paginas = paginas

    def Mostrar(self):
        print(f'Titulo: {self.nome}')
        print(f'Autor: {self.autor}')
        print(f'Paginas: {self.paginas}')


livro1 = Livro('got','thalis',250 )
livro1.Mostrar()