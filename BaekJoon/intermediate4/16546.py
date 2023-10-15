# 16546

# 방법은 다양하다.
# n까지의 합을 구하고 입력 수들을 뺀 결과값을 출력하는 방법도 있고
# set으로 집합을 2개 만들어서 차집합을 한 결과를 출력하는 방법도 있다.

import sys

n = int(sys.stdin.readline())
runner = [0 for x in range(n+1)]
finished = list(map(int, sys.stdin.readline().split()))

runner[0] = 1
for f in finished:
    runner[f] = 1

print(runner.index(0))
