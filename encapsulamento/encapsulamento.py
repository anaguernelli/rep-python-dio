'''
Encapsulamento é um conceitos fundamentais em POO. Sua ideia é
agrupar dados e os métodos que manipulam esses dados em uma unidade,
impondo assim, restrições ao acesso direto a variáveis e métodos
para evitar modificação acidental de dados. Então, a variável só pode
ser alterada pelo método do objeto.

*Em um diagrama, o atributo privado é demarcado por '-' e os públicos
pelo sinal de '+'

* Uma variável ou método iniciado com underscore, é uma convenção de que
não é para ser manipulado.
'''


class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def exibir_saldo(self):
        return self._saldo


conta_corrente = Conta('0001', 200)
conta_corrente.depositar(20)

print(conta_corrente.nro_agencia)
print(conta_corrente.exibir_saldo())
