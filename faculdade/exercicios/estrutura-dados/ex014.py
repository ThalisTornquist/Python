while True:
    try:

        s = input('digite "saida" para sair do programa ')
        if s.lower() == 'saida' :
            break

        nome = input('Nome: ')

        with open('usuarios.txt', 'a') as arquivo:
            arquivo.write(nome +'\n')
        with open('usuarios.txt', 'r') as arquivo:
            usuarios = arquivo.read()

        print(usuarios)


    except Exception as erro:

        print(f'Ocorreu um erro: {erro}')