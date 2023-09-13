ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input("informe a quantidade de ativos: "))

# Entrada dos códigos dos ativos
for i in range(quantidadeAtivos):
    codigoAtivo = input("Informe os ativos: ")
    ativos.append(codigoAtivo)


# TODO: Ordenar os ativos em ordem alfabética.

def ordenar():
    ativos_em_ordem = sorted(ativos)
    ativos_clean = '\n'.join(map(str, ativos_em_ordem))

    return print(ativos_clean)

# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.


ordenar()
