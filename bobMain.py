import Pollard2
import Pollard3
import Pollard1
from utils import message_to_number
from chiffrement import chiffrement, construction_cle, dechiffrement, calculerE, calculerD, messageSansTableau, number_to_message
import cProfile, pstats, io

if __name__ == '__main__':
    print('*****************************')
    print('*****************************')
    print('*****************************')
    print('Bonjour Bob !')

    p = input('Entrez la valeur pour p: ')
    while p == '':
        p = input('Entrez la valeur pour p: ')

    q = input('Entrez la valeur pour q: ')
    while q == '':
        q = input('Entrez la valeur pour q: ')

    print('La clé RSA de Bob est : (' + str(int(p)*int(q)) +', '+ str(calculerE(p, q)) +')')
