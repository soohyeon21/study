# 9로 나눈 나머지

def solution(number):
    answer = sum(int(digit) for digit in number) % 9
    return answer
