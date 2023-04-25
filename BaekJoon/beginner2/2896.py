# 2896

# min값 사용

# 0.0이나 0이나 답으로 모두 인정된다.
# 칵테일을 만드는 데 필요한 주스의 양은 정수로만 한정되어있지 않다.
# 굳이 최대공약수를 구하지 않고 바로 나누어도 된다.

#
# sol1
#
##import sys
##
##def gcf(aa, bb):
##    while (bb != 0):
##        num = aa % bb
##        aa = bb
##        bb = num
##    return aa
##
##juice = list(map(int, sys.stdin.readline().split()))
##ratio = list(map(int, sys.stdin.readline().split()))
##
##gcfn = gcf(gcf(ratio[0], ratio[1]), ratio[2])
##ratio = [ratio[x]//gcfn for x in range(3)]
##
##possible = min(list(juice[x]/ratio[x] for x in range(3)))
##result = []
##for i in range(3):
##    tmp = juice[i] - ratio[i]*possible
##    if (tmp == int(tmp)):
##        tmp = int(tmp)
##    result.append(tmp)
##
##print(*result)



#
# sol2
#
import sys

a, b, c = map(int, sys.stdin.readline().split())
i, j, k = map(int, sys.stdin.readline().split())

minn = min(a/i, b/j, c/k)
print(a-i*minn, b-j*minn, c-k*minn)
