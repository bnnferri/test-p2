def analisar_texto(texto):
    """
    Recebe uma frase e retorna a quantidade de palavras.
    Retorna 0 caso a frase esteja vazia ou contenha apenas espaços.
    """
    if not texto:
        return 0
        
    palavras = texto.split()
    return len(palavras)