# 1331

import sys

def only_once(curr):
    row, col = 5-(int(curr[1])-1), ord(curr[0])-65
    board[row][col] += 1
    if (board[row][col] > 1):
        return False
    return True

def isRightWay(idx0, idx1):
    row0, row1 = 5-(int(visited[idx0][1])-1), 5-(int(visited[idx1][1])-1)
    col0, col1 = ord(visited[idx0][0])-65, ord(visited[idx1][0])-65
    if (abs(row0-row1)*abs(col0-col1) != 2):
        return False
    return True
    

visited = [sys.stdin.readline().rstrip() for _ in range(36)]
board = [[0 for x in range(6)] for y in range(6)]

check = True
for i in range(36):
    # 재방문 여부 확인
    check = only_once(visited[i]) and check

    # 나이트 이동 규칙 준수 확인
    if (i > 1):
        check = check and isRightWay(i-1, i)

    # 마지막에 돌아오는지 확인
    if (i == 35):
        check = check and isRightWay(35, 0)

if (check):
    print("Valid")
else:
    print("Invalid")
