numList = list(map(int, input().split()))
for i in range(1, len(numList)):
    for arrow in range(i-1, -1, -1):
        right = arrow + 1
        if numList[arrow] > numList[right]:
            tmp = numList[right]
            numList[right] = numList[arrow]
            numList[arrow] = tmp

print(*numList)
