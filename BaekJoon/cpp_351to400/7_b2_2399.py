# 2399

# 첫 시도는 '메모리 초과' 나왔다ㅎ
# 굳이 밑에 방법처럼 줄이지 않고, for문 2번 써서 하는 것도 가능한 듯 하다.

import sys

n = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))
line.sort()

val = 0
c = n-1
for i in range(n//2):
    val += c * abs(line[i] - line[n-(i+1)])
    c -= 2
val *= 2
print(val)
