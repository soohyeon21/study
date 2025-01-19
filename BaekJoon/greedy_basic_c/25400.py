# 25400

#
# sol1) 그냥 1부터 차례로 찾아가면서 있으면 다음 숫자 확인, 없으면 제거+1
#
import sys

n = int(sys.stdin.readline())
an = list(map(int, sys.stdin.readline().split()))

now = 1
removal = 0
for i in range(n):
    if (an[i] == now):
        now += 1
    else:
        removal += 1

print(removal)



#
# sol2) 틀림. 21/100점. 왜 틀렸지????
# 1부터 시작해서 나머지 list에 해당 숫자가 있는지 없는지 판단하는 방식.
#
##import sys
##
##n = int(sys.stdin.readline())
##an = list(map(int, sys.stdin.readline().split()))
##
##before = 0
##removal = 0
##for num in range(1, max(max(an)+1, n+1)):
##    if (num in an[before:]):
##        before = an.index(num)
##    else:
##        removal = n-(num-1)
##        break
##
##print(removal)
