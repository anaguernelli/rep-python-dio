'''
Separar funções existentes de saque, depósito e extrato em funções.
++ Criar duas novas funções: cadastrar usuário e cadastrar conta bancária

detalhamentos:
    Saque: keyword only.
    Depósito: positional only.
    Extrato: Ambos.
        Args posicionais: saldo,
        Args nomeados: extrato.

    Dica: Para vincular um usuario a uma conta,
    filtre a lista de usuarios por cpf

'''
import textwrap


def menu():
    menu = '''
    Qual operação deseja realizar?

    [1]\tDepósito
    [2]\tSaque
    [3]\tExtrato
    [4]\tCadastrar-me
    [5]\tCadastrar conta corrente
    [6]\tListar contas
    [7]\tSair

    =>
    '''

    return int(input(textwrap.dedent(menu)))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0.0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        escolha = menu()

        if escolha == 1:
            valor = float(input('Valor do depósito: '))

            saldo, extrato = deposito(saldo, valor, extrato)

        elif escolha == 2:
            valor = float(input('Valor do saque: '))

            saldo, extrato = saque(
                saldo=saldo,
                valor_saque=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif escolha == 3:
            saldo, extrato = visualizar_extrato(saldo, extrato=extrato)

        elif escolha == 4:
            cadastrar_usuario(usuarios)

        elif escolha == 5:
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif escolha == 6:
            listar_contas(contas)

        elif escolha == 7:
            print('Fim do programa.')
            break

        else:
            print('Comando inválido. Selecione novamente a operação desejada.')


def cadastrar_usuario(usuarios):
    cpf = input('Informe seu CPF (somente número): ')
    usuario = usuario_exists(cpf, usuarios)

    if usuario:
        print('Este usuario já existe!')
        # retorna pra função principal
        return

    # caso CPF não exista:
    nome = input('Nome: ')
    sobrenome = input('Sobrenome: ')
    data_nascimento = input('Data de nascimento (dd-mm-aaaa): ')
    logradouro = input('Logradouro: ')
    numero = input('Numero:')
    bairro = input('Bairro: ')
    cidade = input('Cidade: ')

    usuarios.append({
        "nome": nome,
        "sobrenome": sobrenome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "logradouro": logradouro,
        "numero": numero,
        "bairro": bairro,
        "cidade": cidade
        })

    print('=== Cadastro de usuário realizado com sucesso! ===')


def usuario_exists(cpf, usuarios):
    filtro = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    # retorna [0] pois só há um usuario com o cpf
    return filtro[0] if filtro else None


def cadastrar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe seu CPF (somente números): ')
    usuario = usuario_exists(cpf, usuarios)

    if usuario:
        print('=== Sua conta foi criada com sucesso! ===')
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
            }

    print('=== Usuário não encontrado. Por favor, cadastre seu usuário. ===')


def excluir_conta():
    ...


def listar_contas(contas):
    for conta in contas:
        listar = f'''
        Agencia: {conta['agencia']}\n
        C/C: {conta['numero_conta']}\n
        Titular: {conta['usuario']['nome']} {conta['usuario']['sobrenome']}\n
        '''

        print(listar)


# Keyword
def saque(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saques):
    saldo_excedido = valor_saque > saldo
    limite_excedido = valor_saque > limite
    saque_excedido = numero_saques >= limite_saques

    if saldo_excedido:
        print('Saldo insuficiente.')
    elif limite_excedido:
        print('Valor de saque excede o limite de R$ 500.00')
    elif saque_excedido:
        print('Limite diário de saques excedido.')
    elif valor_saque > 0:
        saldo -= valor_saque
        numero_saques += 1
        extrato += f'Saque:\t\t\tR${valor_saque:.2f}\n'

        print(f'Saque no valor de R${valor_saque:.2f} realizado com sucesso.')
    else:
        print('Valor inválido!')

    return saldo, extrato


# Positional
def deposito(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f'Depósito:\t\tR${valor_deposito:.2f}\n'

        print(f'Depósito no valor de R${valor_deposito:.2f} realizado com sucesso')
    else:
        print('Valor de depósito inválido')

    return saldo, extrato


def visualizar_extrato(saldo, /, *, extrato):
    print('=' * 15, 'EXTRATO', '=' * 15)
    print('Não foram realizadas movimentações.'
          if not extrato
          else extrato)
    print(f'\nSaldo atual:\t\tR$ {saldo:.2f}')

    return saldo, extrato


main()
