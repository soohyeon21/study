# 2355

# 아, 문제 제대로 읽자. "두 정수 사이에 있는 수의 합을 구하는 프로그램"이다.
# 두 정수는 크기 순서대로 주어지지 않는다. 크고 작음을 추가로 비교해야 한다.
# 마치 등차수열 계산처럼 계산하는 방법도 있는 듯 하다.

import sys

aa, bb = map(int, sys.stdin.readline().split())
a = min(aa, bb)
b = max(aa, bb)
ssum = (b*(b+1))//2 - ((a-1)*a)//2
print(ssum)
