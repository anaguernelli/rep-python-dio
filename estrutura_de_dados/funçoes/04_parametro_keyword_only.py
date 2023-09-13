# Do contrário do positional only, aqui somente aceita
# Parêmtros passando o nome

def criar_carro(*, modelo, ano, placa, marca, motor):
    print(modelo, ano, placa, marca, motor)


# Inválido
# criar_carro("Sandero", 2000, "ABC-882", marca="Fiat", motor="1.0")

# Válido
criar_carro(modelo="Sandero", ano=2000, placa="ABC-882", marca="Fiat", motor="1.0")
