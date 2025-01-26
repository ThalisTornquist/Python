t = (
    "Botafogo", "Palmeiras", "Flamengo", "Atlético-MG", "Grêmio",
    "Fluminense", "São Paulo", "Internacional", "Fortaleza", "Cruzeiro",
    "Atlético-PR", "Bragantino", "Corinthians", "Santos", "Cuiabá",
    "Bahia", "Vasco", "Goiás", "Chapecoense", "Coritiba"
)

print('o top 5 é: ')
for c in range(0,5):
    print(f'na {c+1} posisao {t[c]}.')


print('-'*40)


print('Os ultimos 4 sao: ')

for c in range(16, len(t)):
    print(f'Na {c+1} posisao {t[c]}')


print('-'*40)


print('Em ordem alfabetica: ')

o = sorted(t)
for c in o:
    print(c)


print('-'*40)


print(f'A chapecoence esta na posisao {t.index('Chapecoense')+1}')