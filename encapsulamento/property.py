'''
No property() pode criar atributos gerenciados em suas classes.
São atributos gerenciados, chamados propriedades, quando precisar modificar
sua implementação interna sem alterar a API pública da classe.
'''


class Foo:
    def __init__(self,  x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0


# property
foo = Foo(20)
print(foo.x)

# x.setter
foo.x = 33
print(foo.x)

# x.deleter
del foo.x
print(foo.x)
