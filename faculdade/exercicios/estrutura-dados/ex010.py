class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco < 0:
            print('Preco invalido')
        else:
            self.__preco = novo_preco

    def __str__(self):
        return f'{self.nome} - R$ {self.preco:.2f}'


class Carrinho:

    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, nome, preco):
        self.produtos.append(Produto(nome, preco))

    def remover_produto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                self.produtos.remove(produto)
                break

    def total(self):
        total = 0

        for produto in self.produtos:
            total += produto.preco

        return total

    def mostrar(self):
        for produto in self.produtos:
            print(produto)

    def __str__(self):

        return f'Carrinho contem {len(self.produtos)} produtos - Total R$ {self.total():.2f}'


carrinho = Carrinho()
carrinho.adicionar_produto('batata', 50)
carrinho.adicionar_produto('pc', 2000)
carrinho.adicionar_produto('carne', 100)






carrinho.produtos[0].preco = 120
carrinho.remover_produto('pc')

carrinho.mostrar()

print(carrinho)