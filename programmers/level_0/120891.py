# 120891
# 369게임

def solution(order):
    answer = 0
    for num in str(order):
        if (num in '369'):
            answer += 1
            
    return answer
