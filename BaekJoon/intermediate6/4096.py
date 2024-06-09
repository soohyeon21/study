# 4096

# str.zfill()

import sys

while (1):
    num = sys.stdin.readline().rstrip()
    if (num == "0"):
        break

    length = len(num)
    cnt = 0
    while (num != num[::-1]):
        num = str(int(num)+1).zfill(length)
        cnt += 1
        
    print(cnt)
