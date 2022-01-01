# 4375

# 딱히 입력에 종료조건이 포함되어 있지 않다면 readline-try-except를 사용하자

# sys.stdin.readline()만 try부분에 있고 나머지는 except 밑에 있어도 됨.
# 문자열로 1씩 더하는 것보다, 숫자상태로 한자리씩 더하는게 더 빠르다.

import sys

while (True):
    try:
        num = "1"
        n = int(sys.stdin.readline())
        while (True):
            if (int(num) % n ==0):
                print(len(num))
                break
            else:
                num += "1"
    except:
        break
