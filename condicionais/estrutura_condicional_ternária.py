saldo = 500
saque = 600

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")