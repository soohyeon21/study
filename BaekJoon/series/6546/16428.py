# 16428

#
# 130점
#
##import sys
##
##a, b = map(int, sys.stdin.readline().split())
##if ((b > 0) or (a == 0)):
##    q = a//b
##elif (b < 0):
##    q = a//b+1
####q = a//b if a//b >= 0 else a//b+1
##r = a - q*b
##print(q)
##print(r)


#
# 630점(만점)
#
import sys

a, b = map(int, sys.stdin.readline().split())

q = a//b
r = a%b
if ((a != 0) and (r < 0)):
    q += 1
    r -= b

print(q)
print(r)
