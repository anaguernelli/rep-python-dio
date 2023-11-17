class Estudante:
    escola = 'Escola'

    def __init__(self, nome, matricula) -> None:
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f'{self.nome} - {self.matricula} - {self.escola}'


def exibir_valores(*args):
    for arg in args:
        print(arg)


estudante1 = Estudante('Ana', 1)
estudante2 = Estudante('Beatriz', 2)

exibir_valores(estudante1, estudante2)

# Percebe-se que o nome da escola passa a ser outro
Estudante.escola = 'Outra escola'

estudante3 = Estudante('Pedro', 3)
exibir_valores(estudante3)
