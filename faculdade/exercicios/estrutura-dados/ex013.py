while True:
    try:
        idade = int(input('Digite sua idede: '))

        if idade <= 0:
            print('idede invalida')
            continue

        print('Idade cadastrada')
        break
    except ValueError:
            print('Digite apenas numeros')