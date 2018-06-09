from utils import pgcd

def pollard2(n):
    """Factorisation d'un nombre entier décomposable (méth. de pollard)"""
    f = lambda z: z * z + 1
    x = 2
    y = 2
    p = 1
    compteur = 0
    while p == 1 or p == n:
        compteur = compteur + 1
        x = f(x) % n
        y = f(f(y)) % n
        p = pgcd(x - y, n)
    return print('Pour n = ' + str(n) + ' p = ' + str(p) + ', q = ' + str(int(n/p)) + " nombre itération " + str(compteur))




