# 2010

# list 말고 sum=0으로 놓고 매 for문마다 += 해주는 게 메모리는 덜 잡아먹는 듯.

# n이 얼마인가에 따라서 최종적으로 빼줘야 하는 수가 달라진다.
# 예제가 많이 주어지지 않은 경우에는 다양한 경우의 test case를 해보자.

# 해당 경우는 sys.stdin.readline()을 써야 시간 초과가 되지 않는다.
# input()은 시간 초과 발생한다.
# 앞으로는 그냥 default로 sys.stdin.readline()을 쓰는게 차라리 좋은 걸까?

import sys

n = int(sys.stdin.readline())

summ = []
for _ in range(n):
    summ.append(int(sys.stdin.readline()))
print(sum(summ) - (n-1))
