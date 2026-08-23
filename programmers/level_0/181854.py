# 181854
# 배열의 길이에 따라 다른 연산하기

def solution(arr, n):
    for i in range(len(arr)):
        arr[i] += (len(arr)%2 * ((i+1)%2)*n) + ((len(arr)+1)%2 * (i%2)*n) # (len(arr) 홀수인 경우) + (len(arr) 짝수인 경우)
    return arr
