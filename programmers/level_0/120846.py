# 120846
# 합성수 찾기

def solution(n):
    prime = [True for _ in range(101)]
    prime[0], prime[1] = False, False
    for i in range(2, 11):
        for j in range(2, 100//i+1):
            prime[i*j] = False
    
    answer = 0
    for k in range(2, n+1): # 1은 소수도, 합성수도 아님.
        if (prime[k] == False):
            answer += 1
    
    return answer
