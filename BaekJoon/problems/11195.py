# 11195

# for i in range(len(s)-1): for j in range(i+1, len(s)+1): s[i:j]는 메모리 초과 발생

import sys

s = sys.stdin.readline().rstrip()

odd_cnt = 0
for i in range(97, 123):
    if (s.count(chr(i))%2 != 0):
        odd_cnt += 1

if (odd_cnt in [0, 1]):
    print(0)
else:
    print(odd_cnt-1)
