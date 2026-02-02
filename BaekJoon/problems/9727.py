# 9727

# +True >>> 1
# +False >>> 0

import sys

t = int(sys.stdin.readline())
for idx in range(1, t+1):
    sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(6)]
    all_num = {an for an in range(1, 7)}
    
    rectangle = True
    for i in range(3):
        for j in range(2):
            tmp_rect = set()
            for ver in range(i*2, i*2+2):
                for hor in range(j*3, j*3+3):
                    tmp_rect.add(sudoku[ver][hor])
            if (tmp_rect != all_num):
                rectangle = False
                
    vertical = True
    for line in sudoku:
        if (set(line) != all_num):
            vertical = False

    horizontal = True
    for c in range(6):
        tmp_hor = [sudoku[r][c] for r in range(6)]
        if (set(tmp_hor) != all_num):
            horizontal = False

    rightdown = True
    tmp_rd = [sudoku[k][k] for k in range(6)]
    if (set(tmp_rd) != all_num):
        rightdown = False

    rightup = True
    tmp_ru = [sudoku[5-p][p] for p in range(6)]
    if (set(tmp_ru) != all_num):
        rightup = False

    print(f"Case#{idx}: {int(rectangle and vertical and horizontal and rightdown and rightup)}")
