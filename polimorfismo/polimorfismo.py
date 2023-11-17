class Passaro:
    def voar(self):
        print('voando')


class Pardal(Passaro):
    def voar(self):
        super().voar()


class Picapau(Passaro):
    def voar(self):
        print('Não quero voar!')


# !!! Aqui está um exemplo ruim do polimorfismo,
# pois usa a herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print('Avião está decolando')


def plano_voo(param):
    param.voar()


passaro1 = Pardal()
passaro2 = Picapau()

plano_voo(passaro1)
plano_voo(passaro2)
