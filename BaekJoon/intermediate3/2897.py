# 2897

# 함수 안에서 만들어진 변수를 지역변수, 함수 밖에서 만들어진 변수를 전역변수
# 함수 안에서 전역변수 만들기: 지역변수 앞에 global 써주기

import sys

def findCrash(plot):
    if ("#" in plot): # if ("#" not in plot):으로 줄일 수 있겠다.
        return
    else:
        crash[plot.count("X")] += 1

    return

r, c = map(int, sys.stdin.readline().split())
park = [sys.stdin.readline().rstrip() for _ in range(r)]
crash = [0, 0, 0, 0, 0]

for row in range(r-1):
    for col in range(c-1):
        findCrash(park[row][col]+park[row][col+1]+park[row+1][col]+park[row+1][col+1])

print(*crash, sep="\n")
