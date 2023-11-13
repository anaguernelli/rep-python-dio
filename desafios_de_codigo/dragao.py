C = int(input('casos de teste: '))


for i in range(C):
    entradas = input('entradas: ')

    if int(entradas) <= 8000:
        print('inseto')
    else:
        print('not inseto')
