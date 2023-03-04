# 1225

# a = '345'
# aa = sum(map(int, a)) # aa는 12

#
# sol1 (시간초과)
#
##import sys
##
##a, b = sys.stdin.readline().split()
##
##mul = 0
##for leta in a:
##    for letb in b:
##        mul += int(leta) * int(letb)
##
##print(mul)



#
# sol2
#
import sys

a, b = sys.stdin.readline().split()

suma = sum(int(leta) for leta in a)
sumb = sum(int(letb) for letb in b)

print(suma * sumb)
