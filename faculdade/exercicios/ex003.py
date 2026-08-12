


def primo(num):
    c = 0
    i = 0
    if num % 2 == 0 and num != 2 and num != 1:
        print(f'Esse numero nao é primo. {num}')
    else:
        while i < num:
            i += 1
            if num % i == 0:
                c += 1

        if c == 2 or num == 1:

            return print(f'Esse numero é primo! {num}')
        else:
            print(f'Esse numero nao é primo. {num}')
for n in range(1, 100):
    if not primo(n):
        continue
    print(n)

