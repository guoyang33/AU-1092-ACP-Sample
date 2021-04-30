import sys

if __name__=='__main__':
    if len(sys.argv) > 1:
        numList = list(map(int, sys.argv[1:]))
        summary = sum(numList)
        avg = summary / len(numList)
        mid = numList[len(numList)//2]
        print('AVG: {0}\nMID: {1}'.format(avg, mid))