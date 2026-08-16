# 181858
# 무작위로 K개의 수 뽑기

def solution(arr, k):
    answer = []
    for i in range(len(arr)):
        if (arr[i] not in answer):
            answer.append(arr[i])
    
    return answer[:k] + [-1]*(k-len(answer))
