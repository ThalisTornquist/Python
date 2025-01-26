f = input('Digite uma frase: ').lower().split()
jf = ''.join(f)

if jf == jf[::-1]:
    print('E um palindromo!')
else:
    print('Nao é um palindromo')
