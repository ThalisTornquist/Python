def prosessamento(entrada, saida):
    try:
        with open(entrada, 'r') as arquivo_entrada:
            conteudo = arquivo_entrada.read()

        if 'a' in conteudo:
            conteudo_codificado = cripto(conteudo)

        else:
            conteudo_codificado = descripto(conteudo)

        with open(saida, 'w') as arquivo_saida:
            arquivo_saida.write(conteudo_codificado)

        print('Arquivo codificado!')

    except FileNotFoundError:
        print('Arquivo não encontrado.')
    except Exception as e:
        print(f'Erro inesperado: {e}')

def cripto(texto):
    resultado = ''

    for c in texto:
        if c in 'Aa':
            resultado += '!'
        elif c in 'Ee':
            resultado += '@'
        elif c in 'Ii':
            resultado += '#'
        elif c in 'oO':
            resultado += '$'
        elif c in 'Uu':
            resultado += '%'
        else:
            resultado += c
    return resultado

def descripto(texto):
    resultado = ''

    for c in texto:
        if c in '!':
            resultado += 'a'
        elif c in '@':
            resultado += 'e'
        elif c in '#':
            resultado += 'i'
        elif c in '$':
            resultado += 'o'
        elif c in '%':
            resultado += 'u'
        else:
            resultado += c
    return resultado


arquivo_entrada = input('Digite o nome do arquivo de entrada: ')

arquivo_saida = input('Digite o nome do arquivo de saída: ')

prosessamento(arquivo_entrada, arquivo_saida)