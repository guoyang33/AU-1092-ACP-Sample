# 5/7 第十一週 | Week11

## 目錄 | Index

## 說明 | Introduction

以下範例是使用 random 函式庫中的 shuffle() 對文字以打散的形式達到加密的效果

### 加密程式

#### 檔案

* [encode_msg.py](encode_msg.py)

#### 程式碼

~~~~py
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
~~~~

### 解密程式

#### 檔案

* [decode_msg.py](decode_msg.py)

#### 程式碼

~~~~py
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
~~~~

---

Authored by CYouLiao <guoyang33@gmail.com>
