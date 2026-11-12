# 120864
# 숨어있는 숫자의 덧셈 (2)

def solution(my_string):
    digits = ''
    for i in range(len(my_string)):
        if (my_string[i].isalpha()):
            digits += ' '
        else:
            digits += my_string[i]
    
    digits = digits.split()
    
    if (len(digits) == 0):
        return 0
    
    answer = 0
    for each in digits:
        answer += int(each)
    return answer
