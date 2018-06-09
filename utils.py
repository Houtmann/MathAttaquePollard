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
    nBlock = int(len(str(n)) - 1)


    message_lower = message.lower()
    number =''
    message_tableau = []
    for i in message_lower:

        number = number + str(alphabet[i])

    j = 0

    while number != 0:

        message_tableau[j] = int(number[int(len(number) - nBlock) : len(number)])
        number = int(number[0: int(len(number) - nBlock) ])
        print(message_tableau[j])
        j += 1

    return message_tableau


message_to_number(5141, 'JEVOUSAIME')