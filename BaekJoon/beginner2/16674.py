# 16674

# dictionary/boolean/try-except를 사용해서 풀 수도 있다.

import sys

n = sys.stdin.readline().rstrip()
spec = ["0", "1", "2", "8"]
nspec = [str(x) for x in range(3, 8)]+["9"]
state = 1

for number in nspec:
    if (number in n):
        state = 0
        break

if (set(n) == set(spec)):
    state = 2
    cnt0 = n.count("0")
    cnt1 = n.count("1")
    cnt2 = n.count("2")
    cnt8 = n.count("8")
    if ((cnt0 == cnt1) and (cnt1 == cnt2) and (cnt2 == cnt8)):
        state = 8
        
print(state)
