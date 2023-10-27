# 9291

import sys

t = int(sys.stdin.readline())
for casex in range(1, t+1):
    sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
    state = True
    
    # row(행)
    for row in sudoku:
        check = {i:0 for i in range(1, 10)}
        for r in row:
            #print(r)
            check[r] += 1
        if (list(check.values()) != [1]*9):
            state = False

    # column(열)
    for x in range(9):
        check = {i:0 for i in range(1, 10)}
        for y in range(9):
            check[sudoku[y][x]] += 1
        if (list(check.values()) != [1]*9):
            state = False

    # 3x3
    pair = [(0, 0), (3, 0), (6, 0), (0, 3), (3, 3), (6, 3), (0, 6), (3, 6), (6, 6)]
    for p in pair:
        check = {i:0 for i in range(1, 10)}
        for a in range(p[0], p[0]+3):
            for b in range(p[1], p[1]+3):
                #print(a, b)
                check[sudoku[a][b]] += 1
        if (list(check.values()) != [1]*9):
            state = False

    print(f"Case {casex}: {['INCORRECT', 'CORRECT'][int(state)]}")

    try:
        line = sys.stdin.readline()
    except:
        pass
