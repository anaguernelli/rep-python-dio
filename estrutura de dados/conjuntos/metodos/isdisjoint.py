conjunto_1 = {1, 2, 3}
conjunto_2 = {6, 7}
conjunto_3 = {1, 0}

# Verifica se todos os elementos de um conjunto não
# estão presentes no outro conjunto

# Não se "tocam"

print(conjunto_1.isdisjoint(conjunto_2))    # True
print(conjunto_1.isdisjoint(conjunto_3))    # False
