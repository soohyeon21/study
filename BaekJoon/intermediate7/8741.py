# 8741

# 오옹 얘도 나름 신기한 규칙이 있나보다! k 개수만큼 1을 출력하고, (k-1)개만큼 0을 출력하는!

#
# sol1) classic
#
##import sys
##
##k = int(sys.stdin.readline())
##max_num = 2**k
##total = (max_num-1)*max_num//2
##print(bin(total)[2:])



#
# sol2) 신기방기
#
import sys

k = int(sys.stdin.readline())
print("1"*k + "0"*(k-1))
