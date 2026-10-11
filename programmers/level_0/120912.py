# 120912
# 7의 개수

# str([1, 2, 3]) # '[1, 2, 3]'

def solution(array):
    answer = 0
    for each in array:
        answer += str(each).count('7')
        
    return answers
