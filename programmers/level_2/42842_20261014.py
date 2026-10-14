# 42842
# 카펫

def solution(brown, yellow):
    poss_y = []
    
    whole = brown + yellow
    for i in range(1, int(whole**0.5)+1):
        if (whole % i == 0):
            poss_y.append(i)
    
    for y in poss_y:
        x = whole//y
        if (brown == 2*(x-1)+2*(y-1)):
            return [x, y]
