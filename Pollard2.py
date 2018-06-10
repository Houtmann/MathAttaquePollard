from utils import pgcd

def pollard2(n, retour):
    """Factorisation d'un nombre entier décomposable (méth. de pollard)"""
    f = lambda z: z * z + 1
    x = 2
    y = 2
    p = 1
    compteur = 0
    while p == 1 or p == n:
        compteur = compteur + 1
        x = f(x) % int(n)
        y = f(f(y)) % int(n)
        p = pgcd(x - y, n)
    if retour == False:
        return print('Pour n = ' + str(n) + ' p = ' + str(p) + ', q = ' + str(int(int(n)/int(p))) + " nombre itération " + str(compteur))
    else:
        return (int(p), int(n)/int(p))




