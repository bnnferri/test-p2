
def verificar_assento(numero_assento):
    if numero_assento == 10 or numero_assento == 15 or numero_assento == 20:
        return False
    else:
        return True


def reservar_assento(numero_assento):
   return f"Assento {numero_assento} reservado"


def confirmar_reserva(numero_assento):
    verifica = verificar_assento(numero_assento)

    if verifica == True:
        return reservar_assento(numero_assento)
    else:
        return "Assento indisponível"

