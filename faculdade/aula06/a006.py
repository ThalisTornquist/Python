class Fila:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.dados = [None] * tamanho
        self.inicio = 0
        self.fim = 0
        self.quantidade = 0

    def enfileirar(self, elemento):
        if self.quantidade < self.tamanho:
            self.dados[self.fim] = elemento
            self.fim = (self.fim + 1) % self.tamanho
            self.quantidade += 1
            print(f"Elemento {elemento} inserido.")
        else:
            print("Fila cheia!")

    def desenfileirar(self):
        if self.quantidade > 0:
            elemento = self.dados[self.inicio]
            self.dados[self.inicio] = None
            self.inicio = (self.inicio + 1) % self.tamanho
            self.quantidade -= 1
            print(f"Elemento {elemento} removido.")
        else:
            print("Fila vazia!")

    def consultar(self):
        if self.quantidade > 0:
            print(f"Primeiro elemento da fila: {self.dados[self.inicio]}")
        else:
            print("Fila vazia!")

    def contar(self):
        print(f"A fila possui {self.quantidade} elementos.")

    def exibir(self):
        print("Fila:", self.dados)



def main():
    tamanho = int(input("Defina o tamanho da fila: "))
    fila = Fila(tamanho)

    while True:
        print("\n=== MENU DA FILA ===")
        print("1 - Enfileirar (Adicionar)")
        print("2 - Desenfileirar (Remover)")
        print("3 - Consultar o primeiro elemento")
        print("4 - Contar elementos")
        print("5 - Exibir fila completa")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            elemento = input("Digite o elemento para adicionar à fila: ")
            fila.enfileirar(elemento)
        elif opcao == "2":
            fila.desenfileirar()
        elif opcao == "3":
            fila.consultar()
        elif opcao == "4":
            fila.contar()
        elif opcao == "5":
            fila.exibir()
        elif opcao == "0":
            print("Encerrando o programa")
            break
        else:
            print("Opção inválida! Tente novamente.")
main()