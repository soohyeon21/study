# 2의 영역

def solution(arr):
    if (2 in arr):
        sidx = arr.index(2)
        eidx = len(arr) - arr[::-1].index(2)
        return arr[sidx:eidx]
    else:
        return [-1]
