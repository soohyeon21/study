# 배열의 원소만큼 추가하기

def solution(arr):
    answer = []
    for num in arr:
        answer.extend([num for x in range(num)])
    return answer
