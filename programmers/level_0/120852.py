# 120852
# 소인수분해

def solution(n):
    pnum = [1 for _ in range(10001)]
    pnum[0], pnum[1] = 0, 0
    for i in range(2, 101):
        for j in range(2, 10000//i+1):
            pnum[i*j] = 0
    
    answer = []
    for k in range(n+1):
        if ((pnum[k] == 1) and (n%k == 0)):
            answer.append(k)
    
    return answer
