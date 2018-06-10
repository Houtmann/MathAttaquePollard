from alphabet import alphabet
import math

def pgcd(a: int, b: int):
    """

    :param a: Entier
    :param b: Entier
    :return: pgcd(b Entier, r, Entier
    """
    if b == 0:
        return a
    else:
        r = a % b
        return pgcd(b, r)


def message_to_number(n, message):
    number = []
    message_lower = message.lower()

    for i in message_lower:
        number.append(str(alphabet[i]))

    return number


def est_premier(n: int):	
    """	
	
    :param n: Entier	
    :return: True si est un nombre premier, False si non.	
    """	
    for i in range(3, n):	
        if n % i == 0:	
            return False	
    return True