# 120897
# 약수 구하기

def solution(n):
    answer = set()
    for i in range(1, int(n**0.5)+1):
        if (n%i == 0):
            answer.add(i)
            answer.add(n//i)
            
    answer = sorted(list(answer))
    
    return answer
