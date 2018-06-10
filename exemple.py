import cProfile

import io
import pstats

import time

import Pollard1, Pollard2, Pollard3

liste_n = [96559,
           462169,
           1435807,
           2013317,
           5436703,
           6156947,
           11340779,
           19752937,
           48013951,
           68444699,
           156179249,
           240530009,
           262596109,
           554576801,
           1072871623,
           1755132007,
           2282496751,
           5060119333,
           10312361471,
           17345701081,
           26411047963,
           37776040793,
           56906053601,
           77428222601,
           136185562199,
           250704237127,
           372533093399,
           513969374969,
           768996512227,
           1106667244799,
           3722106688213,
           18548846503087,
           61767637279697,
           245876657798467,
           860192150137,
           1608553223191,
           6185043754861,
           15395036271149,
           36522670131797,
           90523886246203,
           766832690157389,
           894325585533869,
            1202800005867329,

           ]

start = time.time()
for n in liste_n:
    """pr = cProfile.Profile()
    pr.enable()
    print(Pollard2.pollard2(int(n)))
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s)
    ps.print_stats()
    print(s.getvalue())"""

    Pollard2.pollard2(int(n), True)


end = time.time()
print("Temps mesuré : " + str(end - start))
print("----- Fin de l'exemple -----")
