from unittest.mock import Mock, patch
from EX6 import verificar_assento, reservar_assento, confirmar_reserva 

def test_reserva_sucesso():
    with patch("EX.verificar_assento") as mock_verificar_assento:
        mock_verificar_assento.return_value = True

        numero_assento = 12
        resultado = EX.confirmar_reserva(numero_assento)

        assert resultado == f"Assento {numero_assento} reservado"
        mock_verificar_assento.assert_called_once_with(12)


def test_assento_indisponivel():
    with patch("EX.verificar_assento") as mock_verificar_assento:
        mock_verificar_assento.return_value = False

        numero_assento = 10
        resultado = EX.confirmar_reserva(numero_assento)

        assert resultado == "Assento indisponível"
        mock_verificar_assento.assert_called_once_with(10)


def test_verifica_verificar_assento():
    numero_assento = 10
    resultado = EX.verificar_assento(numero_assento)

    assert resultado == False
