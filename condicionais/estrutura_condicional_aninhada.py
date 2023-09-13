conta_normal = False
conta_universitaria = False
conta_especial = False

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque por saldo insuficiente.")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif conta_especial:
    print("A conta especial foi selecionada.")

else:
    print("""
          Sistema não reconhece seu tipo de conta,
          entre em contato com o gerente.
          """)
