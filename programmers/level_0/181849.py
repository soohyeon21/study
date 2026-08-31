# 181849
# 문자열 정수의 합

def solution(num_str):
    return sum(int(digit) for digit in num_str)
    # return sum(map(int, num_str)) # 이것도 가능.
