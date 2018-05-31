
from utils import *
import sys
from math import gcd

## Initializing argument or use default value for n = 299
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 299

def diviseurPremier(n):
    facteurs = factors(n)
    primeFactors = onlyPrime(facteurs)
    primeFactorsNoOne = stripeone(primeFactors)
    return primeFactorsNoOne

def pollard3(n):
    a = 2 # équivalent à a1
    continuer = True
    result=0
    tour = 1
    #print(str(a) + '^' + str(tour) + ' = ' + str( a ** tour ) + ' modulo (' + str(n) + ')')
    while(continuer):
        # si un des facteurs ne divise pas n, on traite et on continue
        tour += 1;
        ##result = diviseurPremier(nombre) 
        nombre = ((a**(tour))-1)
        powResult = modPowMethod(a, tour, n)
        print(str(a) + '^' + str(tour) + ' = ' + str(powResult) + ' modulo (' , str(n) , ') => diviseur de : ' + str(powResult-1) + ':' + str(1) ) 
        a = a ** tour
        if(pgcd( nombre, n) != 1): 
            pgcdResult = pgcd( nombre, n) 
            print("Trouvé ! p : " + str(pgcdResult)  + " et q=n/p: " + str(int(n/pgcdResult))) 
            # si un des facteurs divise n, on fait 
            continuer = False
        if(tour == 10): continuer = False 
