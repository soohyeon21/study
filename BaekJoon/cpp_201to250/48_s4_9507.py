# 9507

# 미리 67개 길이의 list를 만들어 놓고 하는 방법도 있다.
# 방법은 같고 사용 재료만 다른 느낌이지만...

import sys

def koong(n):
    if (n < 2):
        return 1
    elif (n == 2):
        return 2
    elif (n == 3):
        return 4
    elif (n in dic):
        return dic[n]

    rst = koong(n-1) + koong(n-2) + koong(n-3) + koong(n-4)
    dic[n] = rst
    return rst

t = int(sys.stdin.readline())
dic = {}
for _ in range(t):
    n = int(sys.stdin.readline())
    print(koong(n))
