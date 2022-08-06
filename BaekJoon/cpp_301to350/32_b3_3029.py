# 3029

# 1) 왜 내 풀이는 틀렸지?
# ㄴ "정인이는 적오도 1초를 기다리며, 많아야 24시간을 기다린다."
# ㄴ 입력으로 주어지는 2개의 시간이 같으면 00:00:00이 아니라 24:00:00을 출력해야 된다는 의미.
# ㄴ 다른 input에 대해서는 맞았는데도 틀렸다면, 조건의 양 끝값을 확인해보자.
# 2) 시간을 sec로 전환해서 min과 hour을 알아내는 방법?
# ㄴ hour: //3600 or //60//60
# ㄴ min: //60%60
# ㄴ sec: %60

#
# someone's 풀이 
#
##h1, m1, s1 = map(int, input().split(':'))
##h2, m2, s2 = map(int, input().split(':'))
##t1 = h1*60*60 + m1*60 + s1
##t2 = h2*60*60 + m2*60 + s2
##t = t2 - t1 if t2 > t1 else t2-t1+24*60*60
##h = t//60//60
##m = t//60 % 60
##s = t%60
##print("%02d:%02d:%02d" % (h, m, s))

#
# my 풀이
#
import sys

now = list(map(int, sys.stdin.readline().split(":")))
bomb = list(map(int, sys.stdin.readline().split(":")))

nsum = now[0]*60*60 + now[1]*60 + now[2]
bsum = bomb[0]*60*60 + bomb[1]*60 + bomb[2]
wsum = bsum - nsum
if (nsum >= bsum):
    wsum += 24*60*60
wait = [wsum//3600, wsum//60%60, wsum%60]
print("%02d:%02d:%02d" %(wait[0], wait[1], wait[2]))
