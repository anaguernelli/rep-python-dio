def criar_carro(modelo, ano, placa, /, *, marca, motor):
    print(modelo, ano, placa, marca, motor)


# Válido
criar_carro("Sandero", 2000, "ABC-882", marca="Fiat", motor="1.0")
