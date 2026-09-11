# 181839
# 주사위 게임 1

def solution(a, b):
    answer = 0
    
    cal = [a%2, b%2]
    if (sum(cal) == 2):
        answer = a**2 + b**2
    elif (sum(cal) == 1):
        answer = 2*(a+b)
    else:
        answer = abs(a-b)
    return answer
