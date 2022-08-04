# 3029

# 왜 내 풀이는 틀렸지?
# 시간을 sec로 전환해서 min과 hour을 알아내는 방법?

#
# someone's 풀이 
#
h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
t1 = h1*60*60 + m1*60 + s1
t2 = h2*60*60 + m2*60 + s2
t = t2 - t1 if t2 > t1 else t2-t1+24*60*60
h = t//60//60
m = t//60 % 60
s = t%60
print("%02d:%02d:%02d" % (h, m, s))

#
# my 풀이
#
##import sys
##
##now = list(map(int, sys.stdin.readline().split(":")))
##bomb = list(map(int, sys.stdin.readline().split(":")))
##
##if (bomb[0] < now[0]):
##    bomb[0] += 24
##nsum = now[0]*60*60 + now[1]*60 + now[2]
##bsum = bomb[0]*60*60 + bomb[1]*60 + bomb[2]
##wsum = bsum - nsum
##wait = [wsum//60//60, wsum//60%60, wsum%60]
##print("%02d:%02d:%02d" %(wait[0], wait[1], wait[2]))
