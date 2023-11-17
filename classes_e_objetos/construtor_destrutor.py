'''
O método construtor é executado quando uma instância da classe é criada!
Assim, inicalizamos o estado do nosso objeto declarando o método construtor
da classe, sendo __init__

O método destrutor é executado quando uma instância é destruída!
O destrutor da classe declara-se por __del__. Caso a classe seja
chamada novamente, não retornará nada

'''


class Gato():
    def __init__(self, nome, cor, acordado=True):
        print('Inicializando a classe...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    # Executado ao final do processo
    def __del__(self):
        print('Removendo instância da classe')

    def miar(self):
        print('Miau')


cat = Gato('Meg', 'Laranja')
cat.miar()
del cat
