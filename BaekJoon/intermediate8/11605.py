# 11605

# eval() # eval('3 + 5') # 8

import sys

def cal(num, op, cnt):
    if (op == "ADD"):
        return num+cnt
    elif (op == "SUBTRACT"):
        return num-cnt
    elif (op == "MULTIPLY"):
        return num*cnt
    elif (op == "DIVIDE"):
        return num/cnt


n = int(sys.stdin.readline())

oper = []
for _ in range(n):
    op, cnt = sys.stdin.readline().split()
    cnt = int(cnt)
    oper.append((op, cnt))

total = 0
for i in range(1, 101):
    rst = i
    state = True
    for op, cnt in oper:
        rst = cal(rst, op, cnt)
        if ((rst != int(rst)) or (rst < 0)):
            state = False

    if (not state):
        total += 1

print(total)
