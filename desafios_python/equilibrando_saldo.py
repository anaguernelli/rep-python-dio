'''
Descrição

Para esse desafio, considere que você foi contratado por uma empresa bancária
para auxiliar nas implementações e melhorias do sistema empresarial. Em uma
análise inicial, foi identificado pela equipe financeira a necessidade de
desenvolver uma solução que permita ao cliente equilibrar seu saldo bancário.
Dessa forma, o programa deve solicitar uma entrada que representa o saldo
atual do funcionário, e após, seja informado o valor de duas transações,
sendo elas: um depósito e um saque. O programa deve atualizar o saldo com
base nas transações e exibir o saldo final.

Informação: As transações de depósito e retirada devem ser tratadas como
valores positivos e negativos, respectivamente, para garantir que o cálculo
do saldo final seja realizado corretamente.

'''

saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())

# TO-DO: Calcular o saldo atualizado de acordo com a descrição deste desafio.

saida = (saldo_atual + valor_deposito) - valor_retirada

# TO-DO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).

print(f"Saldo atualizado na conta: {saida:.1f}")