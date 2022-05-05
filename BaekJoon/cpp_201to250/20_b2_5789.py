# 5789

# 문제를 꼼꼼히, 잘, 읽자.

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    num = sys.stdin.readline().rstrip()
    if (num[len(num)//2] == num[len(num)//2-1]):
        print("Do-it")
    else:
        print("Do-it-Not")
