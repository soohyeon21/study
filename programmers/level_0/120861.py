# 120861
# 캐릭터의 좌표

def solution(keyinput, board):
    x, y = 0, 0
    xmax = board[0]//2
    ymax = board[1]//2
    for kipt in keyinput:
        if (kipt == 'left'):
            x -= 1
            x = max(-xmax, x)
        elif (kipt == 'right'):
            x += 1
            x = min(x, xmax)
        elif (kipt == 'up'):
            y += 1
            y = min(y, ymax)
        elif (kipt == 'down'):
            y -= 1
            y = max(-ymax, y)
    
    return [x, y]
