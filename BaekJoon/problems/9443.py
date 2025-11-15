# 9443

# 문제는 최대 26개(A~Z)까지만 가능하다. 복잡하게 풀 필요 없는 문제...

import sys

n = int(sys.stdin.readline())

cap = {}
for k in range(n):
    ipt = sys.stdin.readline().rstrip()
    cap[ipt[0]] = cap.setdefault(ipt[0], 0)
    cap[ipt[0]] += 1

cnt = 0
cidx = 0
for i in range(n):
    if (chr(65+cidx) not in cap.keys()):
        break
    
    if (cap[chr(65+cidx)] > 0):
        cap[chr(65+cidx)] -= 1
        cnt += 1
        cidx = (cidx+1)%26
    elif (cap[chr(65+cidx)] == 0):
        break

print(min(cnt, 26))
