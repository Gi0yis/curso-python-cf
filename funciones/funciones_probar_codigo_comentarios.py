# docstring
# Probar en consola --> python3 -m doctest funciones_probar_codigo_comentarios.py
def palindromo(sentece):
    """
    Permite conocer si un string es, o no, un palindromo.

    Args:
        - sentence (string)
    
    Return:
        - Bool
    
    Examples:
    >>> palindromo('oso')
    True

    >>> palindromo('Anita lava la tina')
    True

    >>> palindromo('CodigoFacilito')
    False
    """
    sentece = sentece.lower().replace(' ', '')
    return sentece == sentece[::-1]

"""print(palindromo('oso'))
print(palindromo('Anita lava la tina'))
print(palindromo('CodigoFacilito'))"""


def average(*args):
    """
    Permite conocer el promedio de N argumentos.

    Example:
    >>> average(5, 5, 5, 5, 5)
    5.0

    >>> average(10, 9, 8, 7)
    8.5
    """
    return sum(args) / len(args)

