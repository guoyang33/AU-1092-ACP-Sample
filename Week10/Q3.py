import sys
import random

def CheckPrime(x):
    for i in range(2, x//2):
        if x%i == 0:
            return False
    return True

def GenRandint():
    num = random.randint(100, 1000)
    while not CheckPrime(num):
        num = random.randint(100, 1000)
    return num

if __name__=='__main__':
    if len(sys.argv)>1:
        random.seed(int(sys.argv[1]))
    for i in range(1, 2+1):
        print('{0} -th Prime Random:\t{1}'.format(i, GenRandint()))