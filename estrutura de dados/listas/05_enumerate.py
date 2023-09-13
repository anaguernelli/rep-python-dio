# Às vezes é necessário saber qual o índice do objeto dentro do laço for
# Para isso, podemos usar afunção enumerate

carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice} - {carro}")
