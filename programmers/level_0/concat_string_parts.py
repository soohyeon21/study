# 부분 문자열 이어 붙여 문자열 만들기

def solution(my_strings, parts):
    answer = ''
    for i in range(len(parts)):
        s, e = parts[i][0], parts[i][1]
        answer += my_strings[i][s:e+1]
    
    return answer
