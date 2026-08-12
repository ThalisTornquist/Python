def CriaTabela(M):
    tabela = {}
    for c in range(M):
        tabela[c] = None

    return tabela


def Dispersao(d, m):
    k = d % m
    return k


def Inserir(chave, dado, tabela):
     if tabela[chave] == None:
         tabela[chave] = dado
     else:
         print('erro')