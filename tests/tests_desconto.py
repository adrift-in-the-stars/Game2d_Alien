import pytest
from src.desconto import Normal, Vip, Premium

def test_normal():
    desconto = Normal()
    resultado = desconto.calcular(100)
    assert resultado == 10, f"Esperado 10, mas resultado: {resultado}"

@pytest.fixture
def desconto_vip():
    return Vip()

def test_vip_100(desconto_vip):
    assert desconto_vip.calcular(100) == 20

def test_vip_200(desconto_vip):
    assert desconto_vip.calcular(200) == 40

@pytest.mark.parametrize("valor, esperado",[
    {100, 30},
    {200, 60},
    {300, 90}
])

def test_premium(valor, esperado):
    desconto = Premium()
    resultado = desconto.calcular(valor)

    assert resultado == esperado