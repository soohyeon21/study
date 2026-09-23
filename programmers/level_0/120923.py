# 120923
# 연속된 수의 합

def solution(num, total):
    rest = (num-1)*num//2
    first = (total-rest)//num
    answer = [first+k for k in range(num)]
    return answer
