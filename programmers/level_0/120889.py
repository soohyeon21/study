# 120889
# 삼각형의 완성조건 (1)

def solution(sides):
    if (max(sides) < sum(sides)-max(sides)):
        return 1
    return 2
