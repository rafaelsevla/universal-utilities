import re

def isCpfValid(cpf):
    """ Se cpf no formato brasileiro for válido, ele retornará True, caso contrário, retornará False """

    # Verifique se o tipo é string
    if not isinstance(cpf,str):
        return False

    # Remova alguns caracteres indesejados :D
    cpf = re.sub("[^0-9]",'',cpf)

    # Verifica se a sequência possui 11 caracteres
    if len(cpf) != 11:
        return False

    sum = 0
    weight = 10

    """ Cálculo do primeiro dígito de verificação cpf. """
    for n in range(9):
        sum = sum + int(cpf[n]) * weight

        # Decrement weight
        weight = weight - 1

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        firstVerifyingDigit = 0
    else:
        firstVerifyingDigit = verifyingDigit

    """ Cálculo do segundo dígito de verificação cpf. """
    sum = 0
    weight = 11
    for n in range(10):
        sum = sum + int(cpf[n]) * weight

        # Decrementar peso
        weight = weight - 1

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        secondVerifyingDigit = 0
    else:
        secondVerifyingDigit = verifyingDigit

    if cpf[-2:] == "%s%s" % (firstVerifyingDigit,secondVerifyingDigit):
        return True
    return False