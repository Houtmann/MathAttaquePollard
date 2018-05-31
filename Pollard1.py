from utils import pgcd
from math import sqrt


def pollard1(n):

    """On construit la fonction Pollard 1 f(x)=x^2 + b"""
    f = lambda x: x * x + b
    x0 = 3
    b = 1
    """On construit le tableau de Pollard en prenant comme valeur initiale x0"""
    tableaupollard1 = []
    tableaupollard1.append(x0)

    """Variable pour compter le nombre d'itération """
    iteration = 0

    """Algo de pollard1"""
    for i in range(1, int(sqrt(n))):
        tableaupollard1.append(f(tableaupollard1[i-1]) % n)

    for i in range(0, len(tableaupollard1)-1):
            for j in range(i+1, len(tableaupollard1)):
                p = pgcd(tableaupollard1[i] - tableaupollard1[j], n)
                iteration += 1
                if p != 1 and p != n:
                    q = n / p
                    print(p)
                    print(q)
                    print(iteration)
                    return p



