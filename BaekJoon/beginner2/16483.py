#  16483

# round()는 반올림 할 자리의 수가 5이면 반올림 할 때 앞자리의 숫자가 짝수면 내림, 홀수면 올림 한다.
# round(4.5) >>> 4
# round(3.5) >>> 4

import sys

t = int(sys.stdin.readline())
rst = t**2/4
print(round(rst))
