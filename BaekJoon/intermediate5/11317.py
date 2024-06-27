# 11317

# 
# sol1) math.sqrt() 사용
# math.sqrt()는 음수에 대해 'ValueError: math domain error'를 발생시킨다.
#
##import sys
##import math
##
##n = int(sys.stdin.readline())
##for _ in range(n):
##    a, b, c, s, t = map(int, sys.stdin.readline().split())
##
##    if ((b**2-4*a*c) >= 0): # 실수 근이 존재하는가?
##        xp = (-b+math.sqrt(b**2-4*a*c)) / (2*a)
##        xm = (-b-math.sqrt(b**2-4*a*c)) / (2*a)
##        
##        if ((s <= xp <= t) or (s <= xm <= t)):
##            print("Yes")
##        else: # 실수 근이 해당 범위 내에 없음
##            print("No")
##    else: # 복소수(complex number)인 경우
##        print("No")



#
# sol2) ()**0.5 사용
# 실근을 찾아야 하기 때문에 루트 안의 수(b**2 - 4*a*c)의 값을 확인해야 한다.
#
# "TypeError: '<=' not supported between instances of 'int' and 'complex'"
# x가 [s, t]에 존재하는지 확인하려면 우선 (b**2 - 4*a*c)>=0인지 확인하고 진행해야지, 안그러면 TypeError가 발생한다.
#
import sys

n = int(sys.stdin.readline())
for _ in range(n):
    a, b, c, s, t = map(int, sys.stdin.readline().split())

    xp = (-b+(b**2-4*a*c)**0.5) / (2*a)
    xm = (-b-(b**2-4*a*c)**0.5) / (2*a)
        
    if ((b**2-4*a*c) >= 0):        
        if ((s <= xp <= t) or (s <= xm <= t)):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
