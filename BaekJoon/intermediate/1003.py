# 1003

# Dynamic Programming

# 피보나치 함수
# 푸는 방법은 다양하다.

#
# sol1
# 0과 1 출력 횟수 각각 다른 함수 써서 구하기
#
##import sys
##
##def fibon0(n):
##    if (fibolist0[n] == 0):
##        if (n == 0):
##            fibolist0[n] = 1
##        elif (n == 1):
##            fibolist0[n] = 0
##        else:
##            fibolist0[n] = fibon0(n-1) + fibon0(n-2)
##    return fibolist0[n]
##
##def fibon1(n):
##    if (fibolist1[n] == 0):
##        if (n == 0):
##            fibolist1[n] = 0
##        elif (n == 1):
##            fibolist1[n] = 1
##        else:
##            fibolist1[n] = fibon1(n-1) + fibon1(n-2)
##    return fibolist1[n]
##
##t = int(sys.stdin.readline())
##for _ in range(t):
##    n = int(sys.stdin.readline())
##    fibolist0 = [0 for x in range(41)]
##    fibolist1 = [0 for x in range(41)]
##    print(fibon0(n), fibon1(n))



#
# sol2
# 0과 1 한번에 구하기
#
##import sys
##
##def fibo(n):
##    if (flist[n] == [0, 0]):
##        if (n == 0):
##            flist[n] = [1, 0]
##        elif (n == 1):
##            flist[n] = [0, 1]
##        else:
##            flist[n] = [fibo(n-1)[0] + fibo(n-2)[0], fibo(n-1)[1] + fibo(n-2)[1]]
##    return flist[n]
##
##t = int(sys.stdin.readline())
##for _ in range(t):
##    n = int(sys.stdin.readline())
##    flist = [[0, 0] for x in range(41)]
##    print(*fibo(n))



#
# sol3
# 피보나치 수열 미리 다 구하기 + def 함수 안쓰고
#
##import sys
##
##fibo = [0 for x in range(41)]
##fibo[0] = (1, 0)
##fibo[1] = (0, 1)
##for i in range(2, 41):
##    fibo[i] = (fibo[i-1][0] + fibo[i-2][0], fibo[i-1][1] + fibo[i-2][1])
##
##t = int(sys.stdin.readline())
##for _ in range(t):
##    n = int(sys.stdin.readline())
##    print(*fibo[n])



#
# sol4
# 0의 출현빈도와 1의 출현빈도 사이 관계 구하기
# 0: 1 0 1 1 2 3 5  8 13 21 ...
# 1: 0 1 1 2 3 5 8 13 21 34 ...
#
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    zeros, ones = 1, 0
    for i in range(n):
        zeros, ones = ones, zeros+ones
    print(zeros, ones)
