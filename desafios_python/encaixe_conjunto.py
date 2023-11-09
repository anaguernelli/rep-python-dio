n = int(input())


while (n > 0):
    entradas = input()
    entradas_split = entradas.split(' ')

    a = entradas_split[0]
    b = entradas_split[1]

    len_a = len(a)
    len_b = len(b)

    final = a[len_a - len_b::]

    if(final == b):
        print("encaixa")
    else:
        print("nao encaixa")

    n -= 1
