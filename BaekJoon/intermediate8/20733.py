# 20733

# 아니면 그냥 세 덩이 중에 동일한 놈을 출력해줘도 된다.

import sys

t = sys.stdin.readline().rstrip()

single = len(t)//3
rst = ""
for th in range(single):
    elem = []
    for i in range(3):
        elem.append(t[i*single+th])

    for e in elem:
        if (elem.count(e) > 1):
            rst += e
            break

print(rst)
