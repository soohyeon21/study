# 120868
# 삼각형의 완성조건 (2)

def solution(sides):
    answer = 0
    for i in range(1, sum(sides)):
        if ((i+min(sides) > max(sides)) or ((i>=max(sides)) and (i < sum(sides)))):
            answer += 1
    return answer
