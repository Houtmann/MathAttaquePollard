import cProfile
import io
import pstats
import time

import Pollard1, Pollard2, Pollard3

liste_n = [
            245876657798467,
            1202800005867329,

           ]

start = time.time()
for n in liste_n:
    print("Benchmark de Pollard1 :")
    pr = cProfile.Profile()
    pr.enable()
    print(Pollard1.pollard1(int(n)))
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s)
    ps.print_stats()
    print(s.getvalue())

    print("Benchmark de Pollard2 :")
    pr = cProfile.Profile()
    pr.enable()
    print(Pollard2.pollard2(int(n), True))
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s)
    ps.print_stats()
    print(s.getvalue())

    print("Benchmark de Pollard3 :")
    pr = cProfile.Profile()
    pr.enable()
    print(Pollard3.pollard3(int(n)))
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s)
    ps.print_stats()
    print(s.getvalue())




end = time.time()
print("Temps mesuré : " + str(end - start))
print("----- Fin de l'exemple -----")
