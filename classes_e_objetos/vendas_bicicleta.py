# class Bicicleta:
#     pass


class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        # self é a referência/instância pro objeto
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('BIBI...')

    def parar(self):
        print('Parando...')

    def correr(self):
        print('Correndo...')

    # def __str__(self):
    #     return f'Bicicleta: cor={self.cor} modelo={self.modelo} \
    #     ano={self.ano} valor={self.valor}'

    def __str__(self):
        return f'{self.__class__.__name__} \
{' '.join([f'{chave}= {valor}' for chave, valor in self.__dict__.items()])}'


b1 = Bicicleta("preta", "caloi", "2023", "800")

b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor, b1.modelo, b1.valor)

Bicicleta.buzinar(b1)
print(b1)
