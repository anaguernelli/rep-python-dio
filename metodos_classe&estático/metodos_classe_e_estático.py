'''
Se preciso ter acesso ao contexto da classe --> class method

Se não preciso de contexto nem da classe
ou da instância do objeto --> static method

'''


class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    # Para termos esse Método de fábrica, devemos
    # transformá-lo num método de classe
    # *A convenção é usar 'cls' em vez de 'self'
    @classmethod
    def criar_por_ano_nascimento(cls, ano, nome):
        idade = 2023 - ano
        return cls(nome, idade)

    # Método estático
    @staticmethod
    def is_maioridade(idade):
        return idade >= 18


pessoa1 = Pessoa('Ana', 12)
print(pessoa1.nome, pessoa1.idade)


pessoa2 = Pessoa().criar_por_ano_nascimento(2003, 'Anao')
print(pessoa2.nome, pessoa2.idade)

print(Pessoa.is_maioridade(21))
