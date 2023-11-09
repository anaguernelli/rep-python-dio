menu = '''
Qual operação deseja realizar?

[1] Depósito
[2] Saque
[3] Extrato
[4] Sair

=>
'''

saldo = 0.0
limite = 500
extrato = ''
cont_saques = 0
LIMITE_SAQUES = 3


while True:
    escolha = int(input(menu))

    if escolha == 1:
        valor = float(input('Valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R${valor:.2f}\n'
            print(f'Depósito no valor de R${valor:.2f} realizado com sucesso')

        else:
            print('Valor de depósito inválido')

    elif escolha == 2:
        valor = float(input('Valor do saque: '))
        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saque_excedido = cont_saques >= LIMITE_SAQUES

        if saldo_excedido:
            print('Saldo insuficiente.')

        elif limite_excedido:
            print('Valor de saque excede o limite de R$ 500.00')

        elif saque_excedido:
            print('Limite diário de saques excedido.')

        elif valor > 0:
            saldo -= valor
            cont_saques += 1
            extrato += f'Saque: R${valor:.2f}\n'
            print(f'Saque no valor de R${valor:.2f} realizado com sucesso.')

        else:
            print('Valor inválido!')

    elif escolha == 3:
        print('=' * 10, 'EXTRATO', '=' * 10)
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo atual: R$ {saldo:.2f}')

    elif escolha == 4:
        print('Fim do programa.')
        break

    else:
        print('Comando inválido. Selecione novamente a operação desejada.')
