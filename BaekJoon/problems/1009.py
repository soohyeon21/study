# 1009

# 마지막 숫자가 반복되면 stop해서 시간 줄이기
# 10의 배수의 데이터는 10번 컴퓨터가 처리한다.

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())

    ends = []
    end = int(str(a)[-1])
    ends.append(end)
    for i in range(1, b):
        end *= a
        end = int(str(end)[-1])
        if (end not in ends):
            ends.append(end)
        else:
            break

    order = b%len(ends)
    computer = ends[order-1]
    if (computer == 0):
        print(10)
    else:
        print(computer)
