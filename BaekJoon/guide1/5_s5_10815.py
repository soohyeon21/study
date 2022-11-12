# 10815

# dictionary는 빠르다.

# 이진 탐색을 사용해서 푸는 방법도 있다.
# 완전 이진 트리인 경우: O(logn)

#
# dictionary 사용 풀이. dictionary는 빠르다!!!
#
import sys

n = int(sys.stdin.readline())
sang = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
chk = list(map(int, sys.stdin.readline().split()))

dic = {}
for i in range(n):
    dic[sang[i]] = 1

for j in range(m):
    if (chk[j] not in dic):
        print(0, end=" ")
    else:
        print(1, end=" ")


#
# 시간 초과 풀이
#
##import sys
##
##n = int(sys.stdin.readline())
##sang = list(map(int, sys.stdin.readline().split()))
##m = int(sys.stdin.readline())
##chk = list(map(int, sys.stdin.readline().split()))
##rst = [0 for x in range(m)]
##
##for i in range(m):
##    if (chk[i] in sang):
##        rst[i] = 1
##
##print(*rst)
