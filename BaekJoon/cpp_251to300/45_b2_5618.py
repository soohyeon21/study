# 5618

# 최대공약수의 약수 == 공약수

# list에 약수 찾아서 넣고 출력하면 시간 초과가 뜬다...
# 얘 좀 이상함. 똑같은 풀이 인데도 어떨 땐 맞고 어떨 땐 틀린다. 뭐지??

# 옛날에 풀었다가 다시 푼 문제. 그 사이 조금은 성장했나보다.
# 전에는 순수하게 약수 찾는 식으로 풀어서 시간 초과가 났었다.

import sys

def GCF(num1, num2):
    while (num2 != 0):
        num = num1 % num2
        num1 = num2
        num2 = num
    return num1

n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))
gcf = GCF(GCF(nlist[0], nlist[1]), nlist[-1])

# 약수 찾기1
for i in range(1, gcf//2 + 1):
    if (gcf % i == 0):
        print(i)
print(gcf)

# 약수 찾기2
##cf = []
##for i in range(1, gcf//2 + 1):
##    if (gcf % i == 0):
##        cf.append(i)
##cf.append(gcf)
##print(*cf, sep="\n")
