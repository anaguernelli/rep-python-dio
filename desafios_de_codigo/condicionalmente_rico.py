saldo_total = int(input("saldo "))
valor_saque = int(input("saque "))


def condicional_saque():
    saldo_disponivel = saldo_total
    if (saldo_disponivel >= valor_saque):
        saldo_disponivel -= valor_saque
        print(f"Saque realizado com sucesso! Novo saldo: {saldo_disponivel}")
    elif (saldo_disponivel <= valor_saque):
        print("Saldo insuficiente. Saque nao realizado!")


condicional_saque()
