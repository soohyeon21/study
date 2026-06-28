# 글자 지우기

def solution(my_string, indices):
    answer = list(my_string)
    for idx in indices:
        answer[idx] = ''
    
    return ''.join(answer)
