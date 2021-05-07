import sys
import random

if __name__=='__main__':
    if len(sys.argv) == 3:
        seed = int(sys.argv[1])
        msg = sys.argv[2]
        print('使用亂數種子碼{0}對\"{1}\"進行加密...'.format(seed, msg))
        
        random.seed(seed)
        msgList = list(msg)
        numList = list(range(len(msg)))
        random.shuffle(numList)
        encodedList = []
        for i in range(len(msg)):
            encodedList.append(msgList[numList[i]])
        cipher = ''.join(encodedList)
        print('加密訊息: \"{0}\"'.format(cipher))
    else:
        print('參數錯誤，輸入參數格式 [seed: 金鑰] [msg: 訊息]')