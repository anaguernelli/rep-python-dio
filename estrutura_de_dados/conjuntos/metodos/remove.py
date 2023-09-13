# A diferença do remove pro discard, é que no discard dando
# um valor inexistente a execução não quebra, já no remove, sim

numeros = {1, 2, 3, 4, 5, 6, 7, 0}

print(numeros)

numeros.remove(0)
numeros.remove(3)

print(numeros)
