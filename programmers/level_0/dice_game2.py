# 주사위 게임 2

def solution(a, b, c):
    set_abc = set([a, b, c])
    
    if (len(set_abc) == 3):
        return a+b+c
    elif (len(set_abc) == 2):
        return (a+b+c) * (a**2 + b**2 + c**2)
    elif (len(set_abc) == 1):
        return (a+b+c) * (a**2+b**2+c**2) * (a**3+b**3+c**3)
