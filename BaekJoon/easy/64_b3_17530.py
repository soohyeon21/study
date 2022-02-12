# 17530

# 어째서 첫 if로 tie 발생한 경우를 걸러내면 틀린 문제 처리가 되는 걸까...?

# "If there is a tie between one or more candidates,
#  the one who registered first is elected."
# => tie가 발생하면 무조건 첫 후보자가 당선되는 것이 아니라,
#    tie가 발생한 사람 중에서 먼저 후보자 등록을 한 사람이 당선된다는 이야기다.

# 허허.... 사실 처음 이해한 거는 말이 안되는 선거 방식이긴 하지ㅎㅎ

import sys

n = int(sys.stdin.readline())
cand = []
for _ in range(n):
    cand.append(int(sys.stdin.readline()))

##if (len(cand) != len(set(cand))): # tie 발생
##    print("S")
##elif (cand[0] == max(cand)): # 최다 득표
##    print("S")
##else:
##    print("N")
    
if (cand[0] == max(cand)): # 최다 득표
    print("S")
else:
    print("N")
