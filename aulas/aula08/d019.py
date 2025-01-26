import random

a1 = input('Digite o nome de um aluno: ')
a2 = input('Digite o nome de um aluno: ')
a3 = input('Digite o nome de um aluno: ')
a4 = input('Digite o nome de um aluno: ')

alunos = [a1, a2, a3, a4]
e = random.choice(alunos)

print(f'Entre os alunos {a1}, {a2}, {a3} e {a4}, o escolhido foi {e}.')