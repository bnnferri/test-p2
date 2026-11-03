import pytest
from unittest.mock import Mock, patch
from EX6 import verificar_assento, reservar_assento, confirmar_reserva 
from EX2 import analisar_texto
import EX6

# 1. Frase com 5 palavras
def test_frase_com_5_palavras():
    frase = "O rato roeu a roupa"
    resultado = analisar_texto(frase)
    assert resultado == 5

# 2. Frase com apenas uma palavra
def test_frase_com_uma_palavra():
    frase = "Excepcional"
    resultado = analisar_texto(frase)
    assert resultado == 1

# 3. Frase vazia
def test_frase_vazia():
    frase = ""
    resultado = analisar_texto(frase)
    assert resultado == 0

# 4. Frase com espaços no início e no final
def test_frase_com_espacos_inicio_fim():
    frase = "   Teste de espaços nas bordas   "
    resultado = analisar_texto(frase)
    assert resultado == 5

# 5. Frase com vários espaços entre palavras
def test_frase_com_varios_espacos():
    frase = "Python    é      uma   linguagem"
    resultado = analisar_texto(frase)
    assert resultado == 4

def test_reserva_sucesso():
    with patch("EX6.verificar_assento") as mock_verificar_assento:
        mock_verificar_assento.return_value = True

        numero_assento = 12
        resultado = EX6.confirmar_reserva(numero_assento)

        assert resultado == f"Assento {numero_assento} reservado"
        mock_verificar_assento.assert_called_once_with(12)


def test_assento_indisponivel():
    with patch("EX6.verificar_assento") as mock_verificar_assento:
        mock_verificar_assento.return_value = False

        numero_assento = 10
        resultado = EX6.confirmar_reserva(numero_assento)

        assert resultado == "Assento indisponível"
        mock_verificar_assento.assert_called_once_with(10)


def test_verifica_verificar_assento():
    numero_assento = 10
    resultado = EX6.verificar_assento(numero_assento)

    assert resultado == False

from EX01 import classificar_nota, analisar_numero
import unittest

def test_classificar_aluno_aprovado():
    result = classificar_nota(8)
    assert result == "Aprovado"

def test_classificar_aluno_recuperacao():
    result = classificar_nota(5.5)
    assert result == "Recuperação"

def test_classificar_aluno_reprovado():
    result = classificar_nota(4.8)
    assert result == "Reprovado"

def test_classificar_aluno_nota_invalida():
    result = classificar_nota(-1)
    assert result == "Nota inválida"    

def test_analisar_numero_zero():
    result = analisar_numero(0)   
    assert result == "Zero e Par"  

def test_analisar_numero_negativo_impar():
    result = analisar_numero(-3)   
    assert result == "Negativo, Ímpar"

def test_analisar_numero_negativo_par():
    result = analisar_numero(-2)   
    assert result == "Negativo, Par"

def test_analisar_numero_positivo_impar():
    result = analisar_numero(3)   
    assert result == "Positivo, Ímpar"

def test_analisar_numero_positivo_par():
    result = analisar_numero(2)   
    assert result == "Positivo, Par"     