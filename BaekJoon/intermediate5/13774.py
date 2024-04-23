# 13774

# default text로 "not possible" 설정하기

import sys

while (1):
    line = sys.stdin.readline().rstrip()
    if (line == "#"):
        break

    text = "not possible"
    for i in range(len(line)):
        forward = line[:i]+line[i+1:]
        if (forward == forward[::-1]):
            text = forward
            break

    print(text)
