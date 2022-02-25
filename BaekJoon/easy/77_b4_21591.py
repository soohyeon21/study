# 21591

# 문제를 제대로 읽자

import sys

wc, hc, ws, hs = map(int, sys.stdin.readline().split())

wc -= 2
hc -= 2

if ((wc >= ws) and (hc >= hs)):
    print(1)
else:
    print(0)



#
# 얜 왜 틀린거지?
# wcnt, hcnt는 0&양의 정수만 가능한거 아닌가? 예외가 되는 case가 뭘까...
#
##import sys
##
##wc, hc, ws, hs = map(int, sys.stdin.readline().split())
##
##wc -= 2
##hc -= 2
##wcnt = wc // ws
##hcnt = hc // hs
##
##if (wcnt*hcnt != 0): # 가로세로에 한 개 이상씩 들어갈 수 있다면
##    print(1)
##else:
##    print(0)
