# O mesmo que sort(), a diferenã é que sorted() é uma função

lista = ["Hi", "ola", "ana", "oi", "anao"]

print(sorted(lista, key=lambda x: len(x)))
print(sorted(lista, key=lambda x: len(x), reverse=True))
print(sorted(lista))
