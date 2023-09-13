opcao = -1

# pois 0 é o comando que finalizará a exec
while opcao != 0:
    opcao = int(input("[1] Saque \n[2] Extrato \n[0] Sair -> "))

    if opcao == 1:
        print("Sacando")
    elif opcao == 2:
        print("Exibindo extrato")

else:
    print("Fim da execução")
