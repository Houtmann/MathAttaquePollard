
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
    answer = input('Voulez allez entrer  p et q et construire votre n à votre guise ?')
    n = 0

    p = input('Entrez la valeur pour p: ')
    while p == '':
        p = input('Entrez la valeur pour p: ')

    q = input('Entrez la valeur pour q: ')
    while q == '':
        q = input('Entrez la valeur pour q: ')
    n = construction_cle(int(p), int(q))

    e = calculerE(p, q)
    message = input('Entrer le message à chiffrer : ')

    message_tab = message_to_number(n, message)

    message_code = []
    for i in message_tab:
        print('depart : ' + i)
        print('crypter ' + str(chiffrement(int(p), int(q), int(i), e)))
        message_code.append(chiffrement(int(p), int(q), int(i), e))

    print("Le message codé est : " + str(message_code))
    print('*****************************')
    print('*****************************')
    print('Message déchiffrer :')


    message_decoder = []
    for i in message_code:
        message_decoder.append(dechiffrement(int(p), int(q), int(i), e))
    print(message_decoder)


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
