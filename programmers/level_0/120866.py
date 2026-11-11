# 120866
# 안전지대

def solution(board):
    n = len(board)
    for x in range(n):
        for y in range(n):
            if (board[x][y] == 1):
                for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    nx = x + dx
                    ny = y + dy
                    if ((0 <= nx < n) and (0 <= ny < n)):
                        if (board[nx][ny] != 1):
                            board[nx][ny] = 2
    
    safe = 0
    for each in board:
        safe += each.count(0)
    
    return safe
