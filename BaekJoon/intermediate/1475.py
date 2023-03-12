# 1475

import sys
import math

n = sys.stdin.readline().rstrip()
nlist = [n.count(str(x)) for x in range(10)]
setnum = max(max(nlist[:6]), max(nlist[7:9]), math.ceil((nlist[6]+nlist[9])/2))
print(setnum)
