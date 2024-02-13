# 11121

# 물론 문제에서 input과 output이 bit로 표현된다고는 했지만, 어째서 int로 인식하게 하면 틀리는 거지?
# 틀리는 경우는 어떤 case일 때일까?

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    ipt, opt = sys.stdin.readline().split()
    if (ipt == opt):
        print("OK")
    else:
        print("ERROR")
