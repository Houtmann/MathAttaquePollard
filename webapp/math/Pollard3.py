
from utils import *
import sys

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
        nombre = ((a**(tour))-1)
        result = diviseurPremier(nombre)
        powResult = modPowMethod(a, tour, n)
        print(str(a) + '^' + str(tour) + ' = ' + str(powResult) + ' modulo (' , str(n) , ') => diviseur de : ' + str(powResult-1) + ':' + str(result) )
        a = a ** tour
        for i in result:
            if(pgcd(i, n) != 1):
                print("Trouvé ! p : " + str(i) + " et q=n/p: " + str(int(n/i)))
                # si un des facteurs divise n, on fait
                continuer = False
                
        if(tour == 10): continuer = False
        
pollard3(n)
