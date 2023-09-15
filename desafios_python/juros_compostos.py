valor_inicial = float(input('Valor inicial: '))
taxa_juros = float(input('Taxa de juros: '))
periodo = int(input('Periodo em anos: '))

valor_final = valor_inicial

# TODO: Iterar, baseado no período em anos,
# para calculo do valorFinal com os juros.


def calcular_juros(*args):
    valor_final = valor_inicial * (1 + taxa_juros) ** periodo

    return print(f"Valor final do investimento: R$ {valor_final:.2f}")


calcular_juros()
