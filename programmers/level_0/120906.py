# 120906
# 자릿수 더하기

def solution(n):
    answer = 0
    for digit in str(n):
        answer += int(digit)
    return answer
