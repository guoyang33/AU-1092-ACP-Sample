import random
import math

# 質數 aaa
def zhishuCheck(n):
    n = int(n)
    flag = True
    for i in range(1, n//2 + 1):
        if n%i==0:
            flag = False
            break
    print('YES' if flag else 'NO')

# 位數計算
def dig(n, cnt=0):
    return dig(n//10, cnt+1) if n > 0 else cnt

# 階乘運算
def getFactorial(n):
    return n * getFactorial(n-1) if n > 2 else n

# m 取 n
def getCombination(m, n):
    return getFactorial(m)/(getFactorial(n)*getFactorial(m-n))

#M3 Q2
# random integer generator
def getRanduntBySeed(seed):
    # sd = int(input())
    # sd = 23323456
    random.seed(seed)
    result = [0] * 6
    for i in range(len(result)):
        x = 0
        while x in result:
            x = random.randint(1, 42)
        result[i] = x
    print(*result, sep='\t')

#M3 Q5
def stp2(n):
    if n>1:
        return n * stp(n-1)
    else:
        return 1

#M3 Q1
def Q1(s):
    # s = input()

    for i in range(len(s)-1, -1, -1):
        print(s[i], end='')
    print()

#M3 Q3
def Q3():
    data = [[]] * 5
    for i in range(len(data)):
        data[i] = list(map(int, input().split()))
    for i in range(len(data[0])):
        for j in range(len(data)):
            print(data[j][i], end='\t')
        print()

#M3 Q4
def F(w, h):
    for i in range(1, h+1):
        for j in range(1, w+1):
            print('{}\t'.format(i*j), end='')
        print()

# M3 Q10
def Q10(n):
    # n = int(input())
    nums = list(map(int, input().split()))
    b = False
    for i in range(len(nums)-1):
        x = nums[i] * nums[i+1]
        if not b:
            b = x
        else:
            if x > b:
                b = x
    print(b)

#M3 Q11
def Q11(n):
    # n = int(input())
    nums = list(map(int, input().split()))
    op, ed = 0, 0 # opening, end
    x = 0
    for i in range(len(nums)-1):
        op = i
        flag = False
        for j in range(i+1, len(nums)):
            ed = j
            x = sum(nums[i:j])
            if x == 0:
                flag = True
                break
        if flag:
            break
    print(*nums[op:ed], sep=' ')

#M3 Q17
def f(n):
    return f(n-1) + f(math.floor(n/2)) if n > 1 else n+1

# print(f(int(input())))

