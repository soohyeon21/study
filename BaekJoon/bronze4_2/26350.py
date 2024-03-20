# 26350

# def로 만들면 isLeastTwice가 False가 되자마자 return하고 끝낼 수 있다.

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    denomin = list(map(int, sys.stdin.readline().split()))
    print(f"Denominations:", *denomin[1:])

    isLeastTwice = True
    for i in range(2, denomin[0]+1):
        if (denomin[i] < denomin[i-1]*2):
            isLeastTwice = False

    if (isLeastTwice):
        print("Good coin denominations!")
    else:
        print("Bad coin denominations!")
    print()
