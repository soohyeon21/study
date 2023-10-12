# 1681

# 라벨의 숫자는 1,000,000을 넘을 수 있으므로 while문 대신 for i in range(1, 1000001)은 좋지 않은 생각.

#
# sol1) label list
#
##import sys
##
##n, l = map(int, sys.stdin.readline().split())
##
##label = []
##num = 1
##while (len(label) != n):
##    if (str(l) not in str(num)):
##        label.append(num)
##    num += 1
##
##print(label[-1])



#
# sol2) list 대신 variable 사용 풀이
# 시간은 비슷하고 메모리는 절반 이상 줄어듦.
#
import sys

n, l = map(int, sys.stdin.readline().split())

biggest = 0
cnt = 0
num = 1
while (cnt != n):
    if (str(l) not in str(num)):
        biggest = num
        cnt += 1
    num += 1

print(biggest)
