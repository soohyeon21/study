# 9094

# 두 정수 n과 m이 주어졌을 때, 0 < a < b < n인 정수 쌍 (a, b) 중에서
# (a2+b2+m)/(ab)가 정수인 쌍의 개수를 구하는 프로그램을 작성하시오.

# 시간 초과
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    cnt = 0
    for a in range(1, n):
        for b in range(a+1, n):
            chk = (a**2 + b**2 + m) / (a*b)
            if (chk == int(chk)):
                cnt += 1
    print(cnt)
