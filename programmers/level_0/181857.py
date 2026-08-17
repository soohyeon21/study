# 181857
# 배열의 길이를 2의 거듭제곱으로 만들기

import math

def solution(arr):
    integer = math.ceil(math.log(len(arr), 2))
    arr.extend([0]*max(0, 2**integer-len(arr)))
    return arr
