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
    print('Bonjour Alice')


    n = input('Entrez la valeur pour n: ')
    while n == '':
        n = input('Entrez la valeur pour n: ')

    print("Attaque de Pollard En cours !!!")
    resultat = Pollard2.pollard2(n, True)


    p = int(resultat[0])
    q = int(resultat[1])

    e = calculerE(p, q)

    message = input('Entrer le message à chiffrer : ')


    message_tab = message_to_number(message)

    message_code = []
    for i in message_tab:
        """print('depart : ' + i)
        print('crypter ' + str(chiffrement(int(p), int(q), int(i), e)))"""
        message_code.append(chiffrement(int(p), int(q), int(i), e))
    print("Le message codé est : " + str(message_code))
    
    print('*****************************')
    print('*****************************')
    
    message_decoder = []
    for i in message_code:
        message_decoder.append(dechiffrement(int(p), int(q), int(i), e)) 
        
    print("Message déchiffrer :" + str(message_decoder))
    messageDecodeLettre = number_to_message(message_decoder)
    
    print("Lettres du message déchiffré: " + str(messageDecodeLettre))
    message = ''
    for i in messageDecodeLettre:
        message = message + str(i)
    print("Message entier: " + str(message))
    
    
    ''' Afficher le message en un seul message, sans séparation entre les lettres '''
    # print(messageSansTableau(message_code))


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
    
    
    
    
'''MENER L ATTAQUE DE POLLARD 3 '''
    
## chiffrement exemple avec le message M = CO
## Dans la perspective où Matt, un attaque souhaite attaquer avec Pollard
## Il lui suffit de récupérer la clé publique d'alice et son message encodé
## Matt alors obtient C (le message chiffré) et (n,e)
def attaqueDeMAtt(C, n, e):
    ## il faut casser n
    pq = pollard3(n)
    p = pq[0]
    q = pq[1]
    
    d = 3
    phin = ((int(p) - 1) * (int(q) - 1))
    while ((d * e) % phin) != 1:
        d += 1

    print("Une fois d, inverse de e dans Z/n, alors on a gagné car on a récupéré la clé privée qui nous permet de décrypter ou du moins, bruterforce le message encodé.")
    print("La complexté est de n!")
    
