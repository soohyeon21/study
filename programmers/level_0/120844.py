# 120844
# 배열 회전시키기

def solution(numbers, direction):
    answer = []
    if (direction == 'left'):
        answer = numbers[1:] + [numbers[0]]
    elif (direction == 'right'):
        answer = [numbers[-1]] + numbers[:-1]
    
    return answer
