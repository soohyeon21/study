# 181837
# 커피 심부름

def solution(order):
    coffee = [0, 0] # americano, latte
    for person in order:
        if ('latte' in person):
            coffee[1] += 1
        else:
            coffee[0] += 1
    
    answer = coffee[0]*4500 + coffee[1]*5000
    
    return answer
