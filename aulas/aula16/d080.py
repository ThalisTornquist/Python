l = []

for c in range(5):
    v = int(input("Digite um número: "))

    if c == 0:
        l.append(v)  # Adiciona o primeiro número diretamente
    elif v >= l[-1]:  # Se o número for maior ou igual ao último da lista
        l.append(v)
    elif v <= l[0]:  # Se o número for menor ou igual ao primeiro da lista
        l.insert(0, v)
    else:
        # Inserir o número na posição correta
        for i in range(len(l)):
            if v <= l[i]:
                l.insert(i, v)
                break

print(f"Os números em ordem crescente são: {l}")
