# 24568

# 28명의 학생들이 나눠먹고 남은 갯수가 아니라, 28명이 하나씩 먹고 남은 갯수.
# 문제를 잘 읽자.

import sys

r = int(sys.stdin.readline())
s = int(sys.stdin.readline())

cups = r*8 + s*3
print(cups - 28)
