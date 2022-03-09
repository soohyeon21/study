# 11719

# #11718과 달리 빈 줄도 입력으로 간주한다.
# 따라서 if-break 조건에 100개의 입력을 초과하는 경우를 추가하였다.
# 단순히 while-try-catch만 하면 출력초과 발생.

import sys

cnt = 0
while (1):
    try:
        inp = sys.stdin.readline().rstrip("\n")
        print(inp)
        cnt += 1
        if (cnt > 100):
            break
    except EOFError:
        break

##for line in sys.stdin:
##    print(line, end='')
