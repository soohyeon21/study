# 10823

# try-except(EOFError)를 사용해도 된다.

import sys

s = ""
while (True):
    new_s = sys.stdin.readline().rstrip()
    if (new_s == ''):
        break
    s += new_s

num = list(map(int, s.split(",")))
print(sum(num))
