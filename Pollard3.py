
from utils import *
import sys
from math import gcd



def pollard3(n):
    """Variable pour compter le nombre d'irération"""
    iteration = 1
    
    """On vérifie si 2 n'est pas le diviseur, tout simplement"""
    if ((n % 2) == 0):
        return print ('p = ' + str(2) + ', q = ' + str(int(n/2)) + " nombre itération " + str(iteration))
    
    """On construit Pollard 3"""
    a = 2 # équivalent à a1
    diviseurTrouve = True
    while(diviseurTrouve):
        # si un des facteurs ne divise pas n, on traite et on continue
        iteration += 1
        nombre = (a-1)
        a = pow(a, iteration, n)
        #print(str(a) + '^' + str(tour) + ' = ' + str(a) + ' modulo (' , str(n) , ') => diviseur de : ' + str(a-1) + ':' + str(1) ) 
        """Si le pcdg est différent de 1, on a trouvé un diviseur de n"""
        if(pgcd( nombre, n) != 1):
            q = pgcd(nombre, n)
            diviseurTrouve = False
            #print("Trouvé ! p : " + str(pgcdResult)  + " et q=n/p: " + str(int(n/pgcdResult))) 
            # si un des facteurs divise n, on fait 
            print('Pour n = ' + str(n) + ' p = ' + str(int(n/q)) + ', q = ' + str(q) + " nombre itération " + str(iteration))
            return [n/q, q]
        
        """On s'assure une sécurité pour éviter une boucle infinie"""
        if(iteration == 50000): diviseurTrouve = False
