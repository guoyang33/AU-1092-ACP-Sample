import sys

if __name__=='__main__':
    if len(sys.argv)>1:
        text = sys.argv[1]
        wordDict = {}
        text.replace('.', '')
        text.replace(',', '')
        text.replace('\t', '')
        text.replace('\n', '')
        for word in text.split():
            if word not in wordDict:
                wordDict[word] = 0
            wordDict[word] = wordDict[word] + 1

        for i in wordDict:
            print('{0}  =>  {1}'.format(i, wordDict[i]))
