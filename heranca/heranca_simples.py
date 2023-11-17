'''
Herança dá a possibilidade de reutilização do código. Além disso,
Permite adicionar mais recursos a uma classe sem modificá-la.

é de natureza transitiva, ou seja, se a classe B herda da classe A,
todas as subclasses de B herdarão automaticamente de A.

Na herança simples a classe filha herda apenas de uma classe pai
Na herança múltipla a classe filha herda de várias classes pai
'''

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('O motor está sendo ligado...')

    def __str__(self):
        return f'{self.__class__.__name__}: \
{', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}'


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        # Para continuar usando oq tem em Veiculo
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def is_carregado(self):
        print(f'{'Sim,' if self.carregado else 'Não'} está carregado...')


class Caminhao(Veiculo):
    pass


moto = Motocicleta("preta", "555-777", 2)
print(moto)
moto.ligar_motor()

carro = Carro("prata", "668=223", 6, True)
carro.ligar_motor()
carro.is_carregado()
