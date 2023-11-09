valor = float(input("valor "))

while True:
    if valor > 0:
        # TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
        print(f"Deposito realizado com sucesso! Saldo atual: R$ {valor:.2f}")
        break
    elif valor == 0:
        # TODO: Imprimir a mensagem de valor inválido.
        print("Encerrando o programa...")
        break
    else:
        # TODO: Imprimir a mensagem de encerrar o programa.
        print("Valor invalido! Digite um valor maior que zero.")
        break
