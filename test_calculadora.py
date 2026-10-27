from calculadora import *

def test_soma():
    result = soma(5, 2)
    
    assert result == 7

def test_subtracao():
    result = subtracao(5, 1)

    assert result == 4

def test_divisao():
    result = divisao(10, 2)

    assert result == 5

def test_divisao_por_zero():
    result = divisao(10, 0)

    assert result == "Erro: Divisão por zero não é permitida."


def test_multiplicacao():
    result = multiplicacao(7, 7)

    assert result == 49

def test_potencia():
    result = potencia(2, 3)

    assert result == 8

def test_raiz_quadrada():
    result = raiz_quadrada(16)

    assert result == 4

def test_raiz_quadrada_negativa():
    result = raiz_quadrada(-9)

    assert result == "Erro: Não é possivel calcular a raiz quadrada de um número negativo."

def test_calculadora():
    result = calculadora(1, 5, 3)
    assert result == 8

    result = calculadora(2, 5, 3)
    assert result == 2

    result = calculadora(3, 10, 2)
    assert result == 5

    result = calculadora(4, 3, 4)
    assert result == 12

    result = calculadora(5, 2, 3)
    assert result == 8

    result = calculadora(6, 16, 0)
    assert result == 4

    result = calculadora(3, 10, 0)
    assert result == "Erro: Divisão por zero não é permitida."