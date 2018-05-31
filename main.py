from Pollard1 import pollard1
from Pollard2 import pollard2
from Pollard3 import pollard3
import cProfile


if __name__ == '__main__':
  n=12
  pollard1(n)
  pollard2(n)
  pollard3(n)

    #cProfile.run("pollard1(100)")
