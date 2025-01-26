c = input('Digite o nome de uma cidade: ')

if c.split()[0].lower().find('santa') == -1:
    print('Sua cidade não começa com Santa.')
else:
    print('Sua cidade começa com Santa')