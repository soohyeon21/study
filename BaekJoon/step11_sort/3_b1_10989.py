# 10989

# 단순 sort()를 쓰면 '메모리 초과'가 발생한다.

# for문 속에서 append를 사용하게 되면 메모리 재할당이 이루어져서 메모리를 효율적으로 사용하지 못한다고 한다.
# 일반적으로 입력값이 크지 않은 경우에는 상관없지만, 입력값이 많이 주어질 때는 주의할 필요가 있단다.

# 주어지는 수는 10,000보다 작거나 같은 자연수이다.

import sys

n = int(sys.stdin.readline())
num = [0] * 10001

for _ in range(n):
    num[int(sys.stdin.readline())] += 1

for i in range(10001):
    if (num[i] != 0):
        for j in range(num[i]):
            print(i)
