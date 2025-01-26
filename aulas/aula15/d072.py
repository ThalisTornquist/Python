n = int(input('Digite um numero de 0 a 20: '))

while n > 20 or n < 0:
    n  = int(input('Tente novamente! Digite um numero de 0 a 20: '))

l = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete",
    "dezoito", "dezenove", "vinte"
)

print(f'Você digitou {l[n]}')