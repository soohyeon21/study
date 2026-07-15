# n보다 커질 때까지 더하기

def solution(numbers, n):
    ssum = 0
    for i in range(len(numbers)):
        ssum += numbers[i]
        if (ssum > n):
            return ssum
