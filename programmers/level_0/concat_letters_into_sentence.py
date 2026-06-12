# 글자 이어 붙여 문자열 만들기

def solution(my_string, index_list):
    answer = ''
    for idx in index_list:
        answer += my_string[idx]
    return answer
