# 181835
# 조건에 맞게 수열 변환하기 3

def solution(arr, k):
    for i in range(len(arr)):
        if (k%2 == 1):
            arr[i] *= k
        else:
            arr[i] += k
    
    return arr
