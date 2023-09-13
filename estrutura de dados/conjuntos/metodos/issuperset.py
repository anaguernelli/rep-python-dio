conjunto_1 = {1, 2, 3}
conjunto_2 = {1, 3, 4, 2, 5, 6, 7}

# Se todos elementos de 2 está em 1
print(conjunto_1.issuperset(conjunto_2))    # False

# Se todos elementos de 1 está em 2
print(conjunto_2.issuperset(conjunto_1))    # True
