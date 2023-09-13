def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def exibir_resultado(a, b, atribuir_funcao):
    resultado = atribuir_funcao(a, b)
    print(f"O resultado da operação é {a} e {b} é {resultado}")


exibir_resultado(10, 20, somar)
