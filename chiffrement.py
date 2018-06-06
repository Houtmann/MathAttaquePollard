import random
from utils import *

def calculerE(p, q):
    e = 1
    phin = ((p-1)*(q-1))
    while pgcd(e, phin) != 1:
        e += 1
    return e

def chiffrement(p, q, message):
    return pow(message, calculerE(p,q), p*q)


def inverseModulo(e, phin):
    if(pgcd(e, phin) == 1):
        d = 1
        while ((e*d) % phin != 1):
            d += 1
        return d
    return False


def dechiffrement(p, q, message):
    n = p * q
    e = calculerE(p,q)
    phin = ((p - 1) * (q - 1))
    d = inverseModulo(e, phin)
    print(d)
    messageDecode = (pow(message, d) ** n)

    return messageDecode

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
            n = random.randint(1000, 10000000000000)
            if (est_premier(n)):
                nombrePremier = True
                return n
