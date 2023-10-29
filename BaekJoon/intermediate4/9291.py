# 9291

#
# sol1)
#
##import sys
##
##t = int(sys.stdin.readline())
##for casex in range(1, t+1):
##    sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
##    state = True
##    
##    # row(행)
##    for row in sudoku:
##        check = {i:0 for i in range(1, 10)}
##        for r in row:
##            #print(r)
##            check[r] += 1
##        if (list(check.values()) != [1]*9):
##            state = False
##
##    # column(열)
##    for x in range(9):
##        check = {i:0 for i in range(1, 10)}
##        for y in range(9):
##            check[sudoku[y][x]] += 1
##        if (list(check.values()) != [1]*9):
##            state = False
##
##    # 3x3
##    pair = [(0, 0), (3, 0), (6, 0), (0, 3), (3, 3), (6, 3), (0, 6), (3, 6), (6, 6)]
##    for p in pair:
##        check = {i:0 for i in range(1, 10)}
##        for a in range(p[0], p[0]+3):
##            for b in range(p[1], p[1]+3):
##                #print(a, b)
##                check[sudoku[a][b]] += 1
##        if (list(check.values()) != [1]*9):
##            state = False
##
##    print(f"Case {casex}: {['INCORRECT', 'CORRECT'][int(state)]}")
##
##    try:
##        line = sys.stdin.readline()
##    except:
##        pass



#
# sol2) def 사용, row&cols/3x3 sol1보다 더 짜임새 있게.
#
# 만약에 중간에 특정 조건 충족시 그 이후 작업이 불필요한 경우가 있다면 def return 사용 적극 고려할 것.
import sys

def isCorrect(board):
    # rows & cols
    for i in range(9):
        row_check, col_check = [], []
        for j in range(9):
            if ((board[i][j] in row_check) or (board[j][i] in col_check)):
                return False
            row_check.append(board[i][j])
            col_check.append(board[j][i])

    # 3x3
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            box_check = []
            for p in range(3):
                for q in range(3):
                    if (board[x+p][y+q] in box_check):
                        return False
                    box_check.append(board[x+p][y+q])

    return True


t = int(sys.stdin.readline())
for casenum in range(1, t+1):
    # 빈 줄 처리
    if (casenum > 1):
        sys.stdin.readline()
    
    sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

    print(f"Case {casenum}: {['INCORRECT', 'CORRECT'][int(isCorrect(sudoku))]}")
