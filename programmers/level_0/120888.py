# 120888
# 중복된 문자 제거

def solution(my_string):
    answer = []
    for letter in my_string:
        if (letter not in answer):
            answer.append(letter)
            
    return ''.join(answer)
