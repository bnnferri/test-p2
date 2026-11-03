def classificar_nota(nota):
    if nota > 0 and nota <= 10:
        if nota >= 7:
            return "Aprovado"
        elif nota >= 5  <= 6.9:
            return "Recuperação"
        elif nota < 5:
            return "Reprovado"
    else:
        return "Nota inválida"

def analisar_numero(numero):
    classificação = ""
    if numero > 0:
        classificação += "Positivo,"
    elif numero < 0:
        classificação += "Negativo,"
    else:
        classificação += "Zero e Par"
        return classificação
    if numero % 2 == 0:
        classificação += " Par"
        return classificação
    else:
        classificação += " Ímpar" 
        return classificação            
    