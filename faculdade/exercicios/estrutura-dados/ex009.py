from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod

    def area(self):
        pass


class quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


class circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio ** 2

class retangulo(Forma):
    def __init__(self, lado, altura):
        self.lado = lado
        self.altura = altura

    def area(self):
        return self.lado * self.altura

q = quadrado(4)
c = circulo(3)
r = retangulo(4, 5)

print(q.area())
print(c.area())
print(r.area())