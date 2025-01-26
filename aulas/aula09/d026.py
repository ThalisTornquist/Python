f = input('Digite uma frase: ').strip()

print(f'A letra "A" apareceu {f.lower().count('a')} vezes nessa frase.')
print(f'Ela apareceu a primeira vez na posição {f.lower().find('a') + 1}.')
print(f'E ela apareceu pela ultima vez na posição {f.lower().rfind('a') + 1}')

