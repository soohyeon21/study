# 14709

# 생각보다 치사한 문제.
# (1, 3), (3, 4) 2개만 주어졌어도 여우를 만들 수 있다고 생각했는데, 틀리다고 처리된다. #1
# (1, 3), (3, 4), (1, 4)가 반드시 1개씩 있는지 확인해야 한다(순서쌍 순서 무관).    #2
# "여우 사인은 엄지손가락, 중지, 약지 세 손가락을 '서로 끝이 맞닿도록' 모으고"
# (음... 문제를 제대로 안읽은 탓인가...?ㅎ)

# sol2,3도 #1의 연장선에서 작성한 코드여서 틀린듯.

# sol2에서 (min(), max())를 사용해서 쌍을 만들면 (1, 3), (3, 1) 이렇게 2번 작성하지 않아도 된다.

#
# sol1) 맞은 풀이
#
import sys

n = int(sys.stdin.readline())
hand = {i:0 for i in range(1, 6)}

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    hand[a] += 1
    hand[b] += 1

if ((hand[1]>1) and (hand[3]>1) and (hand[4]>1) and (hand[2]==0) and (hand[5]==0)):
    print("Wa-pa-pa-pa-pa-pa-pow!")
else:
    print("Woof-meow-tweet-squeek")


#
# sol2) 틀린 풀이
#
##import sys
##
##n = int(sys.stdin.readline())
##hand = [tuple(map(int, sys.stdin.readline().split())) for x in range(n)]
##answer = [(1, 3), (3, 1), (1, 4), (4, 1), (3, 4), (4, 3)]
##state = "Wa-pa-pa-pa-pa-pa-pow!"
##
##for h in hand:
##    if (h not in answer):
##        state = "Woof-meow-tweet-squeek"
##        break
##
##print(state)


#
# sol3) 틀린 풀이
#
##import sys
##
##n = int(sys.stdin.readline())
##hand = [tuple(map(int, sys.stdin.readline().split())) for x in range(n)]
##state = "Wa-pa-pa-pa-pa-pa-pow!"
##
##chk = {hand[0][0], hand[0][1]}
##for i in range(1, n):
##    #chk = {hand[i][0], hand[i][1]} | chk
##    chk.add(hand[i][0])
##    chk.add(hand[i][1])
##    if ((2 in chk) or (5 in chk)):
##        state = "Woof-meow-tweet-squeek"
##        break
##
##if (chk != {1, 3, 4}):
##    state = "Woof-meow-tweet-squeek"
##
##print(state)
