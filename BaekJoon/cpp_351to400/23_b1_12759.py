# 12759

# 처음에는 player1, 2로 하려니까 세로줄 확인할때 등식이 너무 길어지는 것 같아서 player1, 5로 바꿈.

# 대각선도 "직선"으로 3개가 이어지는 경우에 속한다.
# 쳇. 잠깐 고민했다가 포함 안시켰더니 첫시도는 틀려버렸다.

import sys

start = int(sys.stdin.readline())
player = []
if (start == 1):
    player = [1, 5]
else:
    player = [5, 1]

ttt = [[0 for aa in range(3)] for bb in range(3)]

loc = 0
state = "yet"
for _ in range(9):
    x, y = map(int, sys.stdin.readline().split())
    ttt[x-1][y-1] = player[loc]

    for i in range(3): # 가로
        if (sum(ttt[i]) == player[loc]*3):
            state = "end"
            break
    for j in range(3): # 세로
        if (ttt[0][j] + ttt[1][j] + ttt[2][j] == player[loc]*3):
            state = "end"
            break
    if ((ttt[0][0] + ttt[1][1] + ttt[2][2] == player[loc]*3) or (ttt[2][0] + ttt[1][1] + ttt[0][2] == player[loc]*3)): # 대각선
        state = "end"
    
    if (state == "end"): # 만약 중간에 게임이 끝나면
        if (player[loc] == 5):
            player[loc] = 2
        print(player[loc])
        break

    loc = (loc+1)%2

if (state == "yet"):
    print(0)
