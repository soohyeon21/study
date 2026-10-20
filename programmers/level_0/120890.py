# 120890
# 가까운 수

def solution(array, n):
    answer = 101
    diff = 101
    for num in array:
        if (abs(n-num) < diff):
            print(num, abs(n-num), diff)
            answer = num
            diff = abs(n-num)
        elif (abs(n-num) == diff):
            answer = min(num, answer)
            
    return answer
