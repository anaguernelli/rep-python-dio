conjunto_1 = {1, 2, 3}
conjunto_2 = {1, 3, 4, 2, 5, 6, 7}

# Verifica se todos os elementos do
# conjunto_1 está em conjunto_2 e vice-versa

print(conjunto_1.issubset(conjunto_2))  # True
print(conjunto_2.issubset(conjunto_1))  # False
