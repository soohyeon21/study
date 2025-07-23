# 30458

# 홀수인 경우 가운데 문자 제외하고, 전체에서 홀수개로 존재하는 문자가 있는지 확인하면 된다.

import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

whole = {}

for l in range(n//2):
    whole[s[l]] = whole.setdefault(s[l], 0)
    whole[s[l]] += 1
right_start = n//2+1 if n%2!=0 else n//2
for r in range(right_start, n):
    whole[s[r]] = whole.setdefault(s[r], 0)
    whole[s[r]] += 1

state = True
for one in whole.values():
    if (one%2 != 0):
        state = False
        break

if (state):
    print("Yes")
else:
    print("No")
