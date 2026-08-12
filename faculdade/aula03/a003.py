
def cadastro(n):
    'Função que cadastra as frutas e seus preços.'

    l = [] # declaração de lista vazia para usarmos futuramente
    for c in range(n): # loop para repetir o numero de vezes desejado pelo usuario

        '''variaveis para o usuario definir'''
        fruta = input().lower() # pergunta ao usuario o nome dafruta
        preco = float(input()) # perngunta o preço da fruta

        '''verifica se a fruta ja foi cadastrada, caso não tenha o cadastro a lista recebe os novos elementos.'''
        if fruta in l[::2]:
            print('Produto já cadastrado') # imprime para o usuario que ja havia o cadastro
        else:
            l.append(fruta) # cadastra nova fruta
            l.append(preco) # cadastra o preço da fruta
    return l # retorna a lista com os novos elementos

def busca(l):
    'Função para buscar o nome da fruta dentro da lista e mostrar seu preço caso haja cadastro.'

    '''Cria um loop infinito que só acaba quando o usuario digita fim'''
    while True:
        fruta = input().lower() # pergunta ao usuario o nome da fruta
        if fruta == 'fim': # verifica se o usuario que continuar n loop
             break # quebra o loop

        if fruta in l[::2]: #busca a fruta dentro da lista
            indice = l.index(fruta) # acha a posição da fruta dento da lista
            print(l[indice + 1]) # adiciona um na posisao da fruta para ter seu respectivo preço e imprime
        else: # caso o usuario digite uma fruta nao cadastrada imprime a mensagem abaixo
            print('Produto não cadastrado')



n = int(input()) #pergunta o valor de frutas que o usuario que cadastrar
l = cadastro(n) # inicializa a função cadastro com paramentro de 'n'
busca(l) # inicializa a função busca com paramentro de 'l'
