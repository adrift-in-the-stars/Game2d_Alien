from src.desconto import Desconto

class StubSemDesconto(Desconto):
    def calcular(self, valor):
        return 0