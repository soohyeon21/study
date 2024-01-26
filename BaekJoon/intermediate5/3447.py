# 3447

# 이럴때는 그냥 readline() 대신 input() 사용만 해야하려나.
# readlines() 방법도 있긴 하다.

import sys

while (1):
    try:
        #line = sys.stdin.readline().replace("\n", "")
        line = input()
    except EOFError: # or 그냥 except만
        break

    while ("BUG" in line):
        line = line.replace("BUG", "")

    print(line)
