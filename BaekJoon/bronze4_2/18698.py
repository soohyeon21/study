# 18698

# .split('D') 해서 len()하는 방법도 있다.

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    ipt = sys.stdin.readline().rstrip()
    didx = ipt.find('D')
    if ("D" not in ipt):
        didx = len(ipt)
    print(didx)
