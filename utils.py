from alphabet import alphabet
import math

def est_premier(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


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


