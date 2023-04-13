# 4740

# line의 끝에 공백이 포함되어 있을 수 있다.

# rstrip()의 parameter로 제거를 원하는 문자를 넣을 수 있다.

import sys

while (1):
    line = sys.stdin.readline().replace("\n", "")
    if (line == "***"):
        break

    print(line[::-1])
