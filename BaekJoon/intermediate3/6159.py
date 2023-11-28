# 6159

#
# sol1) Python3 시간초과, PyPy3 정답(110532KB, 1420ms)
#
##import sys
##
##n, s = map(int, sys.stdin.readline().split())
##cows = [int(sys.stdin.readline()) for _ in range(n)]
##
##cnt = 0
##for i in range(n):
##    for j in range(i+1, n):
##        if (cows[i]+cows[j] <= s):
##            cnt += 1
##
##print(cnt)



#
# sol2) Python3 시간초과, PyPy3 정답(110816KB, 792ms)
#
##import sys
##
##n, s = map(int, sys.stdin.readline().split())
##cows = sorted([int(sys.stdin.readline()) for _ in range(n)])
##
##cnt = 0
##for i in range(n):
##    for j in range(i+1, n):
##        if (cows[i]+cows[j] > s):
##            continue
##        cnt += 1
##
##print(cnt)



#
# sol3) left, right pivot 사용. Python3 정답(31120KB, 56ms)
# 신기하구려!
#
import sys

n, s = map(int, sys.stdin.readline().split())
cows = sorted([int(sys.stdin.readline()) for _ in range(n)])

cnt = 0
left, right = 0, n-1
while (left < right):
    if (cows[left] + cows[right] > s):
        right -= 1
    else:
        cnt += right - left
        left += 1

print(cnt)
