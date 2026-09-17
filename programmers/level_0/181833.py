# 181833
# 특별한 이차원 배열 1

# answer = [[0]*n for _ in range(n)] # 이것도 하나의 방법

def solution(n):
    answer = [[0 for x1 in range(n)] for x2 in range(n)]
    for i in range(n):
        answer[i][i] = 1
    return answer
