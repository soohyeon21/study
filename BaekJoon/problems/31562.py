# 31562

# try-except 말고 jung.keys()에 없으면 print("!") 했어도 됐다.

import sys

n, m = map(int, sys.stdin.readline().split())

jung = {}
for _ in range(n):
    tlen, title, *scales = sys.stdin.readline().split()
    first3 = ''.join(scales[:3])
    jung[first3] = jung.setdefault(first3, [])
    jung[first3].append(title)

for i in range(m):
    start = sys.stdin.readline().rstrip().replace(' ', '')

    try:
        if (len(jung[start]) == 1):
            print(jung[start][0])
        elif (len(jung[start]) > 1):
            print("?")
    except KeyError:
        print("!")
