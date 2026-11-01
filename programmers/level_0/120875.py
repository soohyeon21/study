# 120875
# 평행

def decline(dot1, dot2):
    d = (dot1[1] - dot2[1]) / (dot1[0] - dot2[0])
    return d

def solution(dots):
    answer = 0
    if (decline(dots[0], dots[1]) == decline(dots[2], dots[3])):
        answer = 1
    if (decline(dots[0], dots[2]) == decline(dots[1], dots[3])):
        answer = 1
    if (decline(dots[0], dots[3]) == decline(dots[1], dots[2])):
        answer = 1
    
    return answer
