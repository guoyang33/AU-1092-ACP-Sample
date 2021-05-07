import sys
import random

if __name__=='__main__':
    if len(sys.argv) == 3:
        seed = int(sys.argv[1])
        cipher = sys.argv[2]
        print('使用亂數種子碼{0}對\"{1}\"進行解密...'.format(seed, cipher))

        random.seed(seed)
        cipherList = list(cipher)
        numList = list(range(len(cipher)))
        random.shuffle(numList)
        decodedList = [None] * len(numList)
        for i in range(len(cipher)):
            decodedList[numList[i]] = cipherList[i]
        msg = ''.join(decodedList)
        print('解密訊息: \"{0}\"'.format(msg))
    else:
        print('參數錯誤，輸入參數格式 [seed: 金鑰] [cipher: 加密訊息]')