# 순서 바꾸기

def solution(num_list, n):
    answer = num_list[n:] + num_list[:n]
    return answer
