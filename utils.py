import numpy as np

def pgcd1(a, b):
    a, b = np.broadcast_arrays(a, b)
    a = a.copy()
    b = b.copy()
    pos = np.nonzero(b)[0]
    while len(pos) > 0:
        b2 = b[pos]
        a[pos], b[pos] = b2, a[pos] % b2
        pos = pos[b[pos]!=0]
    return a


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
