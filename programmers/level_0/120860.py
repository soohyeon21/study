# 120860
# 직사각형 넓이 구하기

def solution(dots):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = dots
    hor = max(abs(x1-x2), abs(x1-x3), abs(x1-x4))
    ver = max(abs(y1-y2), abs(y1-y3), abs(y1-y4))
    
    return hor*ver
