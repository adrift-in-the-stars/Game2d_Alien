from src.desconto import Pedido
import pytest

def test_pedido_com_mock_desconto(mocker):
    mock_desconto = mocker.Mock()
    mock_desconto.calcular.return_value = 10

    pedido = Pedido(mock_desconto)
    resultado = pedido.total(100)

    assert resultado == 90

    mock_desconto.calcular