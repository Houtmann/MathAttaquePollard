from .utils import pgcd
import asyncio
def pollard2(n: int):
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
    return print('p = ' + str(p) + ', q = ' + str(int(n/p)) + " nombre itération " + str(compteur))


    f = lambda x: x * x + b
    x0 = 3
    b = 1
    tab = []
    tab.append(x0)
    for i in range(1, n):

        print(i)
        tab.append(f(tab[i-1 % n]))

    return tab

