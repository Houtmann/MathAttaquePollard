
import Pollard2
import Pollard3
import Pollard1
from utils import message_to_number
from chiffrement import chiffrement, construction_cle, dechiffrement, calculerE
import cProfile, pstats, io

if __name__ == '__main__':
    print('*****************************')
    print('*****************************')
    print('*****************************')
    print('Bonjour Alice')
    answer = input('Voulez vous rentrez p et q et construire votre n à votre guise ? O/n')
    n = 0
    if answer.lower() == 'o':
        p = input('Entrez la valeur pour p: ')
        while p == '':
            p = input('Entrez la valeur pour p: ')

        q = input('Entrez la valeur pour q: ')
        while q == '':
            q = input('Entrez la valeur pour q: ')
        n = construction_cle(int(p), int(q))

    else:
        n = construction_cle(p=None, q=None)


    message = input('Entrer le message à chiffrer : ')

    print(message_to_number(n, message))

    message_code = chiffrement(int(p), int(q), message_to_number(n, message))
    print("Le message codé est : " + str(message_code))
    print('*****************************')
    print('*****************************')
    print('Message déchiffrer :')
    e = calculerE(p, q)
    print(dechiffrement(5, 7, message_code))



    """pr = cProfile.Profile()
    pr.enable()
    p = Pollard3.pollard3(int(n))

    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s)
    ps.print_stats()

    pr = cProfile.Profile()
    pr.enable()
    print(Pollard2.pollard2(int(n)))
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s)
    ps.print_stats()
    print(s.getvalue())"""
