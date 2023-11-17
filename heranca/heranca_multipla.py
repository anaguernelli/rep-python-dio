class Animal:
    def __init__(self, qtd_patas):
        self.qtd_patas = qtd_patas

    def __str__(self):
        return f"{self.__class__.__name__}: \
    {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelagem, **kwargs):
        self.cor_pelagem = cor_pelagem
        super().__init__(**kwargs)


class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelagem, qtd_patas):
        print(Ornitorrinco.mro())

        super().__init__(
            cor_pelagem=cor_pelagem,
            cor_bico=cor_bico,
            qtd_patas=qtd_patas
            )


gatinho = Gato(qtd_patas=4, cor_pelagem='laranja')
print(gatinho)

ornitorrinco = Ornitorrinco(
    qtd_patas=4,
    cor_pelagem='Preto',
    cor_bico='vermelho'
    )
print(ornitorrinco)
