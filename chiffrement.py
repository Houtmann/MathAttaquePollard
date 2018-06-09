import random
from utils import *

def calculerE(p, q):
    e = 3
    phin = ((int(p)-1)*(int(q)-1))
    while pgcd(e, phin) != 1:
        e += 1
    return e

def chiffrement(p, q, message, e):
    n = p * q
    return pow(int(message), e, n)


def calculerD(p, q, e):
    d = 3
    phin = ((int(p) - 1) * (int(q) - 1))
    while ((d * e) % phin) != 1:
        d += 1

    return d

def inverseModulo(e, phin):
    if(pgcd(e, phin) == 1):
        d = 3
        while ((e*d) % phin != 1):
            d += 1
        return d
    return False


def dechiffrement(p, q, message, e):
    n = p * q

    phin = ((p - 1) * (q - 1))

    d = calculerD(p, q , e)



    return pow(int(message), d, n)

def construction_cle(p, q):
    """

    :param p:
    :param q:
    :return:
    """
    if p and q:
        return p * q
    else:
        nombrePremier = False;
        while nombrePremier != True:
            p = random.randint(1000, 10000000000000)
            q = random.randint(1000, 10000000000000)
            if (est_premier(p) and est_premier(q)):
                nombrePremier = True
                return p * q
