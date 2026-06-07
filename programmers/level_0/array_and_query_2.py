# 수열과 구간 쿼리 2

def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        minn = max(arr[s:e+1])
        state = False
        for i in range(s, e+1):
            if (arr[i] > k):
                minn = min(minn, arr[i])
                state = True
        
        if (state):
            answer.append(minn)
        else:
            answer.append(-1)
        
    return answer
