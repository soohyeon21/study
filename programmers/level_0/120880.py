# 120880
# 특이한 정렬

# answer = sorted(numlist,key = lambda x : (abs(x-n), n-x)) # 한번에도 가능.

def solution(numlist, n):
    diff = [(abs(n-num), num) for num in numlist]
    diff.sort(key=lambda x:(x[0], -x[1]))
    
    answer = [v2 for v1, v2 in diff]
    return answer
