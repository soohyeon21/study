# 2167

# dp. Dynamic Programming. 동적 프로그래밍. 다이나믹 프로그래밍
# 메모이제이션. Memoization

#
# sol
#
import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

# dp 만들기
dp = [[0 for x in range(m+1)] for y in range(n+1)]
for row in range(1, n+1):
    for col in range(1, m+1):
        dp[row][col] = arr[row-1][col-1] + dp[row][col-1] + dp[row-1][col] - dp[row-1][col-1]

k = int(sys.stdin.readline())
for _ in range(k):
    i, j, x, y = map(int, sys.stdin.readline().split())
    total = dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1]
    print(total)


#
# 시간초과
#
##import sys
##
##n, m = map(int, sys.stdin.readline().split())
##arr = []
##for _ in range(n):
##    arr.append(list(map(int, sys.stdin.readline().split())))
##    
##k = int(sys.stdin.readline())
##for _ in range(k):
##    i, j, x, y = map(int, sys.stdin.readline().split())
##    rst = 0
####    for row in range(i-1, x):
####        for col in range(j-1, y):
####            rst += arr[row][col]
##    for row in range(i-1, x):
##        rst += sum(arr[row][j-1:y])
##    print(rst)
