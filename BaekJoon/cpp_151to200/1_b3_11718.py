# 11718

# google에 있는 예시답안과 나 사이 시간동안 조건(no 공백)이 추가되었나 보다.

# 입력의 수가 주어지지 않은 경우: use try-except

import sys

while (True):
    try:
        inp = sys.stdin.readline().rstrip()
        if (inp == ""):
            break
        print(inp)
    except:
        break
