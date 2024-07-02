# 1975

# 재귀나 DP를 사용하면 시간초과가 안나려나...? 흠...

#
# sol1) Python3, PyPy3 시간 초과
# [1, n+1]의 base에 대해 모든 자리의 진법변환수를 찾아서 연속 0 세기
#
##import sys
##
##def change(base, num):
##    result = []
##    while (num != 0):
##        result += [num%base]
##        num //= base
##    return result
##
##t = int(sys.stdin.readline())
##for _ in range(t):
##    n = int(sys.stdin.readline())
##    zeros = 0
##    for base in range(2, n+1):
##        reversed_rst = change(base, n)
##        for each in reversed_rst:
##            if (each == 0):
##                zeros += 1
##            else:
##                break
##    print(zeros)



#
# sol2) Python3 시간 초과, PyPy3 정답
# [2, n+1]의 base에 대해 진법변환수의 끝에 0이 나올 때까지만 세기
#
import sys

def consecutive(base, num):
    result = []
    zeros = 0
    while (1):
        if (num % base == 0):
            zeros += 1
            num //= base
        else:
            return zeros

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    total = 0
    for base in range(2, n+1):
        total += consecutive(base, n)
    print(total)



#
# sol3) Python3, PyPy3 시간 초과
# n의 약수를 구하고 n까지 포함해서 base를 정하고, 진법변환수에서 0이 나올 때까지만 세기
#
##import sys
##
##def consecutive(base, num):
##    result = []
##    zeros = 0
##    while (1):
##        if (num % base == 0):
##            zeros += 1
##            num //= base
##        else:
##            return zeros
##
##def get_factors(n):
##    factors = []
##    for i in range(2, n//2+1):
##        if (n % i == 0):
##            factors.append(i)
##    final = factors
##    for f in factors:
##        pair = n//f
##        if (pair not in final):
##            final.append(pair)
##    return final
##
##t = int(sys.stdin.readline())
##for _ in range(t):
##    n = int(sys.stdin.readline())
##    total = 0
##    possible = get_factors(n) + [n]
##    for base in possible:
##        total += consecutive(base, n)
##    print(total)
