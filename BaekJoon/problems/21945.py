# 21945

# 그냥 (a == a[::-1])만 확인했어도 됐다.

import sys

def isPal(num):
    snum = str(num)
    if (len(snum)%2 == 0):
        if (snum[:len(snum)//2][::-1] == snum[len(snum)//2:]):
            return True
        else:
            return False
    elif (len(snum)%2 != 0):
        if (snum[:len(snum)//2][::-1] == snum[len(snum)//2+1:]):
            return True
        else:
            return False


n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

total = 0
for each in num:
    if (isPal(each)):
        total += each

print(total)
