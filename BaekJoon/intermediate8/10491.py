# 10491

# readline() + try-except EOFError는 출력 초과.

import sys

lines = sys.stdin.readlines()

for line in lines:
    if ("problem" in line.lower()):
        print("yes")
    else:
        print("no")
