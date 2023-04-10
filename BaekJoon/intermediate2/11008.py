# 11008

#
# sol1
#
##import sys
##
##t = int(sys.stdin.readline())
##for _ in range(t):
##    s, p = sys.stdin.readline().split()
##    n = 0
##    sec = 0
##    while (n != len(s)):
##        if (len(s) - len(s[:n]) < len(p)):
##            sec += len(s[n:])
##            break
##        if (s[n:n+len(p)] == p):
##            sec += 1
##            n += len(p)
##        else:
##            sec += 1
##            n += 1
##    print(sec)


#
# sol2) count(), replace() 사용
#
##import sys
##
##t = int(sys.stdin.readline())
##for _ in range(t):
##    s, p = sys.stdin.readline().split()
##    sec = s.count(p)
##    s = s.replace(p, "")
##    sec += len(s)
##    print(sec)


#
# sol3) split() 사용
#
# len("") = 0
#
# oxoxo에서 x를 기준으로 split 하면 o 3개가 나온다.
# o 사이사이에 x개 끼어있다 생각하면 o가 3개일때 반대로 x는 2개이다.
#
# "12a34a5a".split("a") >>> ["12", "34", "5", ""]
#
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    s, p = sys.stdin.readline().split()
    sec = len(s.split(p)) - 1 # p의 개수
    sec += sum(map(len, s.split(p))) # p 아닌거
    print(sec)
