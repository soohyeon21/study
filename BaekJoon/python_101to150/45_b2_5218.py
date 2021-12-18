# 5218

# elements를 공백을 두고 출력할때는 문자열 or end=" " 사용가능하다.

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    first, second = sys.stdin.readline().split()

    distance = []
    prnt = "Distances:"
    for i in range(len(first)):
        if (second[i] >= first[i]):
            value = (ord(second[i]) - 64) - (ord(first[i]) - 64)
            distance.append(value)
        else:
            value = (ord(second[i]) - 64) + 26 - (ord(first[i]) - 64)
            distance.append(value)
        prnt += " " + str(distance[i])
    print(prnt)
