nome = input('Digite seu nome completo: ').strip()
ln = len(nome) - nome.count(' ')

print(f'Seu nome com maiusculas fica {nome.upper()}.')
print(f'Seu nome com minusculas fica {nome.lower()}.')
print(f'Seu nome tem {ln} letras.')
print(f'Seu primeiro nome tem {len(nome.split()[0])} letras.')