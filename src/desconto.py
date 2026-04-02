from abc import ABC, abstractmethod

class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass

class Normal(Desconto):

    def calcular(self, valor)->float:
        return valor * 0.1
    
class Vip(Desconto):

    def calcular(self, valor)->float:
        return valor * 0.2

class Premium(Desconto):

    def calcular(self, valor)->float:
        return valor * 0.3
    

def aplicar_desconto(desconto: Desconto, valor: float)->float:
    return desconto.calcular(valor)


class Pedido:
    def __init__(self, desconto: Desconto):
        self.desconto = desconto

    def total(self, valor):
        return valor - self.desconto.calcular(valor)

if __name__ == "__main__":
    valor = 100

    pedido_normal = Pedido(Normal())
    print(pedido_normal.total(valor))

    pedido_vip = Pedido(Vip())
    print(pedido_vip.total(valor))

    pedido_premium = Pedido(Premium())
    print(pedido_premium.total(valor))