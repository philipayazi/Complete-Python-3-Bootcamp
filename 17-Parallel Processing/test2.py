from random import random
from multiprocessing import Pool
import timeit
import sys

N = int(sys.argv[1])  # these arguments are passed in from the command line
P = int(sys.argv[2])

def find_pi(n):
    """
    Function to estimate the value of Pi
    """
    inside=0

    for _ in range(n):
        x=random()
        y=random()
        if (x*x+y*y)**(0.5)<=1:  # if i falls inside the circle
            inside+=1

    return 4*inside/n

if __name__ == '__main__':
    
    with Pool(P) as p:
        print(timeit.timeit(lambda: print(f'{sum(p.map(find_pi, [N//P]*P))/P:0.5f}'), number=10))
    print(f'{N} total iterations with {P} processes')