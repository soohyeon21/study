# 17288

import sys

s = sys.stdin.readline().rstrip()+"0"

cnt = 0
consec = s[0]
for i in range(1, len(s)):
    if (int(consec[-1])+1 == int(s[i])):
        consec += s[i]
    else:
        if (len(consec) == 3):
            cnt += 1
        consec = s[i]
print(cnt)
