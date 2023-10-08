# 1051

# 우와 만약 최대 직사각형을 구하는 거였으면...?
# 그 위치에 있는지 확인하는 대신, 모든 줄을 훑어가며 확인하기?

# 각각의 모든 좌표를 기준으로 정사각형의 한 변의 길이를 늘려가면서 꼭짓점 4개의 수가 같은지 확인하는 풀이도 있음

# sol4가 제일 깔끔해보임

#
# sol1) 각 row에서 가능한 정사각형 한 변 길이 찾고 나머지 위치에도 똑같은 숫자가 있는지 확인
#
import sys

n, m = map(int, sys.stdin.readline().split())
sq = [sys.stdin.readline().rstrip() for x in range(n)]

possible = [1] # 점인 경우 미리 포함
for num in range(10): # 각 숫자에 대해
    for row in range(n): # 각 row에 대해
        if (sq[row].count(str(num)) > 1): # 해당 row에 꼭짓점 최소 2개 이상 있음?
            wcan = [] # 해당 row에 있는 num의 index
            for i in range(m):
                if (sq[row][i] == str(num)):
                    wcan.append(i)
            for idx1 in range(len(wcan)): # wcan 안에 있는 num을 기준으로 정사각형 찾기
                for idx2 in range(idx1+1, len(wcan)):
                    edge = wcan[idx2] - wcan[idx1]
                    try:
                        if ((sq[row+edge][wcan[idx1]] == str(num)) and (sq[row+edge][wcan[idx2]] == str(num))):
                            possible.append((edge+1)**2)
                    except: # 만약 정사각형이 NxM을 벗어나는 경우 처리
                        continue

print(max(possible))



#
# sol2) 틀린 풀이. 각 좌표를 기준으로 한 변의 길이를 다르게 하면서 정사각형을 만들어보기. 시도해봄.
# 한 변의 길이 설정을 긴 놈부터 하는 게 좋은듯?
#
##import sys
##
##def squareEdge(square, row, col):
##    for length in range(1, min(n,m)-1):
##        if ((row+length >= n) or (col+length >= m)):
##            return 0
##        else:
##            if (square[row][col] == square[row+length][col] == square[row][col+length] == square[row+length][col+length]):
##                return length+1
##            else:
##                return 0
##
##n, m = map(int, sys.stdin.readline().split())
##sq = [sys.stdin.readline().rstrip() for x in range(n)]
##
##area = [1]
##for i in range(n):
##    for j in range(m):
##        edge = squareEdge(sq, i, j)
##        area.append(edge**2)
##
##print(max(area))



#
# sol3) 누군가의 풀이
#
##import sys
##
##def findSquare(length):
##    for row in range(n-length+1):
##        for col in range(m-length+1):
##            if (sq[row][col] == sq[row][col+length-1] == sq[row+length-1][col] == sq[row+length-1][col+length-1]):
##                return True
##    return False
##
##n, m = map(int, sys.stdin.readline().split())
##sq = [sys.stdin.readline().rstrip() for x in range(n)]
##
##maxLen = min(n, m)
##for edge in range(maxLen, 0, -1):
##    if (findSquare(edge)):
##        print(edge**2)
##        break



#
# sol4) 누군가의 풀이
#
import sys

def findSquare(y, x):
    global rst

    for length in range(1, m-x): # 정사각형 한 변 길이 늘려보면서 만들 수 있는지 확인
        if (length+y >= n): # 영역을 벗어나면 종료
            return
        if (sq[y][x] == sq[y+length][x] == sq[y][x+length] == sq[y+length][x+length]): # 정사각형 확인
            rst = max(rst, (length+1)**2)

n, m = map(int, sys.stdin.readline().split())
sq = [sys.stdin.readline().rstrip() for x in range(n)]

rst = 1

for i in range(n):
    for j in range(m):
        findSquare(i, j)

print(rst)
