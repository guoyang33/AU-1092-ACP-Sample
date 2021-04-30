import sys

if __name__=='__main__':
    if len(sys.argv)>1:
        keyDict = {
            'q':'w', 'w':'e', 'e':'r', 'r':'t', 't':'y', 'y':'u', 'u':'i', 'i':'o', 'o':'p'
        }
        for key in sys.argv[1]:
            print('{0}'.format(keyDict[key]), end='')
        print()
