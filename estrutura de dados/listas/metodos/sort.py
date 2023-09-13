# Ordenar em ordem alfabética

lista = ["Hi", "ola", "ana", "oi", "anao"]
lista.sort()

print(lista)


# Irá ordenar, porém de trás pra frente

lista = ["Hi", "ola", "ana", "oi", "anao"]
lista.sort(reverse=True)
print(lista)


# Ordenar por tamanho da palavra

lista = ["Hi", "ola", "ana", "oi", "anao"]
print(lista.sort(key=lambda x: len(x)))


print(lista)


lista = ["Hi", "ola", "ana", "oi", "anao"]
print(lista.sort(key=lambda x: len(x), reverse=True))

print(lista)
