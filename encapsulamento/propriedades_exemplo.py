class Person:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        ano_atual = 2023

        return ano_atual - self._ano_nascimento


foo = Person('Ana', 2004)
print(f'Nome: {foo.nome}, Idade: {foo.idade}')
