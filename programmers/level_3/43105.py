# 43105
# 정수 삼각형

###
### botton-up
###
# def solution(triangle):
#     for row in reversed(range(len(triangle))):
#         for th in range(len(triangle[row])-1):
#             triangle[row-1][th] += max(triangle[row][th], triangle[row][th+1])
    
#     return triangle[0][0]


###
### top-down
### 뭐가 고정이고 뭐가 달라지는지 확인하자!
###
def solution(triangle):
    for row in range(1, len(triangle)):
        for th in range(len(triangle[row])):
            if (th == 0):
                triangle[row][th] += triangle[row-1][th]
            elif (th == row):
                triangle[row][th] += triangle[row-1][th-1]
            else:
                triangle[row][th] += max(triangle[row-1][th-1], triangle[row-1][th])
    
    return max(triangle[-1])
