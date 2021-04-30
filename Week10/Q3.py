import sys
import random

def CheckPrime(n):
    flag = True
    for i in range(2, n//2):
        if n%i == 0:
            flag = False
            break
    return flag

def GenRandint(seed):


if __name__=='__main__':
    if len(sys.argv)>1:
        seed = sys.argv[1]
    ri = random.randint(1, 100)
    print(ri)
    while ri != 100:
        print(ri)
    print(ri)