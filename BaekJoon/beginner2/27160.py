# 27160

# 3가지 모두 사용 가능.

import sys

hali = {"STRAWBERRY":0, "BANANA":0, "LIME":0, "PLUM":0}
n = int(sys.stdin.readline())
for _ in range(n):
    s, num = sys.stdin.readline().split()
    hali[s] += int(num)

##if (5 in list(hali.values())):
##    print("YES")
##else:
##    print("NO")

##if (5 in hali.values()):
##    print("YES")
##else:
##    print("NO")

print(["NO", "YES"][5 in hali.values()])
