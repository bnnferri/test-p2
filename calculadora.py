def calculadora(op, n1, n2):
    match op:
        case 1:
            return soma(n1, n2)
        case 2:
            return subtracao(n1, n2)
        case 3:
            return divisao(n1, n2)
        case 4:
            return multiplicacao(n1, n2)
        case 5:
            return potencia(n1, n2)
        case 6:
            return raiz_quadrada(n1)


def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def divisao(n1, n2):
    if n2 == 0:
        return "Erro: Divisão por zero não é permitida."
    return n1 / n2

def multiplicacao(n1, n2):
    return n1 * n2

def potencia(n1, n2):
    return n1 ** n2

def raiz_quadrada(n1):
    if n1 < 0:
        return "Erro: Não é possivel calcular a raiz quadrada de um número negativo."
    return n1 ** 0.5