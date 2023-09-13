# Vai elevar ao quadrado o valor para cada numero em numeros

numeros = [1, 2, 4, 5, 7, 8, 99, 10, 12]
quadrado = [numero ** 2 for numero in numeros]

print(quadrado)


# Vai elevar ao quadrado numeros maiores que 6
# Do contrário, vai pegar números pares do range

pares = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]

print(pares)
