# 1773

#
# sol1) 틀림...
# n(합집합) - sum(n(각각 2개 교집합)) + n(몽땅 교집합) 생각했는데...
#

##import sys
##
##def gcf(a, b): # 6, 3
##    while (b != 0):
##        num = a % b
##        a = b
##        b = num
##    return a
##
##def lcm(a, b):
##    return a*b//gcf(a, b)
##
##n, c = map(int, sys.stdin.readline().split())
##students = [int(sys.stdin.readline()) for _ in range(n)]
##
##total = 0
##same = c+1
##for i in range(n):
##    total += c//students[i]
##    for j in range(i+1, n):
##        total -= c//lcm(students[i], students[j])
##        if (n > 2):
##            same = lcm(students[i], students[j])
##total += c//same
##
##print(total)



#
# sol2) Python3 시간 초과, PyPy3 정답
#
import sys

n, c = map(int, sys.stdin.readline().split())
students = [int(sys.stdin.readline()) for _ in range(n)]

firework = {i:0 for i in range(2000001)}
for student in students:
    for k in range(1, c//student+1):
        firework[k*student] = 1

print(list(firework.values()).count(1))
