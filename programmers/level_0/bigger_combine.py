# 더 크게 합치기

def solution(a, b):
    answer = max(int(str(a)+str(b)), int(str(b)+str(a)))
    return answer
