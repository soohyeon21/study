# 181830
# 정사각형으로 만들기

# 주의 예시
# [[1, 1], [1, 1], [1, 1], [1, 1]] # [[1, 1, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0]]

def solution(arr):
    row = len(arr)
    col = len(arr[0])
    if (col > row):
        for k in range(col-row):
            arr.append([0]*col)
    elif (row > col):
        for i in range(len(arr)):
            arr[i].extend([0]*(row-col))
    return arr
