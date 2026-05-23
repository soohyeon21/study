# 두 수의 연산값 비교하기

def solution(a, b):
    answer = max(int(str(a)+str(b)), 2*a*b)
    return answer
