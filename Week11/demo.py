import numpy as np
import random

a = np.array([1, 2, 3, 4])
# print(a)
b = np.array([(2.5, 1, 3, 4.5), (5, 6, 7, 8)], dtype=float)
# print(b)
c = np.array([[(2.5, 1, 3, 4.5), (5, 6, 7, 8)], [
        (2.5, 1, 3, 4.5), (5, 6, 7, 8)]], dtype=float)
# print(c)
for i in c:
    i[1] = np.array([0, 0, 0, 0], dtype=int)

# print(c)
            
np.zeros((2, 3)) # 建立一個2x3全為0的陣列

np.arange(1, 10, 2) # 建立一個由1開始，不超過10，間隔值為2的均數值陣列
# print(np.arange(1, 10, 2))
np.linspace(0, 10, 5) # 建立一個0到10之間，均勻的5個數值陣列
# print(np.linspace(0, 10, 5))
np.full((3, 2), 8) # 建立一個3x2全為8的陣列

y = np.random.randint(2, 135, (2, 3))
# print(y)

z = y.reshape(1, 6)
# print(z)

z[0].sort()
# print(z)

r = np.random.shuffle(z[0])
# print(r)

x = np.ones((2, 3, 4)) * 128 # 建立一個2x3x4全為1的陣列；星號後面可設定為each cell的值
# print(x)


fileName = 'out2.npy'
# with open(fileName, 'wb') as fp:
#     np.save(fp, z)

with open(fileName, 'rb') as fp:
    x2 = np.load(fp)
    print(x2)