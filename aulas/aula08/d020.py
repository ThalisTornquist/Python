import random

a1 = input('Digite o nome de um aluno: ')
a2 = input('Digite o nome de um aluno: ')
a3 = input('Digite o nome de um aluno: ')
a4 = input('Digite o nome de um aluno: ')

alunos = [a1, a2, a3, a4]
e = random.sample(alunos, k=4)

print(f'A ordem de apresentação dos alunos {a1}, {a2}, {a3} e {a4}, ficou {e}.')