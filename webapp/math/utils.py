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
    
def factors(a: int):
    """

    :param a: Entier
    :return: Liste Entier des facteurs
    """
    factorsListe = []
    for i in range(1, a):
        if (a%i==0):
            factorsListe.append(i)
    return factorsListe
            
def isPrime(n: int):
    """

    :param n: Entier
    :return: True si est un nombre premier, False si non.
    """
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def onlyPrime(ListFactors):
    """

    :param ListFactors Liste Entier
    :return: Liste des entiers premiers 
    """
    primeFactors = []
    for i in ListFactors:
        if isPrime(i):
            primeFactors.append(i)
    return primeFactors

def stripeone(ListePrimeFactors):
    for i in ListePrimeFactors:
        if i == 1:
            ListePrimeFactors.remove(i)
            return ListePrimeFactors;
    return ListePrimeFactors



def powTwo(x):
    powers = []
    i = 1
    while i <= x:
        if i & x:
            powers.append(i)
        i <<= 1
    return powers

## Optimized method to calcul pow of a number
def modPowMethod(a, power, n):
    startPow = 2
    ephemaryPow = power - startPow
    
    result = (pow(a, startPow, n))
    
    if(power <= 2): return (pow(a, power,n))
    if(power > 2):
        while(ephemaryPow >= 1):
            #print(str((result*a)%n) + ' représente : ' + str(a) + '^' + str(power+1-ephemaryPow))
            result = ((result*a)%n)
            ephemaryPow -= 1 ## decrasing pow
    return result
    